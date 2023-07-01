n = tuple(input(f"Insira o {n} valor:  ")for n in range(1,5))
vez = "vez"
pares = []
impar = []
for x in range(0,4):
	if int(n[x]) % 2 == 0:
		pares.append(n[x])
	else:
		impar.append(n[x])
if '9' in n:
	if n.count('9') > 1:
		vez = "vezes"
	print(f"O número 9 apareceu {n.count('9')} {vez}.")
else:
	print("O número 9 não apareceu na tupla.")
if '3' in n:
	print(f"O primeiro número 3 aparece na posição {(n.index('3'))+1}.")
else:
	print("O número 3 não apareceu na tupla.")
print(f"Os números pares foram {pares}")
print(f"Os números impares foram {impar}")
print("Não acredita? então cheque você mesmo!", n)

    # Tudo Certo!