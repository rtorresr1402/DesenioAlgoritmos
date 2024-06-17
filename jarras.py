def resolver_problema_jarras():
    capacidad_jarra_5 = 5
    capacidad_jarra_3 = 3
    objetivo = 4
    
    jarra_5 = 0
    jarra_3 = 0
    
    pasos = []

    # Paso 1: Llenar la jarra de 5 litros
    jarra_5 = capacidad_jarra_5
    pasos.append((jarra_5, jarra_3))
    
    # Paso 2: Verter agua de la jarra de 5 litros a la de 3 litros
    while jarra_5 != objetivo and jarra_3 != objetivo:
        verter = min(jarra_5, capacidad_jarra_3 - jarra_3)
        jarra_3 += verter
        jarra_5 -= verter
        pasos.append((jarra_5, jarra_3))

        # Comprobar si hemos alcanzado el objetivo
        if jarra_5 == objetivo or jarra_3 == objetivo:
            break

        # Si la jarra de 3 litros está llena, vaciarla
        if jarra_3 == capacidad_jarra_3:
            jarra_3 = 0
            pasos.append((jarra_5, jarra_3))
        
        # Si la jarra de 5 litros está vacía, llenarla
        if jarra_5 == 0:
            jarra_5 = capacidad_jarra_5
            pasos.append((jarra_5, jarra_3))
    
    return pasos

pasos = resolver_problema_jarras()
for paso in pasos:
    print(f"Jarra de 5 litros: {paso[0]} litros, Jarra de 3 litros: {paso[1]} litros")

