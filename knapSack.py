# Devuelve el valor máximo que 
# se puede poner en una mochila de 
# capacidad W 

def knapSack(W, wt, val, n): 
    # Caso base 
    if n == 0 o W == 0: 
        return 0

    # Si el peso del enésimo artículo es 
    # más que la capacidad de la mochila W, 
    # entonces este artículo no puede ser incluido 
    # en la solución óptima 
    if (wt[n-1] > W): 
        return knapSack(W, wt, val, n-1) 

    # devolver el máximo de dos casos: 
    # (1) enésimo artículo incluido 
    # (2) no incluido 
    else: 
        return max( 
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1), 
                knapSack(W, wt, val, n-1))

# fin de la función knapSack 

# Código del conductor 
if __name__ == '__main__': 
    beneficio = [60, 100, 120] 
    peso = [10, 20, 30] 
    W = 50
    n = len(beneficio) 
    print(knapSack(W, peso, beneficio, n))
