class Pessoa:
    def __init__(self,matricula,nome,idade):
        self.matricula=matricula
        self.nome=nome
        self.idade=idade
    def ola(self):
        print("Olá,",self.nome)

class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade, notas=0, media=0):
        super().__init__(matricula, nome, idade)
        self.notas=notas
        self.media=media
    def estudar(self):
        print("O aluno ",self.nome,"está  estudando!!")
    def calcular_media(self,n1,n2,n3):
        media=(n1 + n2 + n3)/3
        print(f"A média do Aluno {self.nome} é:{media:.2f}")
class Professor(Pessoa):
    def __init__(self, matricula, nome, idade, formacao, disciplina, carga_horaria, salario):
        super().__init__(matricula, nome, idade)
        self.formacao=formacao
        self.disciplina=disciplina
        self.carga_horaria=carga_horaria
        self.salario=salario
    def ir_para_escola(self):
        print("O professor",self.nome,"está indo para a escola!!")
    def lecionar(self):
        print("O professor",self.nome,"começou a lecionar!!")