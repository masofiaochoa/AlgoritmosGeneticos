from capitalRoute import CapitalRoute
from functions.AG import targetFunction

#Funcion fitness lo tomamos como la funcion objetivo de la ruta especifica, dividido la sumatoria de todas las funciones objetivos de las demas rutas
def testFitness(capitalRoute: CapitalRoute, capitalRoutesTargetFunctionTotal: float) -> float:

    fitnessFunction: float = (capitalRoutesTargetFunctionTotal - targetFunction(capitalRoute)) / capitalRoutesTargetFunctionTotal

    return fitnessFunction