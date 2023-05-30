from random import randint
escolha = int(input('''Escolha a sua jogada!
1 - Pedra.
2 - Papel.
3 - Tesoura.
Insira o número da opção desejada: '''))
escolhapc = randint(1,3)
if escolha == escolhapc:
    print("Empate, o computador escolheu a mesma opção que você selecionou.")
elif escolha == 1 and escolhapc == 2:
    print("O computador escolheu papel, e como todos sabemos papel ganha da pedra, ou seja Parabéns Computador!")
elif escolha == 2 and escolhapc == 1:
    print("O computador escolheu pedra, e como todos sabemos papel ganha da pedra, ou seja Parabéns Jogador!")
elif escolha == 3 and escolhapc == 1:
    print("O computador escolheu pedra, e como todos sabemos a pedra ganha da tesoura, ou seja Parabéns Computador!")
elif escolha == 1 and escolhapc == 3:
    print("O computador escolheu tesoura, e como todos sabemos a pedra ganha da tesoura, ou seja Parabéns Jogador!")
elif escolha == 2 and escolhapc == 3:
    print("O computador escolheu tesoura, e como todos sabemos a tesoura ganha do papel, ou seja Parabéns Computador!")
elif escolha == 3 and escolhapc == 2:
    print("O computador escolheu papel, e como todos sabemos a tesoura ganha do papel, ou seja Parabéns Jogador!")
elif escolha >3 or escolha < 1:
    print("Número inválido, tente novamente.")
print(escolhapc)

    # Tudo Certo!