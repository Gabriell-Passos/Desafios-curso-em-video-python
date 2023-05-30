iniciar = input("Insira qualquer coisa para iniciar o programa: ")
#acumuladores
soma = 0
numerousavel = 0

#contas
for num in range(1, 501):
    if num % 2 != 0 and num % 3 == 0:
        numerousavel += 1
        soma += num

#resultado
print("A soma dos {} números ímpares e múltiplos de 3 entre 1 e 500 é: {}".format(numerousavel,soma))
