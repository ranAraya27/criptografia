def inverso_multiplicativo(a, m, n):
    count = 0
    nums = []
    i = 0
    while(count < n):
        if (a * i) % m == 1:
            count += 1
            nums.append(i)
        i += 1
    return nums
    
    
                                    #Numero A, Modulo M, numero de resultados deseados
nums = inverso_multiplicativo(int(input("Ingrese el numero A: ")), int(input("Ingrese el modulo M: ")), int(input("Ingrese el numero de resultados deseados: ")))
print(f"Nums: {nums}")

