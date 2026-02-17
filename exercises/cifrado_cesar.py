def cifrado_cesar(texto, desplazamiento=3):
    resultado = ""
    base = 97
    texto = texto.lower()

    for letra in texto:
        if letra.isalpha():
            letra_nueva = (ord(letra) - base + desplazamiento) % 26 + base
            resultado += chr(letra_nueva)
        else:
            resultado += letra

    return resultado


def descifrado_cesar(texto, desplazamiento=3):
    resultado = ""
    base = 97
    texto = texto.lower()

    for letra in texto:
        if letra.isalpha():
            letra_nueva = (ord(letra) - base - desplazamiento) % 26 + base
            resultado += chr(letra_nueva)
        else:
            resultado += letra
    return resultado


palabra = "profe si funciona"
cifrada = cifrado_cesar(palabra)
print(cifrada)
print(descifrado_cesar(cifrada))
