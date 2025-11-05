import solara
import leafmap.leafmap as leafmap

# --- 1. 建立左側 3D 地圖 (m1) ---
m1 = leafmap.Map(
    use_maplibregl=True,
    center=[120.957, 23.470], # 玉山
    zoom=10,
    pitch=60,
    style="satellite",
    layout_height="800px"
)
aws_terrain_url = "https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png"
m1.add_terrain(source=aws_terrain_url, layer_id="terrain")

# --- 2. 建立右側 2D 地圖 (m2) ---
m2 = leafmap.Map(
    use_maplibregl=True,
    center=[120.957, 23.470], # 玉山
    zoom=10,
    pitch=0, # <-- 設為 0 度 (2D)
    style="positron", # 使用 2D 街道圖
    layout_height="800px"
)

# --- 3. 建立捲簾 ---
@solara.component
def Page():
    solara.Title("3D/2D 捲簾對比")
    
    # 使用 leafmap 內建的 split_map 功能
    split_control = leafmap.split_map(
        m1, m2,
        left_label="3D 衛星地形",
        right_label="2D 街道圖"
    )
    
    # .element 將 ipywidget 轉為 Solara 元件
    return split_control.element