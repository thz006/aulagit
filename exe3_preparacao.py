try:
    s=int(input("salgados vendidos: "))
    d=int(input("doces vendidos: "))
    b=int(input("bolos vendidos: "))
    if s or d or b <0:
        print("numero invalido")
except:
    print("erro")
salgado_result=s
doce_result=d*2
bolo_result=b*3
soma=salgado_result+doce_result+bolo_result
if soma >= 150:
    print("B")
elif soma >=120 and soma <150:
    print("D")
elif soma >= 100 and soma <120:
    print("S")
elif soma<100:
    print("N")