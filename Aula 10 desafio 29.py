v = float(input("Qual foi a sua volocidade em km/h? "))
if v <= 80:
    print("Tudo certo!")
else:
    va = (v-80)*7
    print("Você excedeu o limite de velocidade de 80km/h, por favor se dirija ao caixa para pagar sua multa de {} reais".format(va))

        # Tudo Certo!