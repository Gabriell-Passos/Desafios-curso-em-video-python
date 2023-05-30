print ("Calculadora de área e quantidade de tinta!")
a = float(input("Insira a altura da parede em metros: "))
l = float(input("Insira a largura da parede em metros: "))
ap = a*l
qt = ap/2
print("Sua parede possui {} metros quadrados, e são necessário {:.1f} litros de tinta para pinta-la.".format(ap, qt))

    # Tudo Certo!