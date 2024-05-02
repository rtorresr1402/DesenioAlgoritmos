class BloqueDeMemoria:
    def __init__(self, id, capacidad):
        self.id = id
        self.capacidad = capacidad
        self.usado = False  # Atributo para rastrear si el bloque ha sido usado

class Proceso:
    def __init__(self, id, tamaño):
        self.id = id
        self.tamaño = tamaño

def primer_ajuste(bloques, proceso):
    # Buscar el primer bloque con capacidad suficiente para el proceso
    for bloque in bloques:
        if bloque.capacidad >= proceso.tamaño:
            bloque.usado = True  # Marcar el bloque como usado
            return bloque
    return None  # No se encontró ningún bloque adecuado

def asignar_memoria(bloques, procesos):
    tabla_de_asignacion = []
    procesos_no_asignados = []
    
    for proceso in procesos:
        bloque = primer_ajuste(bloques, proceso)
        if bloque:
            bloque_original = bloque.capacidad
            bloque.capacidad -= proceso.tamaño
            tabla_de_asignacion.append((proceso.id, bloque.id, proceso.tamaño, bloque_original, bloque.capacidad))
        else:
            procesos_no_asignados.append((proceso.id, proceso.tamaño))
    
    return tabla_de_asignacion, procesos_no_asignados

# Definir bloques de memoria con nuevas capacidades
bloques = [
    BloqueDeMemoria(1, 150),
    BloqueDeMemoria(2, 350),
    BloqueDeMemoria(3, 550),
    BloqueDeMemoria(4, 250),
    BloqueDeMemoria(5, 450)
]

# Definir procesos con nuevos tamaños requeridos
procesos = [
    Proceso(1, 140),
    Proceso(2, 200),
    Proceso(3, 300),
    Proceso(4, 360),
    Proceso(5, 100),
    Proceso(6, 50),
    Proceso(7, 420)
]

resultados_de_asignacion, procesos_no_asignados = asignar_memoria(bloques, procesos)

for resultado in resultados_de_asignacion:
    print(f"Proceso {resultado[0]} asignado al Bloque {resultado[1]} (Solicitó: {resultado[2]}Kb, Capacidad original: {resultado[3]}Kb, Espacio libre después: {resultado[4]}Kb)")

if procesos_no_asignados:
    for no_asignado in procesos_no_asignados:
        print(f"Proceso {no_asignado[0]} no pudo ser asignado (Necesitaba: {no_asignado[1]}Kb)")
else:
    print("Todos los procesos fueron asignados.")

print("\nEstado de los bloques después de las asignaciones:")
for bloque in bloques:
    if bloque.usado:
        print(f"Bloque {bloque.id}: {bloque.capacidad}Kb libre (Usado)")
    else:
        print(f"Bloque {bloque.id}: {bloque.capacidad}Kb libre (No Usado)")