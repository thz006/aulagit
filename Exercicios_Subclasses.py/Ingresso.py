class Ingresso:
    def __init__(self,preco,setor):
        self.preco=preco
        self.setor=setor
    def set_preco(self,novo_preco):
        print("Preço antigo: ",self.preco)
        self.preco=novo_preco
        novo_preco=float(input("novo preço: "))
        print("Preço atual: ",novo_preco)
        return novo_preco
    def get_setor(self):
        print("Setor: ",self.setor)

class IngressoVIP(Ingresso):
    def __init__(self, preco, setor, camarote=False, open_bar=False, open_food=False, estacionamento=False):
        super().__init__(preco, setor)
        self.camarote=camarote
        self.open_bar=open_bar
        self.open_food=open_food
        self.estacionamento=estacionamento
    def pegar_bebida(self):
        print("Preço: ",self.preco,"Você comprou uma bebida!!")
    def acessar_camarote(self):
        self.camarote=True
        self.open_bar=True
        self.open_food=True
        self.estacionamento=True
        if self.camarote and self.open_bar and self.open_food and self.estacionamento==True:
            print("Seu ingresso tem tudo incluso!!!")
        else:
            print("Seu ingresso não é vip!")