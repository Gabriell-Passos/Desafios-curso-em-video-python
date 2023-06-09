numero = int(input("Digite um número: "))
ra = int(input("Digite a razão da progressão aritmética:"))
cont = int(1)

while cont < 11:
    numero += ra
    print("{} termo da preogressão aritmética é igual {}".format(cont,numero))
    cont += 1

esco = input("Você deseja ver mais termos? [S/N]").upper()

if esco == "S":
    quant = int(input("Quantos termos você deseja ver?"))
    for q in range (cont - 1, (cont + quant-1)):
        numero += ra
        print("{} termo da preogressão aritmética é igual {}".format((cont+q)-10,numero))
else:
    print("Tudo bem, tenha um ótimo dia :)")