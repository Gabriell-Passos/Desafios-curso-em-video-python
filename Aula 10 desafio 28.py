from random import randint
r = randint(0,5)
rr = int(input("eu pensei em um número entre 0 e 5, qual você acha que é? "))
if r ==rr:
    print("Parabéns, você acertou :)")
else:
    print("Não foi esse número que pensei :(")
print("O número que pensei foi o {}.".format(r))

    # Tudo Certo!