print("Bem-vindo ao programa de questionário!")

# Perguntas ao usuário
nome = input("Qual é o seu nome? ")
idade = input("Qual é a sua idade? ")
cpf = input("Qual é o seu CPF? ")
sexo = input("Qual é o seu sexo? ")
rg = input("Qual é o seu RG? ")
data_nascimento = input("Qual é a sua data de nascimento? ")
endereco = input("Qual é o seu endereço? ")
telefone = input("Qual é o seu número de telefone? ")

print("\nResumo das informações fornecidas:")
print("Nome:", nome)
print("Idade:", idade)
print("CPF:", cpf)
print("Sexo:", sexo)
print("RG:", rg)
print("Data de Nascimento:", data_nascimento)
print("Endereço:", endereco)
print("Número de Telefone:", telefone)

# Verificação das informações
confirmacao = input("\nAs informações estão corretas? (sim/não): ")

if confirmacao.lower() == "sim":
    print("\nÓtimo! Agora é hora de recitar um poema.")
    poema = input("Por favor, recite um poema: ")
    
    print("\nObrigado por compartilhar o poema!")
    casa_bonita = input("Por fim, sua casa é bonita? (sim/não): ")
    
    if casa_bonita.lower() == "sim":
        print("Que maravilha!")
    else:
        print("Tudo bem, a beleza é subjetiva.")
else:
    print("Desculpe por qualquer erro nas informações fornecidas. Por favor, execute o programa novamente.")

