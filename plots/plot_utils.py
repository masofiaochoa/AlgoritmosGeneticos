import matplotlib.pyplot as plt

from individual import Individual

def drawGenData(maximums: list[Individual], minimums: list[Individual], averages: list[float]) -> None:
    """
    Draws all the necessary data for each generation. Including the maximum, minimum, and average values.
    """
    maxList: list[float] = [x.targetFunctionValue for x in maximums]
    minList: list[float] = [x.targetFunctionValue for x in minimums]

    plt.plot(maxList, label="Maximo")
    plt.plot(minList, label="Minimo")
    plt.plot(averages, label="Promedio")
    plt.title("Gráfico de la evolución de mínimos, máximos y promedios para cada generación")
    plt.legend()
    plt.xlabel("N° de generacion")
    plt.ylabel("Valor de la función objetivo")
    plt.ylim(-0.05, 1.05)
    plt.grid()
    plt.show()

def generateTable(maximums: list[Individual], minimums: list[Individual], averages: list[float]) -> None:
    
    maxList: list[float] = [bin(x.chromosome) for x in maximums]
    minList: list[float] = [bin(x.chromosome) for x in minimums]

    fig, ax = plt.subplots()
    ax.axis('tight')
    ax.axis('off')
    table_data = [["Generación", "Máximo", "Mínimo", "Promedio"]]
    for i in range(len(maxList)):
        table_data.append([str(i), str(maxList[i]), str(minList[i]), str(averages[i])])
    ax.table(cellText=table_data, loc='center', cellLoc='center')
    plt.show()