casa = float(input("Qual é o valor da casa em Reais? "))
salario = float(input("Qual é o seu salário em Reais? "))
anos = int(input("Em quantos anos você pretende pagar? "))
vprestacao = casa/(anos*12)
if vprestacao < salario*30/100:
    print("Parabéns seu empréstimo foi \033[1;32mAPROVADO!!\033[m")
    print("Você terá que pagar {:.2f} Reais por mês.".format(vprestacao))
else:
    print("Desculpe seu empréstimo foi \033[1;31mRECUSADO!!\033[m")
    print("Tente novamente após um aumento salarial, ou escolha um tempo maior de pagamento.")
print(vprestacao)

    # Tudo Certo!