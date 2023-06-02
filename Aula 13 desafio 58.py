from random import randint
r = randint(0,10)
rr = None
tentativas = 0
cont = 0
while r != rr:
    try:
        rr = int(input("eu pensei em um número entre 0 e 10, qual você acha que é? "))
    except ValueError:
        print("Você não digitou um número inteiro, tente de novo!!")
        cont = 1
    if cont == 0:
        print("Não foi esse número que pensei, tente novamente ^_^")  
    cont = 0
    tentativas += 1 
print("O número que pensei foi o {}.".format(r))
print("Parabéns, depois de {} tentativas você acertou :)".format(tentativas))
    # Tudo Certo! 