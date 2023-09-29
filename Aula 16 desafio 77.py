palavras = ("abacaxi","banana","carro","dedo","elefante","fogo","gato","hotel","igreja","janela","kiwi","limao","macaco","navio","olho","pato","queijo",
    "rato","sapato","tigre","uva","vaca","xicara","yoga","zebra","agua","arvore","epoca","indio","oculos","ultimo")
for x in palavras:
    print(f"{x.center(8)} tem {'a'} vogais, e em ordem elas são: {'a'}")
    for y in x:
        print(y)