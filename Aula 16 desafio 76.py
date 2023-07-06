pep = ('Carro', '50.000', 'Casa', '1.200', 'Geléia', '5.00', 'Suco de Maçã', '1.00')
e = 0
print(41*"-")
print("Listagem de Preços".center(41))
print(41*"-")
while True:
    q = 30 - len(pep[e])
    print(pep[e], end="")
    e += 1
    print(q * ".","R$:", (pep[e]).rjust(6))
    e += 1
    if e >= (len(pep)):
        break
print(41*"-")