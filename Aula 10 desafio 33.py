n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))
n3 = int(input("Insira o terceiro número: "))
# maior número
if n1 > n2 :
    nm=n1
else:
    nm=n2
if nm < n3:
    nm=n3
# menor número:
if n1 < n2:
    nn=n1
else:
    nn=n2
if nn > n3:
    nn=n3

print("Entre os números {}, {}, {}, o maior número é o {}, e o menor número é o {}.".format(n1, n2, n3, nm, nn))

    # Tudo Certo!