n = str(input("Digite um número inteiro entre 0 e 9999: ")).strip()
nint = int(n)
u = nint // 1 % 10
d = nint // 10 % 10
c = nint // 100 % 10
m = nint // 1000 % 10
print("Sua unidade é {}".format(u))
print("Sua dezena é {}".format(d))
print("Sua centena é {}".format(c))
print("Seu milhar é {}".format(m))

    # Tudo Certo!