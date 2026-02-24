def cifrado_playfair_paso1(clave):
    alfabeto = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    matriz = [
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
    ]
    letras_matriz = ""
    for c in clave + alfabeto:
        if c not in letras_matriz:
            letras_matriz += c
    k = 0
    for i in range(5):
        for j in range(5):
            matriz[i][j] = letras_matriz[k]
            k += 1

    return matriz


def cifrado_playfair_paso2(mensaje):
    pares = []
    limpio = "".join([c for c in mensaje if c.isalpha()])
    i = 0
    while i < len(limpio):
        a = limpio[i]
        b = limpio[i + 1] if i + 1 < len(limpio) else "X"

        if a == b:
            pares.append((a, "X"))
        else:
            pares.append((a, b))
        i += 2

    return pares


def pos(letra, matriz):
    for i in range(5):
        for j in range(5):
            if matriz[i][j] == letra:
                return i, j


def playfair_forma_general(pares, matriz, modo="cifrar"):
    texto = ""
    operador = 1 if modo == "cifrar" else -1
    for par in pares:
        a = par[0]
        b = par[1]

        fa, ca = pos(a, matriz)
        fb, cb = pos(b, matriz)

        # Caso 1 distinta fila y columna
        if fa != fb and ca != cb:
            texto += matriz[fa][cb]
            texto += matriz[fb][ca]
        # Caso 2 misma fila
        elif fa == fb:
            texto += matriz[fa][(ca + operador) % 5]
            texto += matriz[fb][(cb + operador) % 5]
        # Caso 3 misma columna
        elif ca == cb:
            texto += matriz[(fa + operador) % 5][ca]
            texto += matriz[(fb + operador) % 5][cb]

    return texto


def cifrado_playfair(mensaje, clave):
    mensaje = mensaje.upper().replace("J", "I")
    clave = clave.upper().replace("J", "I")

    # Paso 1: Crear matriz
    matriz = cifrado_playfair_paso1(clave)

    # Paso 2: Separar en pares
    pares = cifrado_playfair_paso2(mensaje)

    # Paso 3: Cifrar
    return playfair_forma_general(pares, matriz, "cifrar")


def descifrado_playfair(mensaje, clave):
    mensaje = mensaje.upper().replace("J", "I")
    clave = clave.upper().replace("J", "I")

    # Paso 1: Crear matriz
    matriz = cifrado_playfair_paso1(clave)

    # Paso 2: Separar en pares
    pares = cifrado_playfair_paso2(mensaje)

    # Paso 3: Descifrar
    palabra_descifrada = list(playfair_forma_general(pares, matriz, "descifrar"))
    for i in range(len(palabra_descifrada)):
        if palabra_descifrada[i] == "X" and i % 2 == 1:
            palabra_descifrada[i] = palabra_descifrada[i - 1]

    return "".join(palabra_descifrada)


clave = "silla"
palabra = "hello world"

palabra_cifrada = cifrado_playfair(palabra, clave)
palabra_descifrada = descifrado_playfair(palabra_cifrada, clave)

print(palabra)
print(palabra_cifrada)
print(palabra_descifrada)
