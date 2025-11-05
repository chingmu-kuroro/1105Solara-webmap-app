# pages/01_globe.py

import solara
import leafmap.maplibregl as leafmap

# 我們不再在「全域」定義 create_map。
# 而是直接定義 Page 元件。

@solara.component
def Page():
    
    # --- 1. 將 create_map (包含 @solara.use_memo) ---
    # ---    「移到」元件內部 ---
    # 這樣 @solara.use_memo 就會在「渲染情境」中被呼叫
    @solara.use_memo
    def create_map():
        # 這裡所有的繁重工作只會執行一次
        m = leafmap.Map(
            style="satellite",        
            center=[121.5654, 25.0330], # 台北 101
            zoom=11,                  
            pitch=50,                 
            bearing=-30,              
            sidebar_visible=True,
            height="750px", # (注意：您樣板中的 height 移到這裡)
        )

        # --- 加入 3D 地形 ---
        aws_terrain_url = "https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png"
        m.add_terrain(source=aws_terrain_url, layer_id="terrain")

        # --- 加入台北捷運路網 ---
        mrt_url = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/master/taipei-mrt.geojson"
        paint = {"line-color": "#FFD700", "line-width": 3}
        m.add_geojson(mrt_url, layer_name="台北捷運路網", paint=paint)

        return m
    
    # --- 2. 呼叫快取函式來取得地圖 ---
    m = create_map()
    
    # 3. 渲染地圖
    return m.to_solara()