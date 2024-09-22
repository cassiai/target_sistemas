palavra = str(input("Digite uma palavra: ").upper())

contador = 0
for i in range(len(palavra)):
    if(palavra[i] == "A"):
        contador += 1

print(f"A letra A ou a apareceu {contador} vezes")