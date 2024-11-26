vetor = [int(input(f"Digite o elemento {i+1} do vetor: ")) for i in range(5)]
maior = vetor[0]

for num in vetor:
    if num > maior:
        maior = num

print("Maior elemento do vetor:", maior)