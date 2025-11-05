# pages/01_globe.py

import solara
# 保持樣板的原始匯入
import leafmap.maplibregl as leafmap 
from maplibre import Layer # ⬅️ 1. (新增) 我們需要手動匯入 Layer 物件

@solara.component
def Page():
    
    @solara.use_memo
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

        # --- 加入 3D 地形 (這部分是正確的) ---
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
        
        # --- 4. (關鍵修正) 手動加入台北捷運路網 ---
        
        mrt_url = "https://drive.google.com/uc?id=1RwHIhfEINPFRYUCToMJzaOIEXLPNmZjX"
        paint = {"line-color": "#FFD700", "line-width": 3}
        
        # 步驟 A：新增 GeoJSON 資料「來源」
        m.add_source(
            "mrt_source", # 1. 給資料來源一個 ID
            {"type": "geojson", "data": mrt_url} # 2. 告訴它資料在哪裡
        )
        
        # 步驟 B：新增一個「圖層」來「繪製」這個來源
        m.add_layer(
            Layer(
                id="mrt_layer",             # 1. 給圖層一個 ID
                type="line",              # 2. 告訴它畫「線」
                source="mrt_source",        # 3. 告訴它使用哪個「資料來源」
                paint=paint               # 4. 告訴它如何畫 (顏色/寬度)
            )
        )
        
        # (我們不再使用 m.add_geojson(...) 函式)
        # ⬆️ ⬆️ ⬆️ 關鍵修正 ⬆️ ⬆️ ⬆️

        return m
    
    # --- 呼叫快取函式來取得地圖 ---
    m = create_map()
    
    # --- 保持樣板的原始渲染方式 ---
    return m.to_solara()