import solara

# 1. 匯入您所有的頁面
import page_home
import page_map_2d
#import page_split_map
#import page_map_3d_vector
#import page_map_3d_raster
#import page_split_map_3d
# (未來在這裡匯入您所有的 page_*.py 檔案)


# --- 2. 將「路由」定義為「全域變數」 ---
# 這是您 App 唯一的「路由真相來源 (Single Source of Truth)」
# Solara 會自動尋找這個名為 'routes' 的全域列表
routes = [
    solara.Route(path="/", component=page_home.Page, label="專案首頁"),
    solara.Route(path="/map-2d", component=page_map_2d.Page, label="2D 互動地圖"),
    #solara.Route(path="/split-map", component=page_split_map.Page, label="2D 捲簾圖台"),
    #solara.Route(path="/map-3d-vector", component=page_map_3d_vector.Page, label="3D 向量 (台北)"),
    #solara.Route(path="/map-3d-raster", component=page_map_3d_raster.Page, label="3D 網格 (台灣)"),
    #solara.Route(path="/split-map-3d", component=page_split_map_3d.Page, label="3D 捲簾圖台"),
]


# --- 3. 客製化您的 App 標題 ---
# Solara 會自動尋找名為 'Layout' 的元件
# 但我們使用一個更簡單的方法來客製化
@solara.component
def Layout(children):
    # 使用 Solara 內建的 AppLayout
    # 它會自動讀取全域的 'routes' 列表來建立側邊欄
    return solara.AppLayout(
        title="🌍 我的 Solara GIS App (台灣)",
        children=children
    )