# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 23:11:36 2018

@author: Akash
"""

import folium
import pandas as pd

data = pd.read_csv("Volcanoes_USA.csv")
latitude = data["LAT"]
longitude = data["LON"]
name = data["NAME"]

def elevation_color(elevation):
    if 0 < elevation < 1000:
        return "green"
    elif 1000 < elevation < 2500:
        return "blue"
    elif 2500 < elevation:
        return "red"
    

map = folium.Map(location=[20.59,78.96], zoom_start=0,tiles = "Mapbox Bright")
fg= folium.FeatureGroup(name="My map")

for lat,lon,name,el in zip(latitude,longitude,name,data["ELEV"]):
    fg.add_child(folium.Marker(location=[lat,lon],popup=folium.Popup(str(name),parse_html=True),icon = folium.Icon(color=elevation_color(el))))

#folium.Marker(location=[26.80,80.76],popup="Hey, Moradabad").add_to(map)
map.add_child(fg)

map.save("mapOutput.html")