n = input(str("Digite o nome da sua cidade: "))
nn = n.split()
n2 = nn[0]
nv = 'Santo' in n2
print("A cidade {} começa com Santo? {}".format(n, nv))

# agora usando o if

n = input(str("Digite o nome da sua cidade: ")).split()
np = n[0]
np2 = 'Santo' in np
if np2:
    print("Parabéns, Santos é o primeiro nome da sua cidade!")
else:
    print("Santos não é o primeiro nome da sua cidade")

        # Tudo Certo!