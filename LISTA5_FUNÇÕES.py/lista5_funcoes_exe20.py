import random

def sorteiaAluno(qtd_alunos):
    # Lista para armazenar os nomes dos alunos
    alunos = []
    
    # Solicita os nomes dos alunos
    for _ in range(qtd_alunos):
        nome = input("Digite um nome: ")
        alunos.append(nome)
    
    # Sorteia um aluno da lista
    aluno_sorteado = random.choice(alunos)
    
    # Retorna o aluno sorteado
    print(f"O primeiro aluno(a) a apresentar será: {aluno_sorteado}")

# Exemplo de uso
sorteiaAluno(6)
