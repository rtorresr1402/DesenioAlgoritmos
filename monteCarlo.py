import random

def estimar_pi(num_muestras):
    puntos_dentro_del_circulo = 0
    
    for _ in range(num_muestras):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            puntos_dentro_del_circulo += 1

    # π es aproximadamente 4 veces la proporción de puntos dentro del círculo al total de puntos
    return 4 * puntos_dentro_del_circulo / num_muestras

# Ejemplo de uso con 10 millones de puntos para una mejor aproximación
num_muestras = 10_000_000
aproximacion_pi = estimar_pi(num_muestras)

if aproximacion_pi > 0:
    print(f"Aproximación de Pi: {aproximacion_pi}")
else:
    print("No se encontró una aproximación adecuada de Pi.")
