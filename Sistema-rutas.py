import pandas as pd
from geopy.distance import geodesic
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
import matplotlib.pyplot as plt

# Cargar el dataset de estaciones
estaciones_df = pd.read_csv('dataset/Paraderos SITP.csv')  # Cambia 'ruta/del/dataset.csv' por tu archivo

# Limpiar los nombres de las columnas
estaciones_df.columns = estaciones_df.columns.str.strip()


# Ejemplo: crear un dataframe de conexiones (si no lo tienes ya)
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


# Generar las conexiones entre estaciones
rutas_df = generar_conexiones(estaciones_df)

# Supongamos que la duración del viaje se estima de alguna manera (puedes cambiar esto según tu dataset)
# Por ejemplo, aquí generamos una duración ficticia basada en la distancia (en minutos)
rutas_df['Duración'] = rutas_df['Distancia'] * 2  # Asumiendo 2 minutos por km

# Preprocesar el dataset para el modelo
X = rutas_df[['Distancia']]
y = rutas_df['Duración']

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Hacer predicciones
y_pred = model.predict(X_test)

# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
print(f"Error Cuadrático Medio: {mse:.2f}")

# Visualizar las predicciones vs los valores reales
plt.scatter(y_test, y_pred)
plt.xlabel('Duración Real')
plt.ylabel('Duración Predicha')
plt.title('Predicciones de Duración del Viaje')
plt.show()

# Guardar el modelo entrenado
joblib.dump(model, 'modelo_duracion_viaje.pkl')
