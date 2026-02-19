def funcion_generadora(texto, clave):
    clave_generada = ""
    for i in range(len(texto)):
        clave_generada += clave[i % len(clave)]
    return clave_generada


def cifrado_vigenere(texto, clave):

    clave = funcion_generadora(texto, clave)
    resultado = ""
    base = 97
    texto = texto.lower()

    for i in range(len(texto)):
        if texto[i].isalpha():
            letra_nueva = (ord(texto[i]) - base + (ord(clave[i]) - base)) % 26 + base
            resultado += chr(letra_nueva)
        else:
            resultado += texto[i]

    return resultado


def descifrado_vigenere(texto, clave):

    clave = funcion_generadora(texto, clave)
    resultado = ""
    base = 97
    texto = texto.lower()

    for i in range(len(texto)):
        if texto[i].isalpha():
            letra_nueva = (ord(texto[i]) - base - (ord(clave[i]) - base)) % 26 + base
            resultado += chr(letra_nueva)
        else:
            resultado += texto[i]

    return resultado


palabra = "abcdef"
clave = "bcd"
cifrada = cifrado_vigenere(palabra, clave)
print(cifrada)
print(descifrado_vigenere(cifrada, clave))
