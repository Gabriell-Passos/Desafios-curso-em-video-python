numero = 0
quant = 0
cont = 0
maior = 0
menor = 0
cont2 = 0 
while True:
    numero = int(input("Digite um número: "))
    cont += 1
    quant += numero
    escolha = int(input("Quer continuar? [1 = sim / 2 = não]"))
    if cont2 == 0:
        menor = escolha
    cont2 = 1
    if escolha > maior:
        maior = escolha
    elif escolha < menor:
        menor = escolha
    if escolha == 2:
        break
resultado = quant/cont
print("A média de todos os {} números é igual a {:.2f}.".format(cont, resultado))
print("O maior número dentre todos é {} e o menor número é {}.".format(maior, menor))

    # Tudo Certo!