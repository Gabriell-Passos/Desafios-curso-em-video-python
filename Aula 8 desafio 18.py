import math

print("Calculadora seno, cosseno e tangente!")
a = int(input("Insira o valor do ângulo em graus: "))
a_rad = math.radians(a)
seno = math.sin(a_rad)
cosseno = math.cos(a_rad)
tangente = math.tan(a_rad)

print("O seno, cosseno e tangente do ângulo {} graus, respectivamente, são: {:.3f} - {:.3f} - {:.3f}".format(a, seno, cosseno, tangente))

    # Tudo Certo!
