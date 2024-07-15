class Funcionario:
    def __init__(self,nome,sobrenome,horas_trabalhadas=50,valor_hora=17):
        self.nome=nome
        self.sobrenome=sobrenome
        self.horas_trabalhadas=horas_trabalhadas
        self.valor_hora=valor_hora
    
    def nome_completo(self):
        print(f"Olá, {self.nome} {self.sobrenome}")

    def incrementar_horas(self):
        incremento=float(input("digite o incremento: "))
        self.valor_hora+=incremento

    def calcular_salario(self):
        print("Seu salário será de: R$",self.horas_trabalhadas*self.valor_hora,"reais")

funci=Funcionario("Arthur","Santoro Gomes")
funci.nome_completo()
funci.incrementar_horas()
funci.calcular_salario()