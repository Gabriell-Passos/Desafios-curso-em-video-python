pessoas = [[], []]
inf = [[], []]
v = int(input("Quantas pessoas serão adicionadas na lista: "))
c = 0
while True:
    if v != c:
        inf[0].append(str(input(f"Digite o nome da {c+1}° pessoa: ")))
        inf[1].append(int(input(f"Digite o peso da {c+1}° pessoa: ")))
        pessoas[c].append(inf)
        c += 1
    else:
        break
print(pessoas)