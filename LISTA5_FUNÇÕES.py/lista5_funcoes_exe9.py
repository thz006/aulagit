def volume_cilindro():
    altura=float(input("altura: "))
    raio=float(input("raio: "))
    volume=3.141592*(raio**2)*altura
    print(f"O volume será: {volume:.2f} ")
volume_cilindro()