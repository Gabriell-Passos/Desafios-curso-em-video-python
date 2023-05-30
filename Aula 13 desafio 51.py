vi = int(input("Digite o valor inicial: "))
r = int(input("Digite a razão de progressão: "))
for c in range (1,r+1):
    vi += r
    print("Termo {} = {}".format(c, vi))

    # Tudo Certo!