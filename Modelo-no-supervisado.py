import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from geopy.distance import geodesic


estaciones_df = pd.read_csv('dataset/Paraderos SITP.csv')


estaciones_df.columns = estaciones_df.columns.str.strip()


X = estaciones_df[['Y', 'X']]


num_clusters = 3


kmeans = KMeans(n_clusters=num_clusters, random_state=42)
estaciones_df['Cluster'] = kmeans.fit_predict(X)

# Visualización de los clusters de estaciones
plt.scatter(estaciones_df['X'], estaciones_df['Y'], c=estaciones_df['Cluster'], cmap='viridis')
plt.title('Clusters de Estaciones de Transporte Masivo')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.colorbar(label='Cluster')
plt.show()

# Función para generar conexiones entre estaciones cercanas
def generar_conexiones(estaciones_df, max_distancia_km=5):
    conexiones = []
    num_estaciones = len(estaciones_df)

    for i in range(num_estaciones):
        estacion_a = estaciones_df.iloc[i]
        for j in range(i + 1, num_estaciones):
            estacion_b = estaciones_df.iloc[j]
            ubicacion_a = (estacion_a['Y'], estacion_a['X'])
            ubicacion_b = (estacion_b['Y'], estacion_b['X'])
            distancia = geodesic(ubicacion_a, ubicacion_b).km

            if distancia <= max_distancia_km:
                conexiones.append({
                    'Estacion_A': estacion_a['NTRNOMBRE'],
                    'Estacion_B': estacion_b['NTRNOMBRE'],
                    'Distancia': distancia
                })

    return pd.DataFrame(conexiones)

# Generar conexiones
rutas_df = generar_conexiones(estaciones_df)

# Guardar los resultados de los clusters y las conexiones
estaciones_df.to_csv('clusters_estaciones.csv', index=False)
rutas_df.to_csv('conexiones_estaciones.csv', index=False)

# Imprimir resumen
print(f"Total de clusters generados: {num_clusters}")
print(f"Total de conexiones generadas: {len(rutas_df)}")
