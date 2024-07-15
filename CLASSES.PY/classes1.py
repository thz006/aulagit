class Automovel:
    def __init__(self,marca,modelo,cor,ano,placa="DKP-8205"):
        self.marca= marca
        self.modelo= modelo
        self.cor= cor
        self.ano= ano
        self.placa= placa
    
    def getDados(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Ano: {self.ano}")
        print(f"Placa: {self.placa}")

carro=Automovel("Ferrari","SF90 Spider","Vermelha",2024)
carro.getDados()