import random
print("Jogo PAR ou IMPAR!")
vitorias = 0
while True:
    na = random.randint(1,2)
    numero = int(input("Insira um número: (1 = IMPAR / 2 = PAR): "))
    if numero > 2 or numero < 1:
        print("escolha inválida.")
    else:
        if na == numero:
            print("Parabéns você ganhou!")
            vitorias += 1
        else:
            print("O computador ganhou, FIM DO JOGO!")
            break
print(f"Você conseguiu ganhar do computador {vitorias} vezes.")

    # Tudo Certo!