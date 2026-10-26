# StockTech - Sistema De Controle De Estoque
produtos = {}
while True:
    print("\n======STOCKTECH======")
    print("1- Cadastrar Produto")
    print("2- Listar Produtos")
    print("3- Consultar Produto")
    print("4- Sair")

    opcao = input("Escolha uma opcao:")

# OPCAO 1 - CADASTRAR PRODUTO
    if opcao == "1":
        codigo = input("Digite o codigo do produto:")
        nome = input("Digite o nome do produto:")
        preco = float(input("Digite o preco do produto:"))
        quantidade = int(input("Digite a quantidade do produto:"))

    produtos[codigo] = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    print("Produto Cadastrado com Sucesso!")

# OPCAO 2 - LISTAR PRODUTOS
    elif opcao == "2":
    if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            for codigo, produto in produtos.items():
                print("\nCodigo:", codigo)
                print("Nome:", produto["nome"])
                print("Preco:", produto["preco"])
                print("Quantidade:", produto["quantidade"])
                print("------------------------")

# OPCAO 3 - CONSULTAR PRODUTO
    elif opcao == "3":            
        print("Consultar Produto - em desenvolvimento")

# OPCAO 4 - SAIR    
    elif opcao == "4":
        print("Saindo do sistema...")
        break
    

        
