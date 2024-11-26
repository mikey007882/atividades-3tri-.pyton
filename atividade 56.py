def transpor_matriz(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def matriz_simetrica(matriz):
    return matriz == transpor_matriz(matriz)

matriz_exemplo = [
    [1, 2, 3],
    [2, 5, 6],
    [3, 6, 9]
]

print(matriz_simetrica(matriz_exemplo))  