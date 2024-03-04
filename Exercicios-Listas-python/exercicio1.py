# Exercício 1
# Crie um sistema de cadastro de produtos em uma lista de produtos
# Seu sistema deve:
# - Pegar o usuário qual produto vai ser cadastrado por meio de um input
# - Garantir que se o usuário escrever com letra maiúscula ou minúscula, o produto continua sendo o mesmo produto
# - Se o usuário inserir um produto que já existe na lista, o programa deve printar a mensagem "Produto já existente, tente novamente"
# - Se o usuário inserir um produto que não existe na lista, o programa deve inserir na lista, printar a mensagem Produto X cadastrado com sucesso e em seguida printar a lista completa

produtos = []


controlador = "sim"
while controlador == "sim":
    produto = input("Informe no nome do produto: ").lower()
    if produto in produtos:
        print("Produto ja cadastrado, tente novamente!")            
    else:
        produtos.append(produto)
        print("Produto {}, cadastrado com sucesso!\n{}".format(produto,produtos))
        controlador = input("Deseja continuar cadastrando?: ")
        



        
    


