vetor = [int(input(f"Digite o elemento {i+1} do vetor: ")) for i in range(5)]
ordenado = True

for i in range(len(vetor) - 1):
    if vetor[i] > vetor[i + 1]:
        ordenado = False
        break

if ordenado:
    print("O vetor está ordenado em ordem crescente.")
else:
    print("O vetor não está ordenado.")