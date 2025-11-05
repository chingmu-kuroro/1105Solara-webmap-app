# pages/01_globe.py

import solara
import leafmap.maplibregl as leafmap 
from maplibre import Layer 

@solara.component
def Page():
    
    # 使用 solara.use_memo 快取地圖
    m = solara.use_memo(create_map, dependencies=[])
    
    # 保持樣板的原始渲染方式
    return m.to_solara()

# 將 create_map 移到頂層，這
# 是 solara.use_memo 的標準用法
def create_map():
    
    # ⬇️ ⬇️ ⬇️ 關鍵修正：使用完整的 Style URL ⬇️ ⬇️ ⬇️
    # CartoDB Dark Matter GL Style 的 JSON 連結
    dark_style_url = "https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json"
    
    m = leafmap.Map(
        style=dark_style_url,       # <-- 使用完整的 URL
        center=[121.5654, 25.0330], # 台北 101
        zoom=11,                  
        pitch=50,                 
        bearing=-30,              
        sidebar_visible=True,
        height="750px",
    )
    # ⬆️ ⬆️ ⬆️ 關鍵修正 ⬆️ ⬆️ ⬆️

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
    m.set_terrain(source="terrain_source", exaggeration=3) # (您將誇張設為 3，這很棒)
    
    # --- 加入台北捷運路網 (向量) (這部分是正確的) ---
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