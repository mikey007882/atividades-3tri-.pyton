vetor = [int(input(f"Digite o elemento {i+1} do vetor: ")) for i in range(5)]
media = sum(vetor) / len(vetor)
print("Média dos elementos do vetor:", media)