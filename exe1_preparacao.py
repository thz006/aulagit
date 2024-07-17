listaV=[]
for i in range (1,7):
    result=str(input("V para venceu e P para perdeu: "))
    if result=="V" or result=="v":
        listaV.append(result)
if len(listaV) >=5:
    print("1")
elif len(listaV) >=3 and len(listaV) <=4:
    print("2")
elif len(listaV) >=1 and len(listaV) <=2:
    print("3")
else:
    print("-1")