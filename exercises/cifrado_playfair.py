def cifrado_playfair(mensaje, clave):
    # Paso 1:
    mensaje = mensaje.upper().replace("J", "I")
    clave = clave.upper().replace("J", "I")

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

    # Paso 2
    pares = []
    limpio = "".join([c for c in mensaje if c.isalpha()])
    i = 0
    while i < len(limpio):
        a = limpio[i]
        b = limpio[i + 1] if i + 1 < len(limpio) else "X"

        if a == b:
            pares.append((a, "X"))
            i += 1
        else:
            pares.append((a, b))
            i += 2

    def pos(letra):
        for i in range(5):
            for j in range(5):
                if matriz[i][j] == letra:
                    return i, j

    # Cifrado
    cifrado = ""
    for par in pares:
        a = par[0]
        b = par[1]

        fa, ca = pos(a)
        fb, cb = pos(b)

        # Caso 1 distinta fila y columna
        if fa != fb and ca != cb:
            cifrado += matriz[fa][cb]
            cifrado += matriz[fb][ca]
        # Caso 2 misma fila
        elif fa == fb:
            cifrado += matriz[fa][(ca + 1) % 5]
            cifrado += matriz[fb][(cb + 1) % 5]
        # Caso 3 misma columna
        elif ca == cb:
            cifrado += matriz[(fa + 1) % 5][ca]
            cifrado += matriz[(fb + 1) % 5][cb]

    print(cifrado)
    return cifrado


def descifrado_playfair(mensaje, clave):
    # Paso 1:
    mensaje = mensaje.upper().replace("J", "I")
    clave = clave.upper().replace("J", "I")

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

    # Paso 2
    pares = []
    limpio = "".join([c for c in mensaje if c.isalpha()])
    i = 0
    while i < len(limpio):
        a = limpio[i]
        b = limpio[i + 1] if i + 1 < len(limpio) else "X"

        if a == b:
            pares.append((a, "X"))
            i += 1
        else:
            pares.append((a, b))
            i += 2

    def pos(letra):
        for i in range(5):
            for j in range(5):
                if matriz[i][j] == letra:
                    return i, j

    # Cifrado
    descifrado = ""
    for par in pares:
        a = par[0]
        b = par[1]

        fa, ca = pos(a)
        fb, cb = pos(b)

        # Caso 1 distinta fila y columna
        if fa != fb and ca != cb:
            descifrado += matriz[fa][cb]
            descifrado += matriz[fb][ca]
        # Caso 2 misma fila
        elif fa == fb:
            descifrado += matriz[fa][(ca - 1) % 5]
            cifrado += matriz[fb][(cb - 1) % 5]
        # Caso 3 misma columna
        elif ca == cb:
            descifrado += matriz[(fa - 1) % 5][ca]
            descifrado += matriz[(fb - 1) % 5][cb]

    print(descifrado.replace("X", ""))
    return descifrado.replace("X", "")


clave = "silla"
cifrado = cifrado_playfair("hello world", clave)
descifrado_playfair(cifrado, clave)
