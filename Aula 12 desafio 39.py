import datetime
an = float(input("Em qual ano você nasceu? "))
ano = int(an)
dac = datetime.date.today().year
if ano < 1900:
    print("Idade muito alta, \033[1;33mtente novamente!\033[m")
elif ano > dac:
    print("Idade incoerente, \033[1;33mtente novamente!\033[m")

elif (ano+18) > dac:
    print("Você não precisa se alistar agora, seu ano de alistamento é em {}, ainda faltam {} anos.".format(ano+18,(ano+18)-dac))

elif (ano+18) < dac:
    print("Seu ano de alistamento foi em {}, e seu tempo de atraso é de {} anos, dirija-se ao quartel imediatamente e realize o seu alistamento militar obrigatório.".format(ano+18, dac-(ano+18)))

elif (ano+18) == dac:
    print("{} é o ano do seu alistamento militar obrigatório, dirija-se \033[1;33mimediatamente\033[m ao quartel para realiza-lo.".format(ano+18))

print("Consulta finalizada!")

    # Tudo Certo!