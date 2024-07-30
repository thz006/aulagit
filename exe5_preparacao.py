n = int(input("Informe o numero de pessoas infectadas no dia 0: "))
r = int(input("Digite o numero do fator reprodutivo: "))
p = int(input("Pessoas a ser infectadas: "))
i = True
cont = n
d=0
s=0
som = 0
while i == True:
    cont = n*r
    som = cont + n + s
    s = n + s
    n = cont
    d += 1
    if som == p or p <= som:
        print(f"Serão necessarios {d} dias para infectar {p} Pessoas")
        break