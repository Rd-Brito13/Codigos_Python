"Um sistema de vendas deve ser criado e deverá coletar 2 inputs do usuário, o nome do produto e depois a quantidade do produto e adicionar eles a uma lista, o programa deve continuar até que o usuário decida finalizar o programa, ao final do programa deve ser exibido a lista dos produtos e quantidades cadastradas"


lista_produtos_quantidades = []
Decisao = input("Deseja fazer o cadastro dos itens? (sim ou não): ")
while Decisao != "não":
    produtos = input("informe o nome do produto: ")
    quantidade = int(input("informe a quantidade desejada do produto: "))
    lista_produtos_quantidades.append([produtos,quantidade])
    Decisao = input("Deseja fazer o cadastro dos itens? (sim ou não): ")

print(lista_produtos_quantidades)


