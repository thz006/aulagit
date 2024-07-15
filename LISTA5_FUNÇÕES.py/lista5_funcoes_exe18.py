import random
numeros = []
def sorteia():
    global numeros
    numeros = [random.randint(1, 100) for _ in range(5)]
    print(f"Números sorteados: {numeros}")
def somaPar():
    soma = sum(num for num in numeros if num % 2 == 0)
    print(f"Soma dos valores pares: {soma}")
sorteia()
somaPar()