class Aluno_Academia:
    def __init__(self,nome,idade,peso,altura,mensalidade=120):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.altura=altura
        self.mensalidade=mensalidade

    def calcular_imc(self):
        imc=self.peso/(self.altura**2)
        print(self.nome,f"Seu IMC é: {imc:.2f}")
    
    def obter_valor_mensalidade(self):
        if self.idade >=18:
            print("Sua mensalidade é de R$120,00 reais")
        else:
            print("Sua mensalidade é de R$90,00 reais")