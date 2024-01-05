lista = []
listaimpar = []
listapar = []
numero = None
cont = 0
escolha2 = None
escolha = int(input("Quantos números você quer adicionar na lista? "))
while True:
    numero = int(input(f"Digite o {cont + 1}° número da lista: "))
    if numero in lista:
        print(f"\033[1;31;41mO número {numero} não foi adicionado pois o mesmo já está na lista\033[m")
    else:
        lista.append(numero)
        print(f"\033[1;32;42mO número {numero} foi adicionado com sucesso\033[m")
        cont += 1
    if cont == escolha:
        escolha2 = int(input("Você quer adicionar mais número na lista? (0 = NÃO / 1 = SIM): "))
        if escolha2 == 0:   
            break
        else:
            escolha += int(input("Quantos números a mais você quer adicionar? "))
print(f"Assim ficou sua lista {lista}")
for x in range(0,escolha):
    if (lista[x] % 2) > 0:
        listaimpar.append(lista[x])
    else:
        listapar.append(lista[x]) 
print(f"Os números impares presentes na sua lista são {listaimpar}")
print(f"Os números pares presentes na sua lista são {listapar}")