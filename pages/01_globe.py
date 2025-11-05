import solara
import leafmap.maplibregl as leafmap

# 1. 使用 @solara.use_memo (快取裝飾器)
# 這能確保地圖與資料只會在 App 啟動時載入一次
# 避免了頁面切換或互動時的重新載入，效能更佳
@solara.use_memo
def create_map():

    m = leafmap.Map(
        style="satellite",        # 改用衛星底圖 (免費)
        # projection="globe",     # 移除 "globe" 投影
        height="750px",
        center=[121.5654, 25.0330], # 2. (修改) 中心點設為台北 (台北 101)
        zoom=11,                  # 3. (修改) 放大到城市尺度
        pitch=50,                 # 4. (新增) 加入 3D 傾斜角度
        bearing=-30,              # (選用) 旋轉一個角度
        sidebar_visible=True,
    )

    # 5. (新增) 加入 3D 地形 (網格) ---
    # 使用免費的 AWS (Amazon Web Services) 全球地形圖磚
    aws_terrain_url = "https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png"
    m.add_terrain(
        source=aws_terrain_url, 
        layer_id="terrain"
    )

    # 6. (新增) 加入台北捷運路網 (向量) ---
    # 從投影片提供的 GitHub Repo 中找到 GeoJSON 的「原始 (Raw)」連結
    mrt_url = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/master/taipei-mrt.geojson"
    
    # 為捷運線條設定顏色和寬度
    paint = {"line-color": "#FFD700", "line-width": 3}
    
    m.add_geojson(
        mrt_url,
        layer_name="台北捷運路網",
        paint=paint,
    )

    return m


@solara.component
def Page():
    # 呼叫快取的函式來取得地圖物件
    m = create_map()
    
    # m.to_solara() 是舊版 leafmap 的寫法，m.element 是新版
    # 兩者在 Solara 中通常都能運作
    return m.to_solara()