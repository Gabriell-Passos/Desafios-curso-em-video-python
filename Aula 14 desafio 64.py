numero = 0
quant = int(0)
soma = int(0)
while numero < 999:
    numero = int(input("Digíte um número inteiro (se for >= a 999 o programa realiza a conta): "))
    if numero < 999:
        quant += 1
        soma += numero
    else:
        break
print("Foram digitados {} números, e a soma de todos é igual a {}.".format(quant, soma))
   
    # Tudo Certo!