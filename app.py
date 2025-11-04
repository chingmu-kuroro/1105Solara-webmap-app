import solara
import page_home
import page_map_2d
# --- 未來在這裡匯入所有新頁面 ---
# import page_split_map
# import page_map_3d_vector
# import page_map_3d_raster
# import page_split_map_3d


# --- 1. 定義主佈局 (Layout) ---
# 這個元件負責「外殼」(AppBar, Sidebar)
@solara.component
def Layout(children): # 從 Router 接收當前頁面作為 'children'
    router = solara.use_router()
    
    # ⬇️ ⬇️ ⬇️ 關鍵：這是從 Router 安全地取得 routes 列表的方法 ⬇️ ⬇️ ⬇️
    # 1. 取得當前 router 的「情境 (context)」
    router_context = solara.use_context(solara.routing.router_context)
    # 2. 從 context 中取得 routes 列表 (如果 context 尚未準備好，就給一個空列表)
    routes = router_context.routes if router_context else []
    # ⬆️ ⬆️ ⬆️ 關鍵 ⬆️ ⬆️ ⬆️

    # 使用 Solara 內建的 AppLayout 元件作為根容器
    with solara.AppLayout() as main:
        
        # 這個 AppBar 會被自動放置在頂部
        with solara.AppBar():
            solara.Markdown("### 🌍 我的 Solara GIS App (台灣)")
            
        # 這個 Sidebar 會被自動放置在左側
        with solara.Sidebar():
            solara.Markdown("## 導覽選單")
            
            # 我們從 context 取得的 routes 列表在這裡被用來建立按鈕
            for route in routes:
                solara.Button(
                    label=route.label,
                    on_click=lambda r=route: router.push(r.path), 
                    text=True,
                )
        
        # 顯示 Router 傳來的頁面內容
        children
        
    return main


# --- 2. 建立 App (唯一的進入點) ---
# Solara 會尋找這個 'Page' 元件，因為它找不到全域的 'routes'
@solara.component
def Page():
    # ⬇️ ⬇️ ⬇️ 關鍵：在這裡「唯一定義」routes ⬇️ ⬇️ ⬇️
    # 這是您 App 唯一的「路由真相來源 (Single Source of Truth)」
    routes = [
        solara.Route(path="/", component=page_home.Page, label="專案首頁"),
        solara.Route(path="/map-2d", component=page_map_2d.Page, label="2D 互動地圖"),
        
        # --- 未來在這裡加入所有新頁面 ---
        # solara.Route(path="/split-map", component=page_split_map.Page, label="2D 捲簾圖台"),
        # solara.Route(path="/map-3d-vector", component=page_map_3d_vector.Page, label="3D 向量 (台北)"),
        # solara.Route(path="/map-3d-raster", component=page_map_3d_raster.Page, label="3D 網格 (台灣)"),
        # solara.Route(path="/split-map-3d", component=page_split_map_3d.Page, label="3D 捲簾圖台"),
    ]
    # ⬆️ ⬆️ ⬆️ 關鍵 ⬆️ ⬆️ ⬆️
    
    # 建立 Router，並將 'routes' 和 'Layout' 傳給它
    return solara.Router(routes=routes, layout=Layout)