class Carro:
    def __init__(self,modelo,marca,cor,ano,valor,consumo,nivel=0):
        self.modelo=modelo
        self.marca=marca
        self.cor=cor
        self.ano=ano
        self.valor=valor
        self.consumo=consumo
        self.nivel=nivel
    
    def abastecer(self):
        abastecer=int(input("digite quantos litros quer abastecer: "))
        print("você abasteceu ",abastecer,"litros de gasolina")
        distancia=float(input("digite a distância percorrida: "))
        nivel= distancia/abastecer
        print("consumo: ",nivel)
        return distancia
        
    def calcular_imposto(self):
        imposto=(self.valor*2.5) / 100
        print("O valor do IPVA será de: R$",imposto,",00 reais")