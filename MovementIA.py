import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

# Cargar el dataset Iris desde scikit-learn
iris = load_iris()

# Crear arrays NumPy para características (X) y etiquetas (y)
X = iris.data
y = iris.target

# Mostrar las primeras 5 filas del array
print("Datos de Iris (primeras 5 filas):")
print(X[:5])

# Dividir los datos en conjunto de entrenamiento y prueba (80% - 20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar un modelo Random Forest
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Realizar predicciones con el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluar el modelo con precisión
accuracy = accuracy_score(y_test, y_pred)
print(f"\nPrecisión del modelo: {accuracy * 100:.2f}%")