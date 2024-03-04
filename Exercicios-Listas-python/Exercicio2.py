#  Exercício 2
# Crie um sistema de consulta de preços
# Seu sistema deve:
# - Pedir para o usuário o nome de um produto
# - Caso o produto exista na lista de produtos, o programa deve retornar o preço do produto como resposta
#        - Ex: O produto celular custa R$1500
# - Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente


produtos = ["polly", "max steel", "kamem rider", "lego", "barbie"]
precos = [150, 100, 190, 295, 20]

controlador = "sim"
while controlador == "sim":

    nome_produto = input("Informe o nome do produto desejado: ").lower()
  
    if nome_produto in produtos:
        indice  = produtos.index(nome_produto)
        preco = precos[indice]
        print("O produto {} tem um valor de {}".format(nome_produto, preco))
    else: 
        print("O produto {}, não consta na lista!".format(nome_produto))
    controlador = input("deseja continuar?: ")