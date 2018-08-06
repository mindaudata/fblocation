import re
import pandas


def get_coords(fb_file):
    df = pandas.DataFrame(columns=['lat', 'lon'])
    with open(fb_file, 'r') as fl:
        for line in fl:
            findings = re.findall(r'[+-]?\d+\.\d+,\s[+-]?\d+\.\d+', line)
            for i in range(len(findings)):
                la, lo = findings[i].split(sep=', ')
                df = df.append({'lat': la, 'lon': lo}, ignore_index=True)
    return df


import folium

def create_map(df):
    map = folium.Map(location=[54.7037527, 25.2837174],
                     zoom_start=6, tiles='Mapbox Bright')
    fg = folium.FeatureGroup(name='Facebook Tracked Locations')

    for index, row in df.iterrows():
        fg.add_child(folium.CircleMarker(location=[float(row['lat']), float(
            row['lon'])], radius=5, color='#3b5998', fill=True))
    map.add_child(fg)

    map.save('templates/tracked.html')
