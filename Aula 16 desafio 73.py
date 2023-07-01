print("20 primeiras seleções do dia 29/06/2023")
cbf = ("Botafogo","Grêmio","Flamengo","Palmeiras","Fluminense","Internacional","Red Bull Bragantino","Fortaleza","Athletico-PR","Atlético-MG","São Paulo",
       "Cruzeiro","Santos","Bahia","Corinthias","Cuiabá","Goiás","Vasco","América MG","Coritiba")
print(f"A lista de times do Brasileirão são: {cbf}")
print("-="*30)
print(f"Os 5 primeiros times são: {cbf[0:5]}")
print("-="*30)
print(f"Os ultimos 5 times são: {cbf[15:]}")
print("-="*30)
print(f"Os times em ordem alfabética são: {sorted(cbf)}")
print("-="*30)
while True:
    procura = str(input("Qual time da lista você quer saber a posição? "))
    if procura in cbf:
        print(f"{procura} está na posição {(cbf.index(procura))+1}")
        break
    else:
        print("Este time não está na lista, cheque se o nome foi escrito corretamente, se a primeira letra está maiuscula ou tente outro time.")

    # Tudo Certo!