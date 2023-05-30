import time
datah = time.localtime().tm_year
maiores = 0
menores = 0
for a in range(1,8):
    d = int(input("Em qual ano a {} pessoa nasceu? ".format(a)))
    print("Quem nasceu em {} hoje tem {} anos.".format(d,datah - d))
    if datah - d >= 21:
        maiores += 1
    else:
        menores += 1
print("Considerando 21 anos como maior idade, nesta lista existem {} maiores de idade e {} menores de idade.".format(maiores, menores))

    # Tudo Certo!
