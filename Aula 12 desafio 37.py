numero = int(input("Insira um número: "))
escolha = int(input("Qual será a base de conversão? \n 1 - Binário \n 2 - Octal \n 3 - Hexadecimal \n Insira o número correspondente: "))
if escolha == 1:
    nb = bin(numero)[2:]
    print("O número {} em Binario é {}.".format(numero, nb))
elif escolha == 2:
    no = oct(numero)[2:]
    print("O número {} em Octal é {}".format(numero,no))
elif escolha == 3:
    nh = hex(numero)[2:]
    print("O número {} em Hexadecimal é {}".format(numero,nh))
elif escolha >3:
    print("Número invalido, por favor tente novamente!")

    # Tudo Certo!