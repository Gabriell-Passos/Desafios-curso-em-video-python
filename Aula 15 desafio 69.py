print("Cadastro de pessoas.")
idade18 = 0
homens = 0
mulherm20 = 0
while True:
    nome = str(input("Qual o nome desta pessoa? "))
    idade = int(input("Qual é a idade desta pessoa? "))
    if idade >= 18:
        idade18 += 1
    while True:
        sexo = int(input(("Qual o sexo desta pessoa? (1 = Masculino / 2 = Feminino) ")))
        if sexo != 1 and sexo != 2:
            print("Escolha inválida.")
        else:
            break
    if sexo == 1:
        homens += 1
    elif sexo == 2 and idade < 20:
        mulherm20 += 1
    escolha = int(input("Você deseja adicionar mais pessoas? (1 = Sim / 2 = Não) "))
    if escolha != 1 and escolha != 2:
        print("Escolha inválida.")
    elif escolha == 2:
        break
print("Encerrando programa, tenha um bom dia!")
print(f"Nesta lista tem {idade18} pessoas maiores de 18 anos, {mulherm20} mulheres menores de 20 anos e {homens} homens.")

    # Tudo Certo!
