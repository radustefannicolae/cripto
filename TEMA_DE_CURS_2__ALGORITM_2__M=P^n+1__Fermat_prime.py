import random

def generate_permutation(n):
    perm = list(range(n))
    random.shuffle(perm)
    return perm

def encrypt(message, permutation):
    encrypted_message = ""
    print(f"message={message}\nrange(len(message))={range(len(message))}")
    for i in range(len(permutation)):
        encrypted_message += message[permutation[i]]
        print(f"i={i}\nencrypted_message={encrypted_message}\n message[permutation[i]]={ message[permutation[i]]}\n permutation[i]={ permutation[i]}")
    return encrypted_message

def decrypt(encrypted_message, permutation):
    decrypted_message = ""
    inverse_permutation = [0] * len(permutation)
    for i in range(len(permutation)):
        inverse_permutation[permutation[i]] = i
    for i in range(len(encrypted_message)):
        decrypted_message += encrypted_message[inverse_permutation[i]]
    return decrypted_message

# Determinarea unui număr prim Fermat
def is_fermat_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if pow(2, pow(2, n) - 1, pow(2, n)) == 1:
        return True
    return False

def generate_fermat_prime():
    n = 0
    while True:
        n += 1
        if is_fermat_prime(n):
            return n

# Exemplu de utilizare
message = "Hello, world!"
message1 = "Linia c) elementele de camp asociate valorilor numerice de la linia b) IN FORMA POLINOMIALA REDUSA Forma vectorialaLinia d) elementele de camp asociate valorilor numerice de la linia b) IN FORMA EXPONENTIALA {Se pune doar exponentul} Poate fi adaugat un gbis care sa aiba reprezentarea exponentiala al lui g Linia h) reprezinta Fxi valorile numerice obtinute in urma calculelor functiei polinomiale de permutare (yi). Obtinem eleme"
fermat_prime = generate_fermat_prime()
print(f"fermat_prime = {fermat_prime}")
permutation = generate_permutation(len(message))  # Aici am modificat pentru a avea lungimea corectă a permutării
print(f"permutation = {permutation}")
encrypted_message = encrypt(message, permutation)
decrypted_message = decrypt(encrypted_message, permutation)

print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)
