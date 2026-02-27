import numpy as np
from sympy import Matrix  # pip install sympy
import numpy as np


def _crear_matriz_clave(clave):
    clave = clave.upper()
    matriz_clave = np.zeros((3, 3))
    count = 0
    for i in range(3):
        for j in range(3):
            matriz_clave[i][j] = ord(clave[count]) - ord("A")
            count = count + 1
    return matriz_clave


def _crear_vector_mensaje(mensaje):
    mensaje = mensaje.upper()
    vector_mensaje = np.zeros((3, 1))
    count = 0
    for i in range(3):
        vector_mensaje[i] = ord(mensaje[count]) - ord("A")
        count = count + 1
    return vector_mensaje


def _inversa_modular(matriz, mod=26):
    M = Matrix(matriz)
    M_inv = M.inv_mod(mod)
    return np.array(M_inv).astype(int)


def _str_a_vector(texto):
    texto = texto.upper()
    return np.array([ord(c) - ord("A") for c in texto], dtype=int).reshape(3, 1)


def _vector_a_str(vector):
    vec = np.asarray(vector).flatten()
    return "".join(chr(int(x) + ord("A")) for x in vec)


def cifrado_hill(mensaje="act", clave="gybnqkurp"):
    matriz_clave = _crear_matriz_clave(clave)
    vector_mensaje = _crear_vector_mensaje(mensaje)

    return _vector_a_str((matriz_clave @ vector_mensaje) % 26)


def descifrado_hill(mensaje_cifrado, clave="gybnqkurp"):
    vector_cifrado = _str_a_vector(mensaje_cifrado)
    matriz_clave_inv = _inversa_modular(_crear_matriz_clave(clave), 26)

    vector_descifrado = (matriz_clave_inv @ vector_cifrado) % 26

    return _vector_a_str(vector_descifrado)


mensaje = "act"
clave = "gybnqkurp"
print(f"El mensaje es: {mensaje}")
print(f"La clave es: {clave}\n")

mensaje_cifrado = cifrado_hill(mensaje, clave)
print(f"El mensaje cifrado es: {mensaje_cifrado}")
print(f"El mensaje descifrado es: {descifrado_hill(mensaje_cifrado)}")
