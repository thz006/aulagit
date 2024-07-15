class Filme:
    def __init__(self,nome,duracao):
        self.nome=nome
        self.duracao=duracao
    
    def get_play(self):
        print("O filme",self.nome,"começou!!")
    
class Drama(Filme):
    def __init__(self,nome,duracao,ator):
        super().__init__(nome,duracao)
        self.ator=ator
    
    def play(self):
        print(self.nome,"começou a chorar!")

class Acao(Filme):
    def __init__(self,nome,duracao,explosao):
        super().__init__(nome,duracao)
        self.explosao=explosao

    def play(self):
        print("O filme",self.nome,"começou a explodir!!")

class Suspense(Filme):
    def __init__(self,nome,duracao,susto):
        super().__init__(nome,duracao)
        self.susto=susto
    
    def assustar(self):
        print("Você",self.susto,"com o filme",self.nome,"!!!")