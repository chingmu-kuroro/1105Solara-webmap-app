import solara
import leafmap.maplibregl as leafmap 

@solara.component
def Page():
    
    @solara.use_memo
    def create_map():
        
        # --- 2. 使用樣板的「輕量級」Map 物件 ---
        m = leafmap.Map(
            style="satellite",        
            center=[121.5654, 25.0330], # 台北 101
            zoom=11,                  
            pitch=50,                 
            bearing=-30,              
            sidebar_visible=True,
            height="750px",
        )

        # --- 3. (關鍵修正) 使用「手動」方式加入 3D 地形 ---
        
        # 這是 AWS 的免費地形圖磚 URL
        aws_terrain_url = "https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png"
        
        # 步驟 A：新增一個「來源 (Source)」
        m.add_source(
            "terrain_source", # 給這個來源一個 ID
            {
                "type": "raster-dem", # 告訴 maplibre 這是 DEM 網格
                "tiles": [aws_terrain_url],
                "tileSize": 256,
                "encoding": "terrarium", # 指定地形編碼
            }
        )
        
        # 步驟 B：告訴地圖「使用」這個來源來設定 3D 地形
        m.set_terrain(
            source="terrain_source", # 使用我們剛剛定義的 ID
            exaggeration=1.0 # 垂直誇張程度 (1.0 = 不誇張)
        )
        
        # --- 4. 加入台北捷運路網 (向量) ---
        mrt_url = "https://drive.google.com/file/d/1RwHIhfEINPFRYUCToMJzaOIEXLPNmZjX/view?usp=sharing"
        
        # (使用 add_geojson 是可以的，因為這個輕量物件也有這個輔助函式)
        paint = {"line-color": "#FFD700", "line-width": 3}
        m.add_geojson(mrt_url, layer_name="台北捷運路網", paint=paint)

        return m
    
    # --- 5. 呼叫快取函式來取得地圖 ---
    m = create_map()
    
    # --- 6. 保持樣板的原始渲染方式 ---
    return m.to_solara()