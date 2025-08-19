import pickle
from trainingData import * #archivo donde entrené el modelo

import numpy as np
from sklearn.linear_model import Ridge  

class Model:
    def __init__(self):
        #pickle -> serializar el modelo (convertilo a un archivo)
        #para ver y reusar el modelo de ML
        pickle.dump(ridge_model, open('model.pkl','wb')) #serializar -> de modelo a archivo

        # cargar el modelo previamente entrenado
        self.model = pickle.load(open('model.pkl','rb')) #deserializar -> de archivo a modelo

    def predict(self, vel_prom_viento: float, dir_prom_viento: float, distancia_mts: float):
        input_data = np.array([[vel_prom_viento, dir_prom_viento, distancia_mts]])
        return self.model.predict(input_data)
    
if __name__ == "__main__":
    # Ejemplo de uso
    ml_model = Model()

    # Valores de prueba
    vel_prom_viento = 10.0
    dir_prom_viento = 45.0
    distancia_mts = 25.0
  
    predicted_time = ml_model.predict(vel_prom_viento, dir_prom_viento, distancia_mts)
    print(f"Tiempo estimado aproximado: {predicted_time[0]:.2f} minutos")
