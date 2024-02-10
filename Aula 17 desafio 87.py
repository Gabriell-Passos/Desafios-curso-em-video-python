matrix=[]
linha1 = []
linha2= []
linha3= []
controle = 0
posisão = -1
pocisão = -1
for posição in range(0,7):
    if controle < 3:
        linha1.append(int(input(f"Digite o número da posição [0][{posição}]: ")))
        controle += 1
    if controle >= 3 and controle <= 5:
        posisão += 1
        linha2.append(int(input(f"Digite o número da posição [1],[{posisão}]: ")))
        controle += 1
    if controle > 5:
        pocisão += 1
        linha3.append(int(input(f"Digite o número da posição [2],[{pocisão}]: ")))
        controle += 1
print(linha1)
print(linha2)
print(linha3)
slinha3 = linha3[0] + linha3[1] + linha3[2]
slinha2 = linha2[0] + linha2[1] + linha2[2]
slinha1 = linha1[0] + linha1[1] + linha1[2]
slinhas = slinha3 + slinha2 + slinha1
print(f"A soma de todos os números é igual a {slinhas}")
print(f"a soma dos itens da linha 3 é igual a {slinha3}")
print(f"O maior número da linha 2 é {max(linha2)}")

#precisa da solução