try:
    n1=int(input("numero (deve ser maior que 5 e menor que 100): "))
    if n1 < 5 and n1 > 100:
        print("(deve ser maior que 5 e menor que 100)")
    n2=int(input("numero (deve ser maior que 5 e menor que 100): "))
    if n2 < 5 and n2 > 100:
        print("(deve ser maior que 5 e menor que 100)")
    n3=int(input("numero (deve ser maior que 5 e menor que 100): "))
    if n3 < 5 and n3 > 100:
        print("(deve ser maior que 5 e menor que 100)")
except:
    print("Número Inválido!")
if n1 <n2 and n1>n3:
    print(n1)
elif n1<n3 and n1>n2:
    print(n1)
elif n2<n1 and n2>n3:
    print(n2)
elif n2<n3 and n2>n1:
    print(n2)
elif n3<n1 and n3>n2:
    print(n3)
elif n3<n2 and n3>n1:
    print(n3)
else:
    print("Números iguais ou inválidos.")