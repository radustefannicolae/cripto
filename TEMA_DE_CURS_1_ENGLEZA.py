import heapq
from collections import defaultdict
import string
import unicodedata
from collections import Counter
import math

def build_huffman_tree(freq):
    heap = [[wt, [sym, ""]] for sym, wt in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

def huffman_code(text):
    freq = defaultdict(int)
    for sym in text:
        freq[sym] += 1
    huff = build_huffman_tree(freq)
    return {sym: code for sym, code in huff}

def calculate_entropy(freq):
    total_count = sum(freq.values())
    entropy = 0.0
    for count in freq.values():
        probability = count / total_count
        entropy += probability * math.log2(probability)
    return -entropy

def calculate_average_code_length(huffman_dict, freq):
    total_count = sum(freq.values())
    total_length = 0
    for sym, code in huffman_dict.items():
        total_length += len(code) * (freq[sym] / total_count)
    return total_length

def calculate_capacity(huffman_dict):
    return math.log2(len(huffman_dict))

def calculate_efficiency(entropy, average_code_length):
    return entropy / average_code_length

def calculate_redundancy(entropy, capacity):
    return 1 - (entropy / capacity)

def verify_coding_theorem(text, encoded_text, huffman_dict):
    decoded_text = ""
    current_code = ""
    for bit in encoded_text:
        current_code += bit
        for sym, code in huffman_dict.items():
            if current_code == code:
                decoded_text += sym
                current_code = ""
                break
    return text == decoded_text

def encode_text(text, huffman_dict):
    encoded_text = ""
    for char in text:
        if char in huffman_dict:
            encoded_text += huffman_dict[char]
    return encoded_text

with open("text2.txt", "r", encoding="utf-8") as f:
    text = f.read()

# normalize the text
text = unicodedata.normalize("NFKD", text).lower()

# build the character frequency dictionary
char_counts = defaultdict(int)
for char in text:
    char_counts[char] += 1

# build the Huffman code dictionary
huffman_dict = huffman_code(char_counts)

# print the code words list
for char, code in sorted(huffman_dict.items()):
    print(f"{char}: {code}")

# calculate the entropy of the information source
entropy = calculate_entropy(char_counts)
print(f"Entropia sursei informationale: {entropy}")

# calculate the average code length
average_code_length = calculate_average_code_length(huffman_dict, char_counts)
print(f"Lungimea medie a codului: {average_code_length}")

# calculate the capacity of the code
capacity = calculate_capacity(huffman_dict)
print(f"Capacitatea codului: {capacity}")

# calculate the efficiency of the code
efficiency = calculate_efficiency(entropy, average_code_length)
print(f"Eficienta codului: {efficiency}")

# calculate the non-uniform redundancy
redundancy = calculate_redundancy(entropy, capacity)
print(f"Redundanta neuniforma: {redundancy}")

# verify the coding theorem
coding_theorem_verified = verify_coding_theorem(text, encode_text(text, huffman_dict), huffman_dict)
print(f"Teorema fundamentala a codificarii verificata: {coding_theorem_verified}")

# encode an example text
text_to_encode = "Acesta este un exemplu de text de codificat."
encoded_text = encode_text(text_to_encode, huffman_dict)
print(f"Textul codificat: {encoded_text}")
