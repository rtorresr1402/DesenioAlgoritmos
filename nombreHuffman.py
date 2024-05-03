import heapq

class Nodo:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        # Primero comparamos por frecuencia
        if self.freq != other.freq:
            return self.freq < other.freq
        # Si las frecuencias son iguales, comparamos por char, pero solo si ambos chars no son None
        if self.char is not None and other.char is not None:
            return self.char < other.char
        # Si uno de los chars es None, damos prioridad a los que no son None (hojas)
        return self.char is not None

def calcular_frecuencias(nombre):
    frecuencias = {}
    for char in nombre:
        if char in frecuencias:
            frecuencias[char] += 1
        else:
            frecuencias[char] = 1
    return frecuencias

def construir_arbol(frecuencias):
    heap = []
    for char, freq in frecuencias.items():
        heapq.heappush(heap, Nodo(char, freq))
    
    while len(heap) > 1:
        nodo1 = heapq.heappop(heap)
        nodo2 = heapq.heappop(heap)
        
        merged = Nodo(None, nodo1.freq + nodo2.freq)
        merged.left = nodo1
        merged.right = nodo2
        
        heapq.heappush(heap, merged)
    
    return heap[0]

def generar_codigos(raiz, path="", codigo={}):
    if raiz is not None:
        if raiz.char is not None:
            codigo[raiz.char] = path
        generar_codigos(raiz.left, path + "0", codigo)
        generar_codigos(raiz.right, path + "1", codigo)
    return codigo

def imprimir_arbol(nodo, prefix=""):
    """Función recursiva para imprimir el árbol con las conexiones visuales."""
    if nodo is not None:
        if nodo.char is not None:
            print(f"{prefix}('{nodo.char}': {nodo.freq})")
        else:
            print(f"{prefix}({nodo.freq})")
        if nodo.left is not None or nodo.right is not None:
            if nodo.left:
                next_prefix = prefix + "|-- "
                imprimir_arbol(nodo.left, next_prefix)
            if nodo.right:
                next_prefix = prefix + "|-- "
                imprimir_arbol(nodo.right, next_prefix)

def main(nombre):
    frecuencias = calcular_frecuencias(nombre)
    print("Frecuencias de cada carácter:")
    for char, freq in sorted(frecuencias.items()):
        print(f"'{char}': {freq}")
    
    raiz = construir_arbol(frecuencias)
    codigos = generar_codigos(raiz)
    sorted_codigos = sorted(codigos.items(), key=lambda item: (len(item[1]), item[0]))
    
    print("\nÁrbol de Huffman:")
    imprimir_arbol(raiz)
    
    print("\nCódigos Huffman ordenados por longitud de código:")
    for char, codigo in sorted_codigos:
        print(f"'{char}': {codigo} (longitud: {len(codigo)})")
    return sorted_codigos

nombre = "ricardo torres reymundo"
codigos_huffman = main(nombre)
