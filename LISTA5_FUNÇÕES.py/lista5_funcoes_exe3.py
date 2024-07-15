def numero():
    n1=int(input("numero: "))
    if n1 >=1:
        print("1")
    elif n1<0:
        print("-1")
    elif n1==0:
        print("0")
    return n1
x=numero()