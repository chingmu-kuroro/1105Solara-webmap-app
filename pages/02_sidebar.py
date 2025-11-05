import solara
import leafmap.maplibregl as leafmap


def create_map():

    m = leafmap.Map(
        style="liberty",
        #projection="globe",
        center=[122.19861, 23.59333],  # 台東市
        zoom=13, 
        pitch=60, 
        bearing=150, 
        height="750px",
        sidebar_visible=True,
    )

    m.add_ee_layer(asset_id="ESA/WorldCover/v200", opacity=0.8)

    aws_terrain_url = "https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png"
    m.add_source(
        "terrain_source", 
        {
            "type": "raster-dem", 
            "tiles": [aws_terrain_url],
            "tileSize": 256,
            "encoding": "terrarium", 
        }
    )
    m.set_terrain(source="terrain_source", exaggeration=3) # 垂直誇張 3 倍



    m.add_legend_to_sidebar(
        builtin_legend="ESA_WorldCover", title="Land Cover Type", shape_type="rectangle"
    )
    m.add_colorbar_to_sidebar(cmap="terrain", label="Elevation")

    image = "https://i.imgur.com/KeiAsTv.gif"
    m.add_image_to_sidebar(image=image, expanded=False)

    video = "https://static-assets.mapbox.com/mapbox-gl-js/drone.mp4"
    m.add_video_to_sidebar(video, expanded=False)
    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()