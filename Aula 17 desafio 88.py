import random

números = []

palpites = []

escolha = int(input("Quantos palpites você deseja: "))

for palpite in range(0,escolha):
    for controle in range(0,6):
        naleatório = random.randint(0,60)
        números.append(naleatório)
    números.append(palpites)

    print(f"Jogo {palpite+1} = {palpites[palpite]}")
    
print(números)

#precisa da solução