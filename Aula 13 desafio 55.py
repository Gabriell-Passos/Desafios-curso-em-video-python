peso=float(input("Quantos kilos a 1 pessoa pesa? "))
pesm = peso
pesa = 0
for p in range(2,6):
    peso=float(input("Quantos kilos a {} pessoa pesa? ".format(p)))
    if peso > pesa:
        pesa = peso
    elif peso < pesm:
        pesm = peso
print("O maior peso foi {} e o menor peso foi {}.".format(pesa, pesm))

    # Tudo Certo!