from streamlit_folium import st_folium
import folium
from weather_icon import get_icon

def render_map(selected_date):

    regionalCoords = [
    [48.14244663381307, -2.8732976551510263],
    [49.01203292123912, 0.15538061753084026],
    [49.97415434164336, 2.8261190286911333],
    [48.71212499407923, 2.5523685049282405],
    [47.439278433081036, 1.7071332414921612],
    [45.10197257034414, 0.09584511043028773],
    [43.58037639713084, 2.169507159438924],
    [43.83998471721191, 6.162653828372608],
    [45.40905180537371, 4.326744974917686],
    [47.12840752815982, 5.067991805604691],
    [48.76520936142879, 5.440004567794441]
    ]
        # center on France
    m = folium.Map(location=[46.6714327602744, 2.5419523299087947], zoom_start=6)

    folium.Marker(
            location=[48.14244663381307, -2.8732976551510263],
            icon=folium.Icon(color='lightgray', icon="cloud", icon_color='white', prefix='fa')   ).add_to(m)
    
    for regionCoords in regionalCoords:
        # TODO get weather and calculate icon
        iconName = get_icon(regionCoords, selected_date)

        folium.Marker(
            location=regionCoords,
            icon=folium.Icon(color='lightgray', icon=iconName, icon_color='white', prefix='fa', tooltip=)   ).add_to(m)

    #for key, value in iconsDict.items():
    #    folium.Marker(
    #        location=value,
    #        icon=folium.Icon(color='lightgray', icon=key, icon_color='white', prefix='fa')
    #    ).add_to(m)

    # call to render Folium map in Streamlit
    st_data = st_folium(m, width = 725)