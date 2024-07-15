class Conta:
    def __init__(self,nome,cpf,numero,saldo=0):
        self.nome=nome
        self.nome=cpf
        self.numero=numero
        self.saldo=saldo

    def depositar(self,valor):
        if valor > 0:
            self.saldo+= valor
            print(f"Você depositou R${valor},00 reais na sua conta, seu saldo agora é: R${self.saldo},00 reais")
        else:
            print("Valor de depósito inválido")
    
    def sacar(self,valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo-= valor
            print(f"Você sacou R${valor},00 reais na sua conta, seu saldo agora é: R${self.saldo},00 reais")
        else:
            print("Valor de saque inválido")

    def get_saldo(self):
        print(f"Seu saldo é de: {self.saldo:.2f}")
saldo= Conta("Arthur","08436089197","67 996331772")
saldo.get_saldo()
saldo.depositar(300000)
saldo.sacar(10000000)
saldo.get_saldo()