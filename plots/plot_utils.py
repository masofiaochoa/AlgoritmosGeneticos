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
    plt.ylabel("Valor de fitness")
    plt.ylim(-0.05, 1.05)
    plt.grid()
    plt.show()