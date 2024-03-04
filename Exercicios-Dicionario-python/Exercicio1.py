# Exercício 1
# Crie um sistema de consulta de preços
# Seu sistema deve:
# - Pedir para o usuário o nome de um produto
# - Caso o produto exista na lista de produtos, o programa deve retornar o preço do produto como resposta
#        - Ex: O produto celular custa R$1500
# - Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente

precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}


controlador = "Sim"
while controlador == "Sim":
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
                print("Produto não existe!")
    controlador = input("deseja continuar comprando?: ")
    

    


        

