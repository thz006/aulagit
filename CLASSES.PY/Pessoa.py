class Pessoa:
    def __init__(self,nome,idade,endereco):
        self.nome= nome
        self.idade=idade
        self.endereco=endereco
    
    def get_nome(self):
        return self.nome
    def get_idade(self):
        return self.idade
    def get_end(self):
        return self.endereco