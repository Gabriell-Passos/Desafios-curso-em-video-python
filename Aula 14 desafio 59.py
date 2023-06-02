n1 = None
n2 = None
esc = None
cont = 0
while n1 == None:
    try:
        n1 = float(input("Digite um número: "))
    except ValueError:
        print("Isso não é um número, tente denovo!")
while n2 == None:
    try:
        n2 = float(input("Digite outro número: "))
    except ValueError:
        print("Isso não é um número, tente denovo!")
while cont == 0:
    try:
        esc = int(input('''---------- Escolha uma opção ----------
[1] Soma
[2] Multiplicação
[3] Maior
[4] Novos números
[5] Sair do Programa
---------------------------------------
Opção desejada: '''))
    except ValueError:
        print("Opção inválida tente novamente!")
    if esc > 5 or esc < 1:
        print("Opção inválida tente novamente!")
    if esc == 1:
        print("A soma de {} com {} é igual a {}.".format(n1,n2,n1+n2))
    elif esc == 2:
        print("A multiplicação de {} com {} é igual a {}.".format(n1,n2,n1*n2))
    if esc == 3:
        if n1 > n2:
            print("{} é maior que {}.".format(n1,n2))
        elif n1 == n2:
            print("Os números possuem o mesmo valor.")
        elif n2 > n1:
            print("{} é maior que {}.".format(n2,n1))
    if esc == 4:
        n1 = float(input("Digite o novo valor do primeiro número: "))
        if n1 == ValueError:
            print("Isso não é um número, tente denovo!")
        
        n2 = float(input("Digite o novo valor do segundo número: "))
        if n2 == ValueError:
            print("Isso não é um número, tente denovo!")
    if esc == 5:
        print("Você escolheu sair.")
        cont = 1