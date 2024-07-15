def gerar_triangulo_lateral(n):
    for i in range(n):
        print('!' * i)
    for i in range(n - 1, 0, -1):
        print('!' * i)

# Exemplo de uso
n = 4
gerar_triangulo_lateral(n)
