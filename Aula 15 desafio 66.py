conta = 0
quant = 0
while True:
    n = int(input("Insira um número: (use 999 para ver o resultado.): "))
    if n == 999:
        break
    else:
        conta += n
        quant += 1
print(f"Foram digitados {quant} números e a soma de todos eles é igual a {conta}.")

    # Tudo Certo!