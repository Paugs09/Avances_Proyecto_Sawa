import folium 
import pandas as pd
import webbrowser 
webbrowser.open('https://www.python.org')

mapa=folium.Map(location=[6.5595200,-73.1363700], zoom_start=30)

mapa.save('sangil.html')
webbrowser.open('sangil.html')