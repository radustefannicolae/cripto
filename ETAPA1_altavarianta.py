import string
import unicodedata
from collections import Counter

# definim alfabetul limbii romane, inclusiv diacriticele
alphabet = string.ascii_lowercase + "ăîâșțĂÎÂȘȚ"
characters = []
specialCharList=['`','~','!','@','#','$','%','^',
             '&','*','(',')','-','_','+','=',
             '|','','{','}','[',']',';',':',
             '"',',','.','<','>','/','?']
# deschidem fisierul text si citim continutul cu codificarea utf-8
with open("text2.txt", "r", encoding="utf-8") as f:
    text = f.read()

# initializam un dictionar gol pentru a contoriza numarul de aparitii al fiecarui caracter
char_counts = {char: 0 for char in alphabet}

# parcurgem fiecare caracter din text si contorizam aparitiile
text = unicodedata.normalize("NFKD", text).lower()
for char in text:
    if unicodedata.category(char)[0] == "M":
        # character is a composing mark, so agregate it with
        # previous character
        characters[-1] += char
    else:
        characters.append(char)

counting = Counter(characters)

# sortam dictionarul counting alfabetic, inclusiv cu diacriticele
counting_sorted = dict(sorted(counting.items(), key=lambda x: x[0]))

# excludem simbolurile din dictionarul counting_sorted
print(counting_sorted.items())
counting_sorted = {char: count for char, count in counting_sorted.items() if char not in alphabet or char not in specialCharList}
print(counting_sorted.items())
# afisam dictionarul counting_sorted
for char, count in counting_sorted.items():
    print(char, count)
