fras = (input("Digíte uma frase: ").strip())
frase = fras.replace(" ","")
if frase == frase[::-1]:
    print("Está frase é um Palíndromo.")
else:
    print("Está frase não é um Palíndromo.")

    # Tudo Certo!