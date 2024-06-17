import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def get_text_from_user():
    return input("Por favor, introduce el texto a procesar: ")

def calculate_frequencies(text):
    return Counter(text)

def build_huffman_tree(frequencies):
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(priority_queue)
    
    while len(priority_queue) > 1:
        node1 = heapq.heappop(priority_queue)
        node2 = heapq.heappop(priority_queue)
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(priority_queue, merged)
    
    return priority_queue[0]

def generate_huffman_codes(node, prefix="", codebook={}):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_huffman_codes(node.left, prefix + "0", codebook)
        generate_huffman_codes(node.right, prefix + "1", codebook)
    return codebook

def encode_text(text, huffman_codes):
    return ''.join(huffman_codes[char] for char in text)

def decode_text(encoded_text, huffman_tree):
    decoded_text = []
    node = huffman_tree
    for bit in encoded_text:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        
        if node.char is not None:
            decoded_text.append(node.char)
            node = huffman_tree
    
    return ''.join(decoded_text)

def save_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

# Obtener el texto del usuario
text = get_text_from_user()

# Calcular las frecuencias
frequencies = calculate_frequencies(text)

# Construir el árbol de Huffman
huffman_tree = build_huffman_tree(frequencies)

# Generar el código de Huffman
huffman_codes = generate_huffman_codes(huffman_tree)

# Codificar el texto
encoded_text = encode_text(text, huffman_codes)

# Guardar el texto original y codificado
save_to_file('original_text.txt', text)
save_to_file('encoded_text.txt', encoded_text)

# Decodificar el texto
decoded_text = decode_text(encoded_text, huffman_tree)

# Verificar y mostrar los resultados
print("Texto original:", text)
print("Texto codificado:", encoded_text)
print("Texto decodificado:", decoded_text)

# Guardar el texto decodificado
save_to_file('decoded_text.txt', decoded_text)
