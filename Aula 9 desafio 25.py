n = input("Insira um nome: ")
n2 = 'Silva' in n
print("O nome {} possui Silva no nome? {}".format(n,n2))

# agora usando o if

n = input("Insira um nome: ")
n2 = 'Silva' in n
if n2:
    print("O nome {} possui Silva".format(n))
else:
    print("O nome {} não possui Silva".format(n))

    # Tudo Certo!