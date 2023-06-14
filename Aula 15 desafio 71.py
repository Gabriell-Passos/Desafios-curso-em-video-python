valor = int(input("Quanto você quer sacar? (numero inteiro) "))
valor2 = valor
valor3 = 0
valorc = str(valor)
valorn = int(len(valorc))
valorcn = 0
print(10*"-","Você vai receber",10*"-")
while valorn > 0:
    valor2 = int(valorc[valorn -1]+(valorcn*"0"))
    valor3 = valor2
    if valorcn == 0:
        print(f"{valor3 / 1:.0f} moedas de 1 Real.")
    elif valorcn == 1:
        print(f"{valor3 / 10:.0f} notas de 10 Reais.")
    elif valorcn == 2:
        print(f"{valor3 / 20:.0f} notas de 20 Reais.")
    elif valorcn >= 3:
        print(f"{valor3 / 50:.0f} notas de 50 Reais.")
    valorn -= 1
    valorcn += 1
print(11*"-"+"----------------"+11*"-")
