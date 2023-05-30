peso = float(input('Quantos é seu peso atual em kg? ').strip())
altura = float(input('Qual a sua altura atual em cm? '))
alturac = altura / 100
imc = peso / (alturac)**2
if altura < 3:
	print("Por favor, insira sua altura em centimentros, sem ponto ou virgula.")
else:
	if imc <= 18.5:
		print("Seu IMC é {:.1f} você está abaixo do peso.".format(imc))
	elif imc > 18.5 and imc <= 25:
		print("Seu IMC é {:.1f} parabéns você está no seu peso ideal.".format(imc))
	elif imc > 25 and imc <= 30:
		print("Seu IMC é {:.1f} você está com sobrepeso.".format(imc))
	elif imc > 30 and imc <= 40:
		print("Seu IMC é {:.1f} você está com obesidade.".format(imc))
	elif imc > 40:
		print("Seu IMC é {:.1f} você está com obesidade morbida.".format(imc))

    # Tudo Certo!