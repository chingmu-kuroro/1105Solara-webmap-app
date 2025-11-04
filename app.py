# app.py (最終的、最穩健的版本)

import solara

# 1. 匯入您所有的頁面
import page_home
import page_map_2d
# --- 未來在這裡匯入所有新頁面 ---
# import page_split_map
# import page_map_3d_vector
# import page_map_3d_raster
# import page_split_map_3d


# --- 2. 將「路由」定義為「全域變數」 ---
# 這是您 App 唯一的「路由真相來源 (Single Source of Truth)」
# Solara 會自動尋找這個名為 'routes' 的全域列表
routes = [
    solara.Route(path="/", component=page_home.Page, label="專案首頁"),
    solara.Route(path="/map-2d", component=page_map_2d.Page, label="2D 互動地圖"),
    
    # --- 未來在這裡加入所有新頁面 ---
    # solara.Route(path="/split-map", component=page_split_map.Page, label="2D 捲簾圖台"),
    # solara.Route(path="/map-3d-vector", component=page_map_3d_vector.Page, label="3D 向量 (台北)"),
    # solara.Route(path="/map-3d-raster", component=page_map_3d_raster.Page, label="3D 網格 (台灣)"),
    # solara.Route(path="/split-map-3d", component=page_split_map_3d.Page, label="3D 捲簾圖台"),
]


# --- 3. 將「佈局」定義為「全域元件」 ---
# Solara 同樣會自動尋找這個名為 'Layout' 的全域元件
@solara.component
def Layout(children):
    # 'children' 參數會自動接收當前頁面 (例如 page_home.Page)
    
    # solara.AppLayout 是 Solara 內建最強大的佈局
    # 它會「自動」尋找上面定義的 'routes' 列表，並「自動」建立側邊欄按鈕
    return solara.AppLayout(
        title="🌍 我的 Solara GIS App (台灣)", # 這會顯示在頂端列
        children=children # 將當前頁面內容放入
    )

# --- 4. (刪除) ---
# 我們不再需要手動定義 Page() 元件。
# Solara 會自動使用 'routes' 和 'Layout' 來建立 App。