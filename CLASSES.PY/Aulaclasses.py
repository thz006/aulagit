class Estudante: ### DEFINIÇÃO DA CLASSE
    def __init__(self,matricula,nome,idade,nota):  ###MÉTODO CONSTRUTOR
        self.matricula= matricula ###ATRIBUTO
        self.nome=nome
        self.idade=idade
        self.nota=nota
    
    def hello(self): ###MÉTODO
        print(f" matrícula {self.matricula}")
        print(f" Olá {self.nome}")
        print(f" idade: {self.idade}")
        print(f" nota: {self.nota}")


aluno2=Estudante(1313,"Arthur",17,100)

aluno2.hello()

print("-"* 30)


class Professor:
    def __init__(self,matricula,nome,idade,salario):
        self.matricula=matricula
        self.nome=nome
        self.idade=idade
        self.salario=salario

    def hello2(self):
        print(f"matricula: {self.matricula}")
        print(f"nome: {self.nome}")
        print(f"idade: {self.idade} anos")
        print(f"salário: R${self.salario},00 reais")
    
professor= Professor(12133,"Thiago",46,25000)

professor.hello2()