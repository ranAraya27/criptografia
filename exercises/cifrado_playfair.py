def cifrado_playfair(mensaje, clave):
    # Paso 1:
    mensaje = mensaje.upper().replace("I", "J")
    clave = clave.upper().replace("I", "J")

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
    print(mensaje)
    limpio = "".join([c for c in mensaje if c.isalpha()])
    print(limpio)
    i = 0
    while i < len(limpio):
        a = limpio[i]
        b = limpio[i + 1] if i + 1 < len(limpio) else "X"

        if a == b:
            pares.append((a, "X"))
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
        print(fa, ca)
        break

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


cifrado_playfair("hello world", "silla")
