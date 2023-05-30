ar1 = float(input("Insira o valor da primeira reta: "))
br2 = float(input("Insira o valor da segunda reta: "))
cr3 = float(input("Insira o valor da terceira reta: "))
if (br2 - cr3)<ar1<br2+cr3:
    a = 1
else:
    a= 0
if (ar1 - cr3)<br2<ar1+cr3:
    b = 1
else:
    b= 0
if (ar1 - br2)<cr3<ar1+br2:
    c = 1
else:
    c= 0
if a+b+c==3:
    print("As três retas podem formar um triângulo.")
    if ar1==br2==cr3:
        print("Será formado um triángulo equilátero.")
    elif ar1 == br2 or ar1 == cr3 or br2 == cr3:
        print("Será formado um triángulo isóceles.")
    elif ar1 != br2 != cr3:
        print("Será formado um triángulo escaleno.")
else:
    print("As três retas não podem formar um triângulo.")

    # Tudo Certo!