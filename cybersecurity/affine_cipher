alphabet = "abcdefghijklmnopqrstuvwxyz"
plaintext = "hello"

def encrypt(x, a, c):
    return (a*x + c) % (len(alphabet))

def encrypt_text(text):
    array = []
    for chr in text:
        index = encrypt(alphabet.index(chr), 5, 2)
        newchar = alphabet[index]
        array.append(newchar)

    return "".join(array)

print(encrypt_text(plaintext))

def find_inverse(a):
    for i in range(1, len(alphabet)):
        if (i * a) % len(alphabet) == 1: return i
        
    return -1