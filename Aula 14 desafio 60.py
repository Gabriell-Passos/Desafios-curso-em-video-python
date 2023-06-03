# Ultilizando o While

numero = int(input("Digite um número para saber o seu fatorial: "))
fatorial = numero
conta = 1
while fatorial > 0:
    conta *= fatorial
    fatorial -= 1

print("O fatorial de {} é igual a {}.".format(numero,conta))

# Ultilizando o For

numero = int(input("Digite um número para saber o seu fatorial: "))
fatorial = 1
for n in range (numero, 0, -1):
    fatorial *= n

print("O fatorial de {} é igual a {}.".format(numero,conta))