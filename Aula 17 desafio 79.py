e = int(input("Quantos números diferentes você quer adicionar na lista? "))
lista = []
clista = None
cont = 0
p = None
while True:
    clista = (int(input(f"Digite o {cont + 1}° número para adicionar na lista: ")))
    if clista in lista:
        print(f"\033[1;31;40mO número {clista} não foi adicionado pois o mesmo já está na lista.\033[0m")
    else:
        lista.append(clista)
        print(f"\033[1;32;40mO número {clista} foi adicionado com sucesso.\033[0m")
        cont += 1
    if cont == e:
        p = int(input(f"\033[1;33;40mSua lista possui {cont} números, você deseja adicionar mais números na lista? (1 = Sim / 0 = Não):\033[m "))
        if p == 1:
            e += int(input("Quantos números a mais você quer adicionar: "))
        else:
            break
lista.sort()
print(f"Sua lista de {e} números organizada em ordem crescente fica {lista}")