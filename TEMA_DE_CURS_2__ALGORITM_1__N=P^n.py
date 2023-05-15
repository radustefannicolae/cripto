import random

def generate_permutation(n):
    perm = list(range(n))
    random.shuffle(perm)
    return perm

def encrypt(message, permutation):
    encrypted_message = ""
    for i in range(len(message)):
        encrypted_message += message[permutation[i]]
    return encrypted_message

def decrypt(encrypted_message, permutation):
    decrypted_message = ""
    inverse_permutation = [0] * len(permutation)
    for i in range(len(permutation)):
        inverse_permutation[permutation[i]] = i
    for i in range(len(encrypted_message)):
        decrypted_message += encrypted_message[inverse_permutation[i]]
    return decrypted_message

# Exemplu de utilizare
message = "Buna, lume"
permutation = generate_permutation(len(message))
encrypted_message = encrypt(message, permutation)
decrypted_message = decrypt(encrypted_message, permutation)

print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)
