import random
nale=tuple(random.randint(0,999) for v in range(0,5))
calculos = nale[0]
calculosm = nale[0]
for n in range(0,5):
	if nale[n] > calculos:
		calculos = nale[n]
	elif nale[n] < calculosm:
		calculosm = nale[n]
print(f"Os números gerados foram: {nale}")
print(f"O maior número é {calculos} o menor número é {calculosm}")

    # Tudo Certo!

