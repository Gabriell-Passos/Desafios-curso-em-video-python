s = float(input("Qual é o seu salário: "))
if s > 1250:
    sa = s + (s/10)
else:
    sa = s + (s/6.666666666666667)
ssa = sa-s
print("Seu salário terá um acréscimo de {} reais, e ao todo você recebera {} reais no proximo mês.".format(ssa, sa))

    # Tudo Certo!