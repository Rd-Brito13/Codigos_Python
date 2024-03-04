# Exercício 2
# Agora edite o programa anterior para fazer com que, caso não exista o produto, o programa pergunte se o usuário quer cadastrar o produto
# Se ele responder sim, o programa deve pedir o nome do produto e o preco do produto e cadastrar no dicionário de preços
# Em seguida do cadastro bem sucedido, o programa deve printar o dicionário de precos atualizado

precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}


controlador = "sim"

while controlador == "sim":
    Nome_Produto = input("Informe o nome do Produto Desejado: ")
    Nome_Produto = Nome_Produto.lower()
    match Nome_Produto:
            case "celular":
                print("O valor é de {} é: {}".format(Nome_Produto,precos[Nome_Produto] ))
            case "camera":
                print("O valor é de {} é: {}".format(Nome_Produto,precos[Nome_Produto] ))
            case "fone de ouvido":
                print("O valor é de {} é: {}".format(Nome_Produto,precos[Nome_Produto] ))
            case "monitor":
                print("O valor é de {} é: {}".format(Nome_Produto,precos[Nome_Produto] ))
            case _:
               Cadastro = input("Produto não existe!, gostaria de cadastrar?: ")
               Cadastro = Cadastro.lower()
               if Cadastro == "sim":
                   Novo_Produto = input("Informe o Nome do Produto: ")
                   Novo_Produto = Novo_Produto.lower()
                   Valor_Novo_Produto = float(input("Informe o valor do Produto: "))
                   precos.update({Novo_Produto: Valor_Novo_Produto})
                   print("Cadastro Bem-Sucedido")
                   print(precos)
               else: 
                   print("Obrigado!")

    controlador = input("deseja continuar comprando?: ")
    controlador = controlador.lower()