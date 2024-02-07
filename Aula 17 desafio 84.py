nep = []
v = []
controle = 0
mapeso = 0
mepeso = 0
escolha = int(input("Quantos nomes você quer adicionar? "))
while True:
    if controle < escolha:
        v.append(input(f"Qual o nome da {controle + 1}° pessoa?  "))
        v.append(input(f"Qual o peso da {controle + 1}° pessoa? "))
        nep.append(v[:])
        if v[1] > nep[controle][1]:
            mapeso = v[1]
        else:
            mepeso = v[1]
        v = []
        controle +=1
    else:
        break
print(f"Foram cadastradas {len(nep)} pessoas")
print(f"O maior peso é {mapeso} e o menor peso é {mepeso}")