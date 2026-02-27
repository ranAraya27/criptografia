import numpy as np

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


def cifrado_hill(vector, clave="gybnqkurp"):
    C = np.zeros((3, 3))
    M = np.zeros((3, 1))
    clave = clave.upper()
    mensaje = mensaje.upper()
    count = 0
    for i in range(3):
        for j in range(3):
            C[i][j] = val_let[clave[count]]
            count = count + 1

    C_inv = np.linalg.inv(C)

    A = 
    for i in range(3):
        A[i] = A[i] % 26
    return A
