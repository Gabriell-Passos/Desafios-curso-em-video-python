controle = 0
media = 0
mulheresmenoresde20 = 0
idadehomem = 0
for i in range(1,5):
    print("Insíra os dados da {} pessoa.".format(i))
    nome=input("Insíra o nome: ")
    idade=int(input("Insíra a idade: "))
    media += idade
    print("Seu Gênero é Masculino ou Feminino? ")
    sexo=int(input("Digite 1 para Masculino e 2 para Feminino: "))
    if sexo == 1:
        if idade > idadehomem:
            idadehome = idade
    if sexo == 2 and idade < 20:
        mulheresmenoresde20 += 1
    if sexo > 2 or sexo < 1:
        print("Opção inválida.")
        controle = 1
        break
if controle == 1:
    print("Reinicie a operação e insíra os dados novamente!")
else:
    print("Tudo certo!")
    print("A média de idade nesse grupo foi de {} anos.".format(media/i))
    print("Existem {} mulheres menores de 20 anos.".format(mulheresmenoresde20))
    print("O homem mais velho é o {} com {} anos.".format(idadehomem,idadehomem))