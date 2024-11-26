def multiplicar_matrizes(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        return "Multiplicação impossível"
    return [[sum(matriz1[i][k] * matriz2[k][j] for k in range(len(matriz2))) 
            for j in range(len(matriz2[0]))] 
            for i in range(len(matriz1))]
