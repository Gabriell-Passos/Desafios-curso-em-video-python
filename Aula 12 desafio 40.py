n1 = float(input("Insira sua primeira nota: "))
n2 = float(input("Insira sua segunda nota: "))
m = (n1+n2)/2
if m < 5:
    print("Sua média foi de {} pontos, infelizmente você está \033[1;31mREPROVADO.\033[m")
elif m > 5 and m < 6.9:
    print("Sua média foi de {} pontos, infelizmente você está de \033[1;33mRECUPERAÇÃO.\033[m".format(m))
elif m > 7:
    print("Parabéns você foi \033[1;32mAPROVADO.\033[m")
print("Consulta finalizada!")

    # Tudo Certo!