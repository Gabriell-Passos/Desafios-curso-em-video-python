n1 = None
n2 = None
esc = None
while n1 == None:
    try:
        n1 = float(input("Digite um número: "))
    except ValueError:
        print("Isso não é um número, tente denovo!")
while n2 == None:
    try:
        n2 = int(input("Digite outro número: "))
    except ValueError:
        print("Isso não é um número, tente denovo!")
while esc == None:
    esc = int(input('''---------- Escolha uma opção ----------
[1] Soma
[2] Multiplicação
[3] Maior
[4] Novos números
[5] Sair do Programa
---------------------------------------
Opção desejada: '''))
if esc > 5 or esc <1:
    print("Opção inválida tente novamente!")
    esc = None
