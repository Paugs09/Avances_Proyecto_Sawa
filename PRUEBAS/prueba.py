import folium 
mymap =folium.Map(
    location=[40,2.1],
    tiles='OpenStreetMap',
    zoom_start=10

)

mymap.save('index.html')