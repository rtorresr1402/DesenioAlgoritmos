def capturar_ladrones(arreglo, k):
    i_policias = [i for i, val in enumerate(arreglo) if val == 'p']
    i_ladrones = [i for i, val in enumerate(arreglo) if val == 'l']
    
    capturas = 0
    i_p = 0
    i_l = 0
    
    while i_p < len(i_policias) and i_l < len(i_ladrones):
        # Si la distancia entre policía y ladrón es menor o igual que k
        if abs(i_ladrones[i_l] - i_policias[i_p]) <= k:
            capturas += 1  # Realiza una captura
            i_p += 1  # Avanza al siguiente policía
            i_l += 1  # Avanza al siguiente ladrón
        elif i_ladrones[i_l] < i_policias[i_p]:
            i_l += 1  # Avanza al siguiente ladrón
        else:
            i_p += 1  # Avanza al siguiente policía
            
    return capturas

# Ejemplo de uso del algoritmo:
# "p" representa un policía y "l" representa un ladrón.
##ARREGLO DE 10 
##arreglo_ejemplo = ['p', 'p', 'p', 'p', 'p', 'p', 'l', 'p', 'l', 'p']
arreglo_ejemplo = ['p', 'l', 'p', 'l', 'l', 'p']
k_ejemplo = 3

# Llamada a la función con el arreglo y k de ejemplo
capturas = capturar_ladrones(arreglo_ejemplo, k_ejemplo)
print(capturas)