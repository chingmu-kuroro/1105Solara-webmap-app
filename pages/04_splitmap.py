import solara
import leafmap.leafmap as leafmap


def create_map():

    m = leafmap.Map()
    m.split_map(
        left_layer="NLCD 2001 CONUS Land Cover",
        right_layer="NLCD 2016 CONUS Land Cover",
        left_label="2001",
        right_label="2016",
        label_position="bottom",
        center=[36.1, -114.9],
        zoom=10,
        )
    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()