class Aluno:
    def __init__(self,nome,ra,nota1,nota2,nota3,nota4):
        self.nome=nome
        self.ra=ra
        self.nota1=nota1
        self.nota2=nota2
        self.nota3=nota3
        self.nota4=nota4
    
    def calcular_media(self):
        return (self.nota1+self.nota2+self.nota3+self.nota4) / 4
    
    def mostrar_situacao(self):
        media=self.calcular_media()
        if media >= 7:
            print("Aprovado!")
        elif media >= 5 and media <= 6.9:
            print("Exame!")
        else:
            print("Reprovado!") 
       
situacao=Aluno("Arthur","12143",10,10,10,10)
x=situacao.calcular_media()
print(x)
y=situacao.mostrar_situacao()
print(y)