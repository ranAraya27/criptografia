import numpy as np
from sympy import Matrix  # pip install sympy
import numpy as np


def inversa_modular(matriz, mod=26):
    M = Matrix(matriz)
    M_inv = M.inv_mod(mod)
    return np.array(M_inv).astype(int)


val_let = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25,
}


def cifrado_hill(mensaje="act", clave="gybnqkurp"):
    C = np.zeros((3, 3))
    M = np.zeros((3, 1))
    clave = clave.upper()
    mensaje = mensaje.upper()
    count = 0
    for i in range(3):
        for j in range(3):
            C[i][j] = val_let[clave[count]]
            count = count + 1

    count = 0
    for i in range(3):
        M[i] = val_let[mensaje[count]]
        count = count + 1

    A = C @ M
    for i in range(3):
        A[i] = A[i] % 26
    return A


def descifrado_hill(vector_cifrado, clave="gybnqkurp"):
    clave = clave.upper()
    matriz_clave = np.zeros((3, 3))
    count = 0
    for i in range(3):
        for j in range(3):
            matriz_clave[i][j] = val_let[clave[count]]
            count = count + 1
    print(matriz_clave)

    matriz_clave_inv = inversa_modular(matriz_clave, 26)

    vector_descifrado = matriz_clave_inv @ vector_cifrado

    palabra_descifrada = ""
    vec = np.rint(np.asarray(vector_descifrado)).astype(int).flatten()
    print(matriz_clave_inv, "\n")
    print(vector_cifrado)
    for x in vec:
        palabra_descifrada += chr((x % 26) + ord("A"))
    return palabra_descifrada


vector_cifrado = cifrado_hill()
print(vector_cifrado, "\n\n")
print(descifrado_hill(vector_cifrado))
