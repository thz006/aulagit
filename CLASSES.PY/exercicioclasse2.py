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

livro=Livro("A teoria de tudo","Jane Hawking","editoragente","448")
print(f"editora antiga: {livro.editora}")
x=livro.set_editora("editora do arthur")
print(f"Nova editora: {x}")
y=livro.get_qnt_paginas()
print(f"Quantidade de páginas: {y}")