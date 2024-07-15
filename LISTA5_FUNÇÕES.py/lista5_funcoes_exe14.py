def carro():
    km=float(input("km: "))
    litros=float(input("litros: "))
    result=km/litros
    if result < 8:
        print("Gasta muito!")
    elif result >=8 and result <= 15:
        print("Econômico!")
    elif result > 15:
        print("Super econômico!")
carro()