import pandas as pd
from collections import deque

# Definir las rutas como un DataFrame de Pandas
data = {
    'Inicio': ['A', 'A', 'B', 'B', 'C', 'D', 'E', 'F'],
    'Destino': ['B', 'C', 'D', 'E', 'F', 'G', 'G', 'G']
}
rutas_df = pd.DataFrame(data)


# Función para obtener vecinos de un nodo (parada)
def obtener_vecinos(rutas_df, nodo):
    return rutas_df[rutas_df['Inicio'] == nodo]['Destino'].tolist()


# Función para buscar la mejor ruta utilizando BFS
def buscar_ruta(rutas_df, inicio, destino):
    # Cola para almacenar los caminos posibles
    cola = deque([[inicio]])

    # Conjunto para rastrear los nodos visitados
    visitados = set()

    while cola:
        # Extraer el primer camino de la cola
        camino = cola.popleft()

        # Obtener el último nodo en el camino actual
        nodo = camino[-1]

        # Verificar si hemos llegado al destino
        if nodo == destino:
            return camino

        # Si el nodo no ha sido visitado, continuar la búsqueda
        if nodo not in visitados:
            # Marcar el nodo como visitado
            visitados.add(nodo)

            # Obtener los vecinos del nodo actual desde el DataFrame
            vecinos = obtener_vecinos(rutas_df, nodo)
            for vecino in vecinos:
                nuevo_camino = list(camino)  # Crear un nuevo camino
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)

    # Si no se encuentra un camino al destino
    return None


# Probar el sistema buscando la mejor ruta desde A hasta G
inicio = "A"
destino = "G"
ruta = buscar_ruta(rutas_df, inicio, destino)

if ruta:
    print(f"La mejor ruta desde {inicio} hasta {destino} es: {' -> '.join(ruta)}")
else:
    print(f"No se encontró una ruta desde {inicio} hasta {destino}.")
