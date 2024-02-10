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

#precisa da solução