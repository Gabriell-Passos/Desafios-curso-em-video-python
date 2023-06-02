n = 1
par = 0
impar = 0
while n != 0:
    n = int(input("Insíra um valor: "))
    if n != 0 and n % 2 == 0:
        print("Este número é par")
        par += 1
    elif n != 0 and n % 2 != 0:
        print("Este número é impar")
        impar += 1
print("Você digitou {} número impares e {} números pares.".format(impar, par))
print("Fim!")