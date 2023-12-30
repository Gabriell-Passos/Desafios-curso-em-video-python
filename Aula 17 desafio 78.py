lista = []
for x in range (1,6):
    e = lista.append(input(f"Digite o {x}° número da lista: "))
mn = max(lista)
mm = min(lista)
print(f"Na lista {lista} criada por você, o maior número é {mn} que está na posição {lista.index(mn) + 1} e o menor número é {mm} que está na posição {lista.index(mm) + 1}.")
lista.sort()
print(f"A lista com os números em ordem crescente fica {lista}")
