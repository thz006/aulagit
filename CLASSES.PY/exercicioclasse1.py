class Pessoa:
    def __init__(self,nome,idade,endereco):
        self.nome=nome
        self.idade=idade
        self.endereco=endereco
    
    def mostrar_nome(self):
        return self.nome
    def definir_idade(self,a):
        self.idade=a
        return self.idade
    def mostrar_endereco(self):
        return self.endereco
    
pessoa= Pessoa("Arthur","17","rua da saudade 189")
x=pessoa.mostrar_nome()
print(f"nome: {x}")
print(F"idade anterior: {pessoa.idade}")
y=pessoa.definir_idade(18)
print(f"idade nova: {y}")
z=pessoa.mostrar_endereco()
print(f"endereço: {z}")