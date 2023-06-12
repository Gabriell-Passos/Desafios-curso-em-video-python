while True:
    numero = int(input("Insira um número para ver sua tabuada: (número negativo encerra o programa): "))
    if numero <= -1:
            break
    for n in range (0,11):
        v = numero*n
        print(f"{numero} X {n} = {v}")
print("Programa finalizado, tenha um bom dia :)")
        
    # Tudo Certo!