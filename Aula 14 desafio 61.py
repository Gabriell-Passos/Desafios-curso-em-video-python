numero = int(input("Digite um número: "))
ra = int(input("Digite a razão da progressão aritmética:"))
cont = 1

while cont < 11:
    numero += ra
    print("{} termo da preogressão aritmética é igual {}".format(cont,numero))
    cont += 1
