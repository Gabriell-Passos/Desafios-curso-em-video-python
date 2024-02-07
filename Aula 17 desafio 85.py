numeros = [[],[]]
escolha = int(input("Digite a quantidade de valores que você quer adicionar a lista: "))
for cont in range(0,escolha):
    valor = int(input(f"Digite o {cont+1}° número da lista: "))
    if valor % 2 != 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
pares = sorted(numeros[0])
impares = sorted(numeros[1])
print(f"{pares} são os números pares, {impares} são os números impares.")