import pandas as pd
import folium

# Leer el archivo Excel y limitar a las primeras 500 filas
df = pd.read_excel('data.xlsx')
df = df[(df['magnitud (M)'] >= 6) & (df['profundidad (km)'] < 100)]
# Crear el mapa centrado en la región de interés (Perú)
m = folium.Map(location=[-9.19, -75.0152], zoom_start=5)

# Función para asignar color según la magnitud
def color_por_magnitud(magnitud):
    if magnitud >= 7:
        return 'red'
    elif magnitud >= 6.5:
        return 'orange'
    elif magnitud >= 6:
        return 'blue'
    else:
        return 'blue'  # Puedes ajustar este color para sismos más débiles

# Añadir marcadores al mapa
for index, row in df.iterrows():
    lat = row['latitud']
    lon = row['longitud']
    magnitud = row['magnitud (M)']
    
    # Obtener color según la magnitud
    color = color_por_magnitud(magnitud)
    
    # Añadir marcador con color personalizado
    folium.CircleMarker(
        location=[lat, lon],
        radius=5,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.7,
        popup=f'Magnitud: {magnitud}'
    ).add_to(m)

# Guardar el mapa en un archivo HTML
m.save('mapa_terremotos.html')
