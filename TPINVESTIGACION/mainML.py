import pickle
from trainingData import * #archivo donde entrené el modelo

import numpy as np
from sklearn.linear_model import Lasso  
from pathlib import Path

class Model:
    def __init__(self):
        # cargar el modelo previamente entrenado
        current_dir = Path(__file__).parent
        model_path = current_dir / 'model.pkl'
        self.model = pickle.load(open(model_path,'rb')) #deserializar -> de archivo a modelo

    def predictTime(self, vel_prom_viento: float, dir_prom_viento: float, distancia_mts: int):
        input_data = np.array([[vel_prom_viento, dir_prom_viento, distancia_mts]])
        return self.model.predict(input_data)
    
if __name__ == "__main__":

    #pickle -> serializar el modelo (convertilo a un archivo)
    #para ver y reusar el modelo de ML
    current_dir = Path(__file__).parent
    model_path = current_dir / 'model.pkl'
    pickle.dump(lasso_model, open(model_path,'wb')) #serializar -> de modelo a archivo
    
    ml_model = Model()

    # Valores de prueba
    vel_prom_viento = float(input("Ingrese la velocidad promedio del viento (km/h): "))
    dir_prom_viento = float(input("Ingrese la dirección promedio del viento (grados): "))
    distancia_mts = int(input("Ingrese la distancia (m): "))

    predicted_time = ml_model.predictTime(vel_prom_viento, dir_prom_viento, distancia_mts)
    print(f"Tiempo estimado aproximado: {predicted_time[0]:.2f} minutos")
