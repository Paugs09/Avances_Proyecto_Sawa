import folium
import pandas as pd
import webbrowser 
webbrowser.open('https://www.python.org')

mapa=folium.Map(location=[4.570868,-74.297333],zoom_start=5)

mapa.save('mimapa.html')
webbrowser.open("mimapa.html")
