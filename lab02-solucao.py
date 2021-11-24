# Sergio Akira Sarui Junior

entrada = ['1 1', '1000', '1000', '3 4', '1 3 5', '2 4 6 8', '10 9', '1 1 2 3 5 7 8 8 9 15', '2 2 2 3 4 6 10 11 11', '0 0']
linha = entrada[0]
i = 0
while (linha != '0 0'):
    possiveisalice = 0
    possiveisbetty = 0
    cartasadicionadas = []
    cartasAlice = entrada[i+1].split()
    cartasBetty = entrada[i+2].split()
    i += 3
    for x in cartasAlice:
        if (x not in cartasBetty) and (x not in cartasadicionadas):
            possiveisalice += 1
            cartasadicionadas.append(x)

    for x in cartasBetty:
        if (x not in cartasAlice) and (x not in cartasadicionadas):
            possiveisbetty += 1
            cartasadicionadas.append(x)


    if (possiveisbetty > possiveisalice):
        print(possiveisalice)
    else:
        print(possiveisbetty)

    linha = entrada[i]