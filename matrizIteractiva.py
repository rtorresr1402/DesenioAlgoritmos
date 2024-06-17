def caminos_unicos_con_obstaculos(matriz):
    filas, columnas = len(matriz), len(matriz[0])
    
    # Crear una matriz para almacenar el número de rutas posibles
    dp = [[0] * columnas for _ in range(filas)]
    
    # Inicializar la primera celda
    dp[0][0] = 1 - matriz[0][0]
    
    # Llenar la primera columna
    for i in range(1, filas):
        dp[i][0] = dp[i-1][0] * (1 - matriz[i][0])
    
    # Llenar la primera fila
    for j in range(1, columnas):
        dp[0][j] = dp[0][j-1] * (1 - matriz[0][j])
    
    # Calcular el número de rutas posibles para cada celda
    for i in range(1, filas):
        for j in range(1, columnas):
            if matriz[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    # Imprimir la matriz dp
    print("Matriz dp:")
    for fila in dp:
        print(fila)
    
    return dp[filas-1][columnas-1]

# Ejemplo de uso
matriz = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print("Número de rutas posibles:", caminos_unicos_con_obstaculos(matriz))  # Salida: 2
