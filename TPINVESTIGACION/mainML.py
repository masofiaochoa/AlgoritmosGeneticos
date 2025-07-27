import pickle
from trainingData import * #archivo donde entrené el modelo

import numpy as np
from sklearn.linear_model import Ridge  

#pickle -> serializar el modelo (convertilo a un archivo)
#para ver y reusar el modelo de ML
pickle.dump(ridge_model, open('model.pkl','wb')) #serializar -> de modelo a archivo

# cargar el modelo previamente entrenado
ridge_model = pickle.load(open('model.pkl','rb')) #deserializar -> de archivo a modelo

# Ingreso de datos (manuales por ahora)
print("Ingrese los valores para predecir el tiempo (en minutos):")
vel_prom_viento = float(input("Velocidad promedio del viento (km/h): "))
dir_prom_viento = float(input("Dirección promedio del viento (en grados): "))
distancia_mts = float(input("Distancia (en metros): "))

# Realizar la predicción
input_data = np.array([[vel_prom_viento, dir_prom_viento, distancia_mts]])
predicted_time = ridge_model.predict(input_data)

print(f"\nTiempo estimado aproximado: {predicted_time[0]:.2f} minutos") #lo corta en 2 decimales
print("Tiempo estimado real:", predicted_time[0])
