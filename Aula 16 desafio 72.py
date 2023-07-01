nex = ("zero","um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze",
        "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

escolha = int(input("Digite um número entre 0 e 20: "))
while escolha > 20 or escolha < 0:
    escolha = int(input("\033[1;31;40mNumero inválido\033[m digite um número entre 0 e 20: "))
print(f"Você digitou o número {nex[(escolha)]}.")

    # Tudo Certo!