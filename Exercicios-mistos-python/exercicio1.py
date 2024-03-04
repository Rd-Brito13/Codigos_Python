"crie um programa que funcione como registro de vendas de uma empresa. Nele a pessoa deve inserir o nome do produto e o produto deve ser adicionado a lista de venda. Enquanto o usuário não encerrar o programa, significa que ele está registrando novos produtos, então o programa deve continuar."

nome_produto = input("informe o nome do produto que deseja adicionar: ")
lista_produtos = []

while nome_produto != "":
    lista_produtos.append(nome_produto)
    nome_produto = input("informe o nome do produto que deseja adicionar: ")

    
print(lista_produtos)


