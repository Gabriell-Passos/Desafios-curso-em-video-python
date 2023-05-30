print( )
nome = str((input("Qual é o seu nome completo? ")).strip())
print("Seu nome todo em maiusculo é: {}".format(nome.upper()))
print("Seu nome todo em minusculo é: {}".format(nome.lower()))
print("Seu nome completo possui {} letras".format(len(nome)-nome.count(' ')))
nome2 = nome.split()
print("Seu primeiro nome é {} e possui {} letras".format(nome2[0], len(nome2[0])))

    # Tudo Certo!