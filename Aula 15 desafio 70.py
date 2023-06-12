print(41*"-")
print("SUPERMERCADO".center(41))
print(41*"-")
m1000 = 0
total = 0
mnvalor = 0
mnome = "none"
while True:
    nomep = str(input("Qual é o nome do produto? ")).strip()
    print(41*"-")
    valor = float(input("Qual é o valor do produto? "))
    if mnvalor == 0:
        mnvalor = valor
        mnome = nomep
    elif valor < mnvalor:
        mnvalor = valor
        mnome = nomep
    elif valor > 1000:
        m1000 += 1
    total += valor
    print(41*"-")
    escolha = int(input("Você que adicionar mais produtos? (1 = SIM / 2 = NÃO) "))
    if escolha == 2:
        break
print(f"O valor total será de {total:.2f} Reais, {m1000} produtos custam mais de 1000 Reais e o produto mais barato da lista é o {mnome} que custa {mnvalor:.2f}")

    # Tudo Certo!