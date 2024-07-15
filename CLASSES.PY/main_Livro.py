from Livro import Livro
livro=Livro("A teoria de tudo","Jane Hawking","editoragente","448")
print(f"editora antiga: {livro.editora}")
x=livro.set_editora("editora do arthur")
print(f"Nova editora: {x}")
y=livro.get_qnt_paginas()
print(f"Quantidade de páginas: {y}")