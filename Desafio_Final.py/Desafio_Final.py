produtos = [
    {'codigo': 1001, 'nome': 'Sabonete', 'descricao': 'Sabonete em barra', 'tipo': 'Higiene', 'subtipo': 'Banho', 'preco': 2.50, 'estoque': 100},
    {'codigo': 1002, 'nome': 'Macarrão', 'descricao': 'Macarrão espaguete', 'tipo': 'Alimento', 'subtipo': 'Massas', 'preco': 5.00, 'estoque': 50},
    {'codigo': 1003, 'nome': 'Detergente', 'descricao': 'Detergente líquido', 'tipo': 'Produtos para casa', 'subtipo': 'Limpeza', 'preco': 4.30, 'estoque': 80},
    {'codigo': 1004, 'nome': 'Coca-Cola', 'descricao': 'Refrigerante', 'tipo': 'Alimento', 'subtipo': 'Bebidas', 'preco': 8.20, 'estoque': 120},
    {'codigo': 1005, 'nome': 'Arroz', 'descricao': 'Saco de Arroz', 'tipo': 'Alimento', 'subtipo': 'Grãos', 'preco': 12.00, 'estoque': 210}
]
### listas de armazenamento de info
clientes = []
funcionarios = []
###FUNÇÕES EM GERAL
def menu_inicial():
    while True:
        print("\nMenu Inicial")
        print("1. Entrar como Funcionário")
        print("2. Entrar como Cliente")
        print("3. Cadastrar Funcionário")
        print("4. Cadastrar Cliente")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            login_funcionario()
        elif opcao == '2':
            login_cliente()
        elif opcao == '3':
            cadastrar_funcionario()
        elif opcao == '4':
            cadastrar_cliente()
        elif opcao == '5':
            break
        else:
            print("Opção inválida! Tente novamente.")

def cadastrar_funcionario():
    matricula = input("Digite a matrícula do funcionário: ")
    nome = input("Digite o nome do funcionário: ")
    email = input("Digite o e-mail do funcionário: ")
    cpf = input("Digite o CPF do funcionário: ")
    senha = input("Digite a senha do funcionário: ")
    funcionarios.append({'matricula': matricula, 'nome': nome, 'email': email, 'cpf': cpf, 'senha': senha})
    print(f"Funcionário {nome} cadastrado com sucesso!")

def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    clientes.append({'nome': nome, 'cpf': cpf, 'carrinho': []})
    print(f"Cliente {nome} cadastrado com sucesso!")

def login_funcionario():
    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua senha: ")
    for func in funcionarios:
        if func['cpf'] == cpf and func['senha'] == senha:
            menu_funcionario(func)
            return
    print("CPF ou senha incorretos!")

def login_cliente():
    cpf = input("Digite seu CPF: ")
    for cli in clientes:
        if cli['cpf'] == cpf:
            menu_cliente(cli)
            return
    print("Cliente não encontrado! Faça o cadastro primeiro.")

def menu_funcionario(funcionario):
    while True:
        print(f"\nBem-vindo, {funcionario['nome']}!")
        print("1. Consultar Estoque")
        print("2. Atualizar Estoque")
        print("3. Adicionar Novo Produto")
        print("4. Editar Preço de Produto")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            consultar_estoque()
        elif opcao == '2':
            atualizar_estoque()
        elif opcao == '3':
            adicionar_produto()
        elif opcao == '4':
            editar_preco_produto()
        elif opcao == '5':
            break
        else:
            print("Opção inválida! Tente novamente.")

def menu_cliente(cliente):
    while True:
        print(f"\nBem-vindo, {cliente['nome']}!")
        print("1. Adicionar Produtos ao Carrinho")
        print("2. Remover Produtos do Carrinho")
        print("3. Finalizar Compra")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_ao_carrinho(cliente)
        elif opcao == '2':
            remover_do_carrinho(cliente)
        elif opcao == '3':
            finalizar_compra(cliente)
        elif opcao == '4':
            break
        else:
            print("Opção inválida! Tente novamente.")

def consultar_estoque():
    for produto in produtos:
        print(f"Código: {produto['codigo']} - {produto['nome']} ({produto['subtipo']} - {produto['tipo']}): R${produto['preco']:.2f}")

def atualizar_estoque():
    codigo = int(input("Digite o código do produto: "))
    quantidade = int(input("Digite a nova quantidade em estoque: "))
    for produto in produtos:
        if produto['codigo'] == codigo:
            produto['estoque'] = quantidade
            print(f"Estoque atualizado para {quantidade} unidades.")
            return
    print("Produto não encontrado!")

def adicionar_produto():
    codigo = int(input("Digite o código do produto: "))
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")
    tipo = input("Digite o tipo do produto: ")
    subtipo = input("Digite o subtipo do produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = int(input("Digite a quantidade em estoque: "))
    novo_produto = {'codigo': codigo, 'nome': nome, 'descricao': descricao, 'tipo': tipo, 'subtipo': subtipo, 'preco': preco, 'estoque': estoque}
    produtos.append(novo_produto)
    print(f"Produto {nome} adicionado com sucesso!")

def editar_preco_produto():
    codigo = int(input("Digite o código do produto: "))
    novo_preco = float(input("Digite o novo preço do produto: "))
    for produto in produtos:
        if produto['codigo'] == codigo:
            produto['preco'] = novo_preco
            print(f"Preço do produto {produto['nome']} atualizado para R${novo_preco:.2f}.")
            return
    print("Produto não encontrado!")

def adicionar_ao_carrinho(cliente):
    consultar_estoque()
    codigo = int(input("Digite o código do produto que deseja adicionar ao carrinho: "))
    quantidade = int(input("Digite a quantidade: "))
    for produto in produtos:
        if produto['codigo'] == codigo:
            if produto['estoque'] >= quantidade:
                cliente['carrinho'].append((produto, quantidade))
                produto['estoque'] -= quantidade
                print(f"{quantidade} unidades de {produto['nome']} adicionadas ao carrinho.")
                return
            else:
                print("Quantidade indisponível em estoque!")
                return
    print("Produto não encontrado!")

def remover_do_carrinho(cliente):
    for i, item in enumerate(cliente['carrinho']):
        produto, quantidade = item
        print(f"{i+1}. {produto['nome']} - {quantidade} unidades")
    opcao = int(input("Digite o número do produto que deseja remover: "))
    if 1 <= opcao <= len(cliente['carrinho']):
        produto, quantidade = cliente['carrinho'].pop(opcao - 1)
        produto['estoque'] += quantidade
        print(f"{quantidade} unidades de {produto['nome']} removidas do carrinho.")
    else:
        print("Opção inválida!")

def finalizar_compra(cliente):
    if not cliente['carrinho']:
        print("Carrinho vazio! Adicione produtos antes de finalizar a compra.")
        return
    
    total = sum(produto['preco'] * quantidade for produto, quantidade in cliente['carrinho'])
    print("\nNota Fiscal:")
    for produto, quantidade in cliente['carrinho']:
        print(f"{produto['nome']} - {quantidade} unidades - R${produto['preco'] * quantidade:.2f}")
    
    imposto_nacional = total * 0.05
    imposto_estadual = total * 0.08
    imposto_municipal = total * 0.12
    total_impostos = imposto_nacional + imposto_estadual + imposto_municipal
    total_com_impostos = total + total_impostos
    
    print(f"\nTotal: R${total:.2f}")
    print(f"Imposto Nacional: R${imposto_nacional:.2f}")
    print(f"Imposto Estadual: R${imposto_estadual:.2f}")
    print(f"Imposto Municipal: R${imposto_municipal:.2f}")
    print(f"Total de Impostos: R${total_impostos:.2f}")
    print(f"Total com Impostos: R${total_com_impostos:.2f}")

    print("Escolha a forma de pagamento:")
    print("1. Dinheiro")
    print("2. Pix")
    print("3. Cartão de Débito")
    print("4. Cartão de Crédito")
    print("5. Voucher")
    opcao = input("Escolha a forma de pagamento: ")

    if opcao == '1':
        valor_pago = float(input("Digite o valor pago: "))
        if valor_pago > total_com_impostos:
            troco = valor_pago - total_com_impostos
            print(f"Compra finalizada com sucesso! Troco: R${troco:.2f}")
        elif valor_pago == total_com_impostos:
            print("Compra finalizada com sucesso! Valor exato.")
        else:
            print("Valor insuficiente! Tente novamente.")
    elif opcao in ['2', '3', '4', '5']:
        saldo = float(input("Digite o saldo disponível: "))
        if saldo >= total_com_impostos:
            print("Compra finalizada com sucesso!")
        else:
            print("Saldo insuficiente! Tente novamente.")
    else:
        print("Opção inválida! Tente novamente.")

# chama o menu inicial
menu_inicial()