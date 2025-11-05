# pages/01_globe.py

import solara
import leafmap.maplibregl as leafmap 
from maplibre import Layer 

@solara.component
def Page():
    
    # --- 1. (關鍵修正) 將 create_map 定義為一個「普通的內部函式」 ---
    #    (不要在它上面加 @solara.use_memo)
    def create_map():
        
        m = leafmap.Map(
            style="satellite",        
            center=[121.5654, 25.0330], # 台北 101
            zoom=11,                  
            pitch=50,                 
            bearing=-30,              
            sidebar_visible=True,
            height="750px",
        )

        # --- 加入 3D 地形 ---
        aws_terrain_url = "https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png"
        
        m.add_source(
            "terrain_source", 
            {
                "type": "raster-dem", 
                "tiles": [aws_terrain_url],
                "tileSize": 256,
                "encoding": "terrarium", 
            }
        )
        m.set_terrain(source="terrain_source", exaggeration=1.0)
        
        # --- 加入台北捷運路網 (向量) ---
        mrt_url = "https://drive.google.com/uc?id=1RwHIhfEINPFRYUCToMJzaOIEXLPNmZjX"
        paint = {"line-color": "#FFD700", "line-width": 3}
        
        # 步驟 A：新增 GeoJSON 資料「來源」
        m.add_source(
            "mrt_source", 
            {"type": "geojson", "data": mrt_url}
        )
        
        # 步驟 B：新增一個「圖層」來「繪製」這個來源
        m.add_layer(
            Layer(
                id="mrt_layer",             
                type="line",              
                source="mrt_source",        
                paint=paint               
            )
        )
        
        return m
    
    # --- 2. (關鍵修正) 使用 Solara Hook 的「正確語法」 ---
    # solara.use_memo 是一個「函式」，它接收 create_map 作為參數
    # dependencies=[] 告訴 Solara 這個快取永遠不需要過期
    m = solara.use_memo(create_map, dependencies=[])
    
    # --- 3. 保持樣板的原始渲染方式 ---
    return m.to_solara()