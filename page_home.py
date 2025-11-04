import solara
@solara.component
def Page():
    solara.Title("首頁")
    solara.Markdown("# 歡迎來到 Solara GIS 儀表板 (台灣)")
    solara.Markdown("請使用左側選單切換頁面，探索台灣的 2D 與 3D 地理圖資。")