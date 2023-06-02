sexo = ""
while sexo != "M" and sexo != "F":
    sexo = str(input("Qual é o seu sexo? [M/F]")).upper()
    print("Opção inválida, escola M para Masculino e F para Feminino!")
if sexo == "F":
    print("Você é do sexo feminino.")
elif sexo == "M":
    print("Você é do sexo masculino.")
print("fim!!")