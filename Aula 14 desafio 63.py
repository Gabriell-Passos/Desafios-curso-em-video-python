print("SEQUÊNCIA DE FIBONACCI!")
ter = int(input("Quantos termos você quer ver? (A partir de 4): "))
if ter < 4:
    print("Por favor digíte um número maior que 3.")
else:
    t1 = 0
    t2 = 1
    t3 = t1 + t2
    cont = 0
    print ("{} - {} - {} - ".format(t1, t2, t3),end='')
    while True:
        t1 = t2
        t2 = t3
        t3 = t1 + t2
        print("{} - ".format(t3), end='')
        if cont == (ter - 4):
            print("FIM")
            break
        else:
            cont += 1
    print("Ai estão os {} termos da sequência de Fibonacci.".format(ter))

        # Tudo Certo!