try:
    a=int(input("A: "))
    b=int(input("B: "))
    c=int(input("C: "))
except:
    print("erro")
if (b-a) < (c-b):
    print("1")
elif (b-a) > (c-b):
    print("-1")
elif (b-a) == (c-b):
    print("0")