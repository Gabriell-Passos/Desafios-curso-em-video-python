produto = float(input("Insira o valor do produto: ").strip())
print('''Qual será o método de pagamento?
1 - A vista em dinheiro ou cheque.
2 - A vista no cartão.
3 - Em 2 vezes no cartão.
4 - Em 3 ou mais vezes no cartão.''')
pagamento = int(input("Insira o número correspondente a opção desejada: "))
if pagamento > 4:
	print("Número invalido, tente novamente!")
elif pagamento == 1:
	produtod = produto - (produto*10/100)
	print('''Ao pagar a vista no dinheiro ou cheque, você ganha 10% de desconto.
O novo valor do produto será de {} reais, cerca de {} reais de desconto.'''.format(produtod, produto*10/100))
elif pagamento == 2:
	produtod = produto - (produto*5/100)
	print('''Ao pagar a vista no cartão, você ganha 5% de desconto.
O novo valor do produto será de {} reais, cerca de {} reais de desconto.'''.format(produtod, produto*5/100))
elif pagamento == 3:
	print('''Ao pagar em 2 vezes no cartão, o valor se mantem.
O valor do produto será de {} reais, cerca de {} reais de desconto.'''.format(produto, "0"))	
elif pagamento == 4:
	parc = int(input("Será em quantas parcelas? insira um número maior que 2: "))
	if parc < 3:
		print("Você inseriu um número de parcelas menor que 3 e isso é inválido para esta opção, por favor tente novamente.")
	elif parc > 2:
		produtod = produto + (produto*20/100)
		print('''Ao pagar em {} vezes no cartão, você tem 20% de juros.
O novo valor do produto será de {} reais, cerca de {} reais mais caro, o valor das parcela será de {:.2f} Reais por mês..'''.format(parc, produtod, produto*20/100, produtod/parc))

    # Tudo Certo!