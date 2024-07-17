def conta():
    lista1=[]
    lista2=[]
    if id1 <=17:
        preco=15
        lista1.append(preco)
    elif id1>=18 and id1<=59:
        preco=30
        lista1.append(preco)
    elif id1 >=60:
        preco=20
        lista1.append(preco)
    if id2 <=17:
        preco=15
        lista2.append(preco)
    if id2>=18 and id1<=59:
        preco=30
        lista2.append(preco)
    if id2 >=60:
        preco=20
        lista2.append(preco)
    conta=sum(lista1)+sum(lista2)
    print(conta)
id1=int(input("idade 1: "))
id2=int(input("idade 2: "))
if id1 <=1 or id2 <=1:
    print("erro")
else:
    conta()