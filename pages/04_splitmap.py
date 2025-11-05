# pages/03_splitmap.py

import solara
import leafmap.leafmap as leafmap # <-- 1. 保持「重量級」 (ipyleaflet) 匯入

@solara.component
def Page():
    solara.Title("3D/2D 捲簾對比 (ipyleaflet)")
    
    # 2. (關鍵) 將地圖建立移入 use_memo，
    #    避免在「全域」執行 (這是導致您 App 啟動失敗的原因)
    @solara.use_memo
    def create_split_map():
        
        # --- 3. 建立左側 3D 地圖 (m1) ---
        m1 = leafmap.Map(
            # ⬇️ ⬇️ ⬇️ 關鍵修正 ⬇️ ⬇️ ⬇️
            # 移除 use_maplibregl=True
            basemap="SATELLITE",        # <-- 使用 ipyleaflet 的簡寫 "SATELLITE"
            # ⬆️ ⬆️ ⬆️ 關鍵修正 ⬆️ ⬆️ ⬆️
            center=[120.957, 23.470], # 玉山
            zoom=10,
            pitch=60,                 # <-- ipyleaflet 也支援 pitch
            layout_height="800px"
        )
        # add_terrain() 是 ipyleaflet 支援的函式
        aws_terrain_url = "https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png"
        m1.add_terrain(source=aws_terrain_url, layer_id="terrain")

        # --- 4. 建立右側 2D 地圖 (m2) ---
        m2 = leafmap.Map(
            # ⬇️ ⬇️ ⬇️ 關鍵修正 ⬇️ ⬇️ ⬇️
            # 移除 use_maplibregl=True
            basemap="CartoDB.Positron", # <-- 使用 ipyleaflet 的簡寫
            # ⬆️ ⬆️ ⬆️ 關鍵修正 ⬆️ ⬆️ ⬆️
            center=[120.957, 23.470], # 玉山
            zoom=10,
            pitch=0, # <-- 設為 0 度 (2D)
            layout_height="800px"
        )

        # --- 5. 建立捲簾 (現在 m1 和 m2 都是 ipyleaflet 物件) ---
        split_control = leafmap.split_map(
            m1, m2,
            left_label="3D 衛星地形",
            right_label="2D 街道圖"
        )
        
        return split_control
        
    # --- 6. 呼叫快取函式並渲染 ---
    split_map_widget = create_split_map()
    
    # .element 將 ipywidget (split_control) 轉為 Solara 元件
    return split_map_widget.element