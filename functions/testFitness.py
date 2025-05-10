def testFitness(chromosome: int) -> float:
    """ Esta es la funcion fitness del ej, el tema es que si los 4 individuos toman valor 31(Valor maximo) el fitness retorna 0.25 y termina haciendo un bardo barbaro
    total: int = 0;
    for i in POPULATION:
        total += i.chromosome ** 2;
    
    if(total == 0.0):
        return 0.0
    else:
        return ( individual.chromosome ** 2 ) / total;
    """

    return (chromosome**2 / 31 ** 2);