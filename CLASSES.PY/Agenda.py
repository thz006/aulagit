class Agenda:
    def __init__(self,dia,mes,ano,anotacao=""):
        self.dia=dia
        self.mes=mes
        self.ano=ano
        self.anotacao=anotacao

    def anotar_tarefa(self):
        anotacao=input("Anotação: ")
        self.anotacao=anotacao
    def get_data(self):
        if self.dia >= 1 and self.dia <= 31 and self.mes >= 1 and self.mes <= 12 and self.ano <= 2024 and self.ano > 0:
            print("Data Válida")
        else:
            print("Data Inválida")

    def mostrar_anotacao(self):
        self.anotacao
        print("no dia selecionado a anotação é: ",self.anotacao)
        return self.anotacao
