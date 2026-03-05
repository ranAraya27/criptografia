import random


def cifrado_vernam(mensaje, clave):
    m = mensaje.encode("utf-8")
    c = clave.encode("utf-8")

    resultado = []
    for i in range(len(m)):
        xor = m[i] ^ c[i]
        resultado.append(xor)
    return bytes(resultado)


def descifrado_vernam(cifrado, clave):
    c = clave.encode("utf-8")
    resultado = []
    for i in range(len(cifrado)):
        xor = cifrado[i] ^ c[i]
        resultado.append(xor)
    return bytes(resultado).decode("utf-8")


def generar_clave(mensaje):
    resultado = []
    for i in range(len(mensaje)):
        resultado.append(random.randint(65, 90))
    return "".join([chr(c) for c in resultado])


mensaje = "HOLA"
clave = generar_clave(mensaje)


cifrado = cifrado_vernam(mensaje, clave)
resultado = descifrado_vernam(cifrado, clave)
print(f"La clave aleatoria es: {clave}")
print(f"La palabra cifrada es {cifrado}")
print(f"La palabra descifrada es {resultado}")
