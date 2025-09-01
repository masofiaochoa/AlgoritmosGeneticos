import warnings
import pandas
from sklearn.linear_model import LinearRegression, ElasticNet, Lasso, Ridge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from pathlib import Path

# Solo ejecutar el entrenamiento si este archivo se ejecuta directamente
if __name__ == "__main__":
    # TRAINING THE MODEL
    # ver los datos para ver qué elegimos

    # Obtener la ruta del directorio donde está este archivo
    current_dir = Path(__file__).parent
    filename = current_dir / 'modelo_final_ml.csv'  # Usar ruta absoluta
    names = ['vel_prom_viento', 'dir_prom_viento', 'distancia_mts','tiempo_minutos'] #nombre de las columnas
    df = pandas.read_csv(filename,names=names, skiprows=1)

    array = df.values
    X = array[:,0:3] #los datos fijos, las columnas: velocidad del viento, direccion del viento y distancia
    Y = array[:,3] #La variable a calcular: tiempo

    # Group of scoring metrics
    # sirven para evaluar el modelo de machine learning
    #max_error_scoring = 'max_error'
    neg_mean_absolute_error_scoring = 'neg_mean_absolute_error'
    r2_scoring = 'r2'
    neg_mean_squared_error_scoring = 'neg_mean_squared_error'

    # Definición de modelos a usar para entrenar y evaluar el dataset
    models = []
    models.append(('LR', LinearRegression())) 
    models.append(('LASSO', Lasso())) 
    models.append(('EN', ElasticNet())) 
    models.append(('Ridge', Ridge())) 
    models.append(('KNN', KNeighborsRegressor())) 
    models.append(('CART', DecisionTreeRegressor())) 
    models.append(('SVR', SVR())) 

    # Evaluar cada modelo e imprimir los resultados
    results = []
    names = []

    #para cada nombre de modelo y modelo en la list de modelos
    for name, model in models:

        # kfold validation
        # divide los datos en 5 partes iguales (n_splits=5) y se fija en 7 el valor de random
        kfold = KFold(n_splits=5, shuffle=True, random_state=7) #kfold validation

        # se corren 4 runs, cada una con una métrica diferente
        #cv_results = cross_val_score(model, X, Y, cv=kfold, scoring=max_error_scoring) cv_results.mean()
        cv_results2 = cross_val_score(model, X, Y, cv=kfold, scoring=neg_mean_absolute_error_scoring)
        cv_results3 = cross_val_score(model, X, Y, cv=kfold, scoring=r2_scoring)
        cv_results4 = cross_val_score(model, X, Y, cv=kfold, scoring=neg_mean_squared_error_scoring)
        msg = "%s: mean absolute error: %f, r2: %f, mean squared error: %f" % (name, -cv_results2.mean(),cv_results3.mean(),-cv_results4.mean())
        print(msg)

    # dado el analisis, elegimos Ridge Regression
    # podriamos usar otro pero nos faltan datos (tenemos 11 filas nada más)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=1, shuffle=True)

    lasso_model = Lasso()
    lasso_model.fit(X_train, Y_train) #la funcion fit() es para entrenar el modelo de ML

    # tira un predict random, para ver que funcione bien el modelo
    predictions = lasso_model.predict(X_test)
    print(predictions)

else:
    # Cuando se importa desde otro archivo, solo entrenar el modelo sin prints
    current_dir = Path(__file__).parent
    filename = current_dir / 'modelo_final_ml.csv'
    names = ['vel_prom_viento', 'dir_prom_viento', 'distancia_mts','tiempo_minutos']
    df = pandas.read_csv(filename, names=names, skiprows=1)
    
    array = df.values
    X = array[:,0:3]
    Y = array[:,3]
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=1, shuffle=True)
    
    lasso_model = Lasso()
    lasso_model.fit(X_train, Y_train)

