import folium
import pandas as pd
import webbrowser 
webbrowser.open("https://www.python.org")

mapa_Curiti=folium.Map(location=[6.61,-73.07167], zoom_start=30)

mapa_Curiti.save('curiti.html')
webbrowser.open('curiti.html')
