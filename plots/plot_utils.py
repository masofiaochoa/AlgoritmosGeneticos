import matplotlib.pyplot as plt

from individual import Individual

#Dibuja todos los datos necesarios de cada generacion (Maximo, minimo, promedio, etc)
def drawGenData(maximums: list[Individual], minimums: list[Individual], averages: list[float]) -> None:
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

#Genera una hoja de calculo con todos los individuos y sus valores pertinentes (Maximo, minimo, etc)
def generateTable(maximums: list[Individual], minimums: list[Individual], averages: list[float]) -> None:
    
    maxList: list[str] = [bin(x.chromosome) for x in maximums]
    minList: list[str] = [bin(x.chromosome) for x in minimums]

    fig, ax = plt.subplots(figsize=(20, 0.25 * len(maxList)))
    ax.axis('tight')
    ax.axis('off')
    table_data = [["Generación", "Máximo", "Mínimo", "Promedio"]]
    for i in range(len(maxList)):
        table_data.append([str(i), str(maxList[i]), str(minList[i]), str(averages[i])])
    table = ax.table(cellText=table_data, loc='center', cellLoc='center', colWidths=[0.1, 0.3, 0.3, 0.3])
    table.auto_set_font_size(False)
    fontsize = 10
    table.set_fontsize(fontsize)

    plt.savefig("output/tabla.png", dpi=300, bbox_inches='tight')