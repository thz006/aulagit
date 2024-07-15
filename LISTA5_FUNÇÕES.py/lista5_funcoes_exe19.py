def gerar_triangulo(n):
    for i in range(1, n + 1):
        num_asteriscos = 2 * i - 1
        num_espacos = n - i
        print(' ' * num_espacos + '*' * num_asteriscos)

# Exemplo de uso
n = 6
gerar_triangulo(n)
