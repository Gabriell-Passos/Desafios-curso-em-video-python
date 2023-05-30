iniciar = input("Insira qualquer coisa para iniciar o programa: ")
s = 0
for c in range(1,7):
    n = int(input("Insira o {} número inteiro: ".format(c)))
    if n % 2 == 0:
        s = n + s
print("A soma dos números pares, excluindo os impares é {}".format(s))

    # Tudo Certo!