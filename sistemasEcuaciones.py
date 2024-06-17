import numpy as np

# Coeficientes del sistema de ecuaciones
A = np.array([
    [1, 2, 1, 3],
    [2, 0, 2, -1],
    [-1, 1, 1, 0],
    [3, 3, -2, 2]
])

# Constantes en el lado derecho
b = np.array([-8, 13, 8, -1])

# Función para calcular el residual (diferencia entre el lado izquierdo y el lado derecho)
def calcular_residual(x):
    return np.linalg.norm(np.dot(A, x) - b)

# Parámetros
max_iteraciones = 10_000_000
mejor_x = None
mejor_residual = float('inf')

# Búsqueda aleatoria
for i in range(max_iteraciones):
    # Generar valores enteros aleatorios para x, y, z, t entre -5 y 5
    solucion_aleatoria = np.random.randint(-5, 6, size=4)
    residual = calcular_residual(solucion_aleatoria)
    
    # Mensaje de depuración para cada iteración
    if i % 100000 == 0:
        print(f"Iteración {i}: Solución aleatoria: {solucion_aleatoria}, Residual: {residual}")
    
    # Actualizar la mejor solución encontrada hasta ahora
    if residual < mejor_residual:
        mejor_x = solucion_aleatoria
        mejor_residual = residual

        # Imprimir la mejor solución encontrada hasta ahora
        print(f"Iteración {i}: Mejor solución hasta ahora: {mejor_x} con residual: {mejor_residual}")

    # Si el residual es 0, hemos encontrado una solución exacta
    if mejor_residual == 0:
        break

# Imprimir la mejor solución final
if mejor_x is not None:
    print(f"Mejor solución final: {mejor_x} con residual: {mejor_residual}")
else:
    print("No se encontró ninguna solución.")
