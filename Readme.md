# Sistema Inteligente de Rutas en Transporte Masivo con Python

## Descripción
Este proyecto implementa un sistema inteligente para encontrar la mejor ruta desde un punto A a un punto B dentro de un sistema de transporte masivo utilizando **Python**, **Pandas** y el algoritmo de búsqueda en anchura (**BFS**).

El sistema utiliza una **base de conocimiento** representada en un **DataFrame de Pandas**, donde cada fila del DataFrame representa una conexión directa entre dos paradas. Luego, el algoritmo BFS busca la ruta más corta entre las paradas de inicio y destino.

## Estructura del Proyecto
- `sistema_rutas.py`: Archivo principal que contiene el código para la búsqueda de la mejor ruta.
- `README.md`: Este archivo de documentación.

## Requisitos
- Python 3.x
- Librerías:
  - `pandas`
  - `collections` (ya incluida en Python)

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/sistema-inteligente-rutas.git
   ```

2. Instalar la dependencia de pandas
```bash
pip install pandas
```
3. Para ejecurar el proyecto, necesitan escribir en la consola el siguiente comando:

```bash
python MovementIA.py
```