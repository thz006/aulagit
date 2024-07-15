def notas_aluno():
    print("pesos n1-peso 5/ n2-peso 3/ n3-peso 2")
    n1=float(input("nota 1: "))
    n2=float(input("nota 2: "))
    n3=float(input("nota 3: "))

    letra=str(input("digite A ou P: "))
    if letra == "a" or letra == "A":
        media =(n1+n2+n3)/3
        print(f"A média aritmética será: {media:.2f}")
    elif letra == "p" or letra == "P":
        media = ((n1*5) + (n2*3) + (n3*2)) / 10
        print(f"A média poderada será: {media:.2f}")
notas_aluno()    