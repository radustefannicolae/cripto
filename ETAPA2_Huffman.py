import heapq
from collections import defaultdict
import string
import unicodedata
from collections import Counter
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

with open("text2.txt", "r", encoding="utf-8") as f:
    text = f.read()

# normalizam textul
text = unicodedata.normalize("NFKD", text).lower()

# construim dictionarul cu frecventa aparitiilor fiecarui caracter
char_counts = defaultdict(int)
for char in text:
    char_counts[char] += 1

# construim dictionarul cu codurile Huffman pentru fiecare caracter
huffman_dict = huffman_code(char_counts)

# afisam lista cuvintelor de cod
for char, code in sorted(huffman_dict.items()):
    print(f"{char}: {code}")

# această funcție primește textul de codificat și dicționarul de codificare (codul Huffmann obținut în etapa 2) și returnează textul codificat.
def encode_text(text, huffman_dict):
    encoded_text = ""
    for char in text:
        encoded_text += huffman_dict[char]
    return encoded_text

print(f"Textul codificat:\n{encode_text(text,huffman_dict)}")