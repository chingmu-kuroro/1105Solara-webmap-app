import solara

# --- 1. 匯入您的頁面檔案
import page_home  
import page_map_2d 


# --- 2. 定義主佈局 (Layout) ---
#    (我們把 'routes' 列表從全域刪除了)
@solara.component
def Layout(children):
    router = solara.use_router()
    
    # ⬇️ ⬇️ ⬇️ 關鍵修正 ⬇️ ⬇️ ⬇️
    # A. 取得當前 router 的「情境 (context)」
    #    這能讓我們安全地存取到 Page 元件傳給 Router 的 routes
    router_context = solara.use_context(solara.routing.router_context)
    # B. 從 context 中取得 routes 列表
    #    (如果 context 尚未準備好，就給一個空列表)
    routes = router_context.routes if router_context else []
    # ⬆️ ⬆️ ⬆️ 關鍵修正 ⬆️ ⬆️ ⬆️

    with solara.AppLayout() as main:
        with solara.AppBar():
            solara.Markdown("### 🌍 我的 Solara GIS App (台灣)")
            
        with solara.Sidebar():
            solara.Markdown("## 導覽選單")
            # 現在 Layout 讀取的 routes 
            # 絕對是 Router 正在使用的那一份
            for route in routes: 
                solara.Button(
                    label=route.label,
                    on_click=lambda r=route: router.push(r.path), 
                    text=True,
                )
        
        # 顯示 Router 傳來的頁面內容
        children
        
    return main


# --- 3. 建立 App (唯一的進入點) ---
@solara.component
def Page():
    # ⬇️ ⬇️ ⬇️ 關鍵修正：在這裡「唯一定義」routes ⬇️ ⬇️ ⬇️
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
    
    # ⬆️ ⬆️ ⬆️ 關鍵修正 ⬆️ ⬆️ ⬆️
    
    # 將 routes 傳給 Router，Router 會再把 routes 
    # 和 "children" (當前頁面) 傳給 Layout
    return solara.Router(routes=routes, layout=Layout)