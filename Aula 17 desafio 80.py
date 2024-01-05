q = 5
c = 0
x = None
lista = []
while True:
    x = int(input(f"Digite o {c + 1}° número da lista: "))
    if x in lista:
        print(f"\033[0;31;41mO número {x} já está na lista!\033[m")
    else:
        if len(lista) == 0:
           lista.append(x)
           print(f"\033[1;30;42mO número {x} foi adicionado no final da lista!\033[m")
        elif x > max(lista):
            lista.append(x)
            print(f"\033[1;30;42mO número {x} foi adicionado no final da lista!\033[m")
        elif x < min(lista):
            lista.insert(0,x)
            print(f"\033[1;30;42mO número {x} foi adicionado no inicio da lista!\033[m")
        for a in range(5):

        c += 1
    if c == q:
        break
print(lista)  

#não finalizado