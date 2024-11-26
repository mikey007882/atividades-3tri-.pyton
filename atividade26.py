vetor = [int(input(f"Digite o elemento {i+1} do vetor: ")) for i in range(5)]
pares = sum(1 for num in vetor if num % 2 == 0)
print("Quantidade de elementos pares no vetor:", pares)