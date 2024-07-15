class Livro:
    def __init__(self,nome,autor,editora,paginas):
        self.nome=nome
        self.autor=autor
        self.editora=editora
        self.paginas=paginas
    
    def set_editora(self,edit):
        self.editora=edit
        return self.editora
    
    def get_qnt_paginas(self):
        return self.paginas