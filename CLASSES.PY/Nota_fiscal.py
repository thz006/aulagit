class Nota_fiscal:
    def __init__(self,numero,tipo,serie,cnpj,razao_social,data,valor_produtos,icms,frete,ipi,valor_total=0):
        self.numero=numero
        self.tipo=tipo
        self.serie=serie
        self.cnpj=cnpj
        self.razao_social=razao_social
        self.data=data
        self.valor_produtos=valor_produtos
        self.icms=icms
        self.frete=frete
        self.ipi=ipi
        self.valor_total=valor_total

    def obter_numero(self):
        print("Número: ",self.numero)
    
    def obter_data_emissao(self):
        print("Data emissão: ",self.data)
    
    def alterar_razao_social(self):
        alterar=input("alterar razão social: ")
        print("Nova razão social: ",alterar)

    def calcular_valor_total(self):
        total=self.valor_produtos + self.frete + self.icms + self.ipi
        print("O valor total com fretes e impostos será de: ",total)