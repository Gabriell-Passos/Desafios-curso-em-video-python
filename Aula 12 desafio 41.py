import datetime
an = float(input("Em qual ano você nasceu: "))
ano = int(an)
anoa = datetime.date.today().year
idade = anoa - ano
print("Você tem {} anos de idade.".format(idade))
if idade <= 9:
    print("Você faz parte da categoria mirim.")
elif idade >= 14 and idade < 19:
    print("Você faz parte da categoria infantil.")
elif idade >= 19 and idade < 20:
    print("Você faz parte da categoria junior.")
elif idade == 20:
    print("Você faz parte da categoria sênior.")
elif idade > 20 and idade <= 100:
    print("Você faz parte da categoria master.")
elif idade > 100:
    print("Idade muito alta, tente novamente!")
    
    # Tudo Certo!