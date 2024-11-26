def contar_vogais(s):
    vogais = "aeiouAEIOU"
    return sum(1 for char in s if char in vogais)