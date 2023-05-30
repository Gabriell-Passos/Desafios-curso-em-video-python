print ("Sorteio de 4 alunos com ranking!")
import random
a1 = input("Aluno 1: ")
a2 = input("Aluno 2: ")
a3 = input("Aluno 3: ")
a4 = input("Aluno 4: ")
al = [a1, a2, a3, a4]
random.shuffle (al)
print ("O ranking do sorteio é: {}, {}, {}, {}.".format(*al))

    # Tudo Certo!

