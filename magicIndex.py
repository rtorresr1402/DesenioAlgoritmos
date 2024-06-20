import random

# Generar un arreglo aleatorio de tamaño n con valores no necesariamente distintos
def generar_arreglo_aleatorio(n, rango_min, rango_max):
    return [random.randint(rango_min, rango_max) for _ in range(n)]

# Encontrar índices mágicos en un arreglo con valores no necesariamente distintos
def encontrar_indices_magicos_no_distintos(arr):
    def busqueda_binaria(arr, izquierda, derecha, indices_magicos):
        if izquierda > derecha:
            return
        
        medio = (izquierda + derecha) // 2
        valor_medio = arr[medio]
        
        if valor_medio == medio:
            indices_magicos.append(medio)
        
        # Buscar a la izquierda
        indice_izquierda = min(medio - 1, valor_medio)
        busqueda_binaria(arr, izquierda, indice_izquierda, indices_magicos)
        
        # Buscar a la derecha
        indice_derecha = max(medio + 1, valor_medio)
        busqueda_binaria(arr, indice_derecha, derecha, indices_magicos)
    
    indices_magicos = []
    busqueda_binaria(arr, 0, len(arr) - 1, indices_magicos)
    return indices_magicos

# Generar un arreglo aleatorio
tamaño_arreglo = 20
rango_min = -10
rango_max = 20
arreglo_aleatorio = generar_arreglo_aleatorio(tamaño_arreglo, rango_min, rango_max)

# Encontrar los índices mágicos
indices_magicos = encontrar_indices_magicos_no_distintos(arreglo_aleatorio)

# Mostrar el arreglo y los índices mágicos encontrados
print(f"Arreglo: {arreglo_aleatorio}")
print(f"Índices mágicos encontrados: {indices_magicos}")

import random

# Generar un arreglo aleatorio de tamaño n con valores no necesariamente distintos
def generar_arreglo_aleatorio(n, rango_min, rango_max):
    return [random.randint(rango_min, rango_max) for _ in range(n)]

# Encontrar índices mágicos en un arreglo con valores no necesariamente distintos
def encontrar_indices_magicos_no_distintos(arr):
    def busqueda_binaria(arr, izquierda, derecha, indices_magicos):
        if izquierda > derecha:
            return
        
        medio = (izquierda + derecha) // 2
        valor_medio = arr[medio]
        
        if valor_medio == medio:
            indices_magicos.append(medio)
        
        # Buscar a la izquierda
        indice_izquierda = min(medio - 1, valor_medio)
        busqueda_binaria(arr, izquierda, indice_izquierda, indices_magicos)
        
        # Buscar a la derecha
        indice_derecha = max(medio + 1, valor_medio)
        busqueda_binaria(arr, indice_derecha, derecha, indices_magicos)
    
    indices_magicos = []
    busqueda_binaria(arr, 0, len(arr) - 1, indices_magicos)
    return indices_magicos

# Generar un arreglo aleatorio
tamaño_arreglo = 20
rango_min = -10
rango_max = 20
arreglo_aleatorio = generar_arreglo_aleatorio(tamaño_arreglo, rango_min, rango_max)

# Encontrar los índices mágicos
indices_magicos = encontrar_indices_magicos_no_distintos(arreglo_aleatorio)

# Mostrar el arreglo y los índices mágicos encontrados
print(f"Arreglo: {arreglo_aleatorio}")
print(f"Índices mágicos encontrados: {indices_magicos}")

