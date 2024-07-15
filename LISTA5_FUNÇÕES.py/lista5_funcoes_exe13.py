def potencia(base, expoente):
    resultado = 1
    for _ in range(expoente):
        resultado *= base
    return resultado
base = 5
expoente = 3
print(f"{base} elevado a {expoente} é {potencia(base, expoente)}")