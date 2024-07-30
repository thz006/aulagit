a=int(input("caixa 1: "))
b=int(input("caixa 2: "))
c=int(input("caixa 3: "))
if (a == b and a == c):
    print("3")
elif (a > b and b > c) or (a > c and c > b) or (b > a and a > c) or (b > c and c > a) or (c > a and a > b) or (c > b and b > a):
    print("1")
elif (a+b <c) or (a+c < b) or (b+c <a):
    print("1")
else:
    print("2")