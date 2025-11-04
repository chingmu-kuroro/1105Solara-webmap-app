import solara
import page_home  # 1. 匯入您的頁面檔案
import page_map_2d # (稍後會建立)

# --- 2. 定義路由 (網站地圖) ---
routes = [
    # 路徑 "/" 會執行 page_home.py 裡的 Page 元件
    solara.Route(path="/", component=page_home.Page, label="專案首頁"),
    # 路徑 "/map-2d" 會執行 page_map_2d.py 裡的 Page 元件
    solara.Route(path="/map-2d", component=page_map_2d.Page, label="2D 互動地圖"),
]

# --- 3. 定義主佈局 (Layout)，包含導覽 ---
@solara.component
def Layout(main_content):
    router = solara.use_router() # 取得路由控制器

    # 1. 使用 solara.AppLayout 作為根容器
    #    它會自動提供 AppBar 和 Sidebar 所需的「插槽」
    with solara.AppLayout() as main:
        
        # 2. 這個 AppBar 會被「傳送」到 AppLayout 的頂部插槽
        with solara.AppBar(color="primary"):
            solara.Markdown("### 🌍 我的 Solara GIS App (台灣)")
        
        # 3. 這個 Sidebar 會被「傳送」到 AppLayout 的側邊插槽
        with solara.Sidebar():
            solara.Markdown("## 導覽選單")
            with solara.ButtonGroup(vertical=True):
                for route in routes:
                    solara.Button(
                        label=route.label,
                        on_click=lambda r=route: router.push(r.path), 
                        text=True,
                    )
                        
        # 4. 關鍵：將 main_content (您的頁面) 放置在 AppLayout 的「主要內容區域」
        main_content
    
    # 5. 回傳「整個」佈局
    return main

# --- 4. 建立 App ---
@solara.component
def Page():
    # Router 會自動根據 routes 列表，將當前 URL 對應的 component
    # 渲染為 main_content，並傳遞給 Layout
    return solara.Router(routes=routes, layout=Layout)