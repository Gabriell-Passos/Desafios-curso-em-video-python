f = str(input("Insira uma frase: ")).upper().strip()
print("A frase {} tem {} letras A".format(f, f.count('A')))
print("A primeira letra A apareceu na posição {}".format(f.find('A')+1))
print("A última letra A apareceu na posição {}".format(f.rfind('A')+1))

    # Tudo Certo!