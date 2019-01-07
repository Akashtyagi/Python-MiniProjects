# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 00:35:31 2018

@author: Akash
"""


import folium
import pandas as pd

data = pd.read_csv("college.csv")

def elevation_color(elevation):
    if 0 < elevation < 1000:
        return "green"
    elif 1000 < elevation < 2500:
        return "blue"
    elif 2500 < elevation:
        return "red"
    

map = folium.Map(location=[20.59,78.96], zoom_start=0,tiles = "Mapbox Bright")
fg= folium.FeatureGroup(name="My map")

for college_name,lat,lon in zip(data["College Name"],data["Latitude"],data["Longitude"]):
    fg.add_child(folium.Marker(location=[lat,lon],popup=folium.Popup(str(college_name),parse_html=True),icon = folium.Icon(color="green")))

fg.add_child(folium.GeoJson(data=open("world.json",encoding="utf-8-sig").read(),
                            style_function=lambda x: {"fillColor":"green"}))
folium.LayerControl().add_to(map)
map.add_child(fg)

map.save("CollegeList.html")