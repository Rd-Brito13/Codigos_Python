"""
 Mude o programa de lista de compras para usar um dicionário ao invés de uma lista.
# O programa deve ter as mesmas funcionalidades, mas agora deve ser possível
# adicionar mais de uma unidade de um item na lista de compras. Ou seja, o dicionário
# deve armazenar o nome do item e a quantidade desejada pelo usuário. Por exemplo,
# se o usuário digitar "banana" e "2", o dicionário deve armazenar "banana" como chave
# e 2 como valor. A estrutura do dicionário ficaria assim: `{"banana": 2}`.
# 
# O programa deve permitir que o usuário adicione, remova e visualize o dicionário de compras.
# 
# Além disso, o programa deve mostrar uma mensagem de erro se o usuário tentar
# usar uma opção inválida do menu. Por exemplo, se o usuário digitar 5, o programa
# deve mostrar a mensagem "Opção inválida. Por favor, escolha uma opção válida." e
# mostrar o menu novamente. Além disso, o programa deve ser *case insensitive*, ou seja,
# "Maçã" e "maçã" devem ser considerados o mesmo item.

"""

lista_compras = {}
lista_items = []
lista_quantidades = []
controlador = "sim"


while controlador == "sim":
    print("1 - Adicionar itens e quantidade a lista de compra: \n2 - Remover itens a lista de compra:\n3 - Mostrar a situação da lista:\n4 - Encerrar o Programa: ")
    Decisao = int(input("Informe a opção desejada: "))
    if Decisao >= 5:
        print("Opção invalida, tente novamente: ")
        
    else:

        match Decisao:
            case 1:
                Item = str(input("Informe o item que deseja adicionar: ")).casefold()
                Quantidade = input("Informe a quantidade que deseja do item: " ).casefold()
                lista_items.append(Item)
                lista_quantidades.append(Quantidade)
                print(f"Item: {Item}, e Quantidade: {Quantidade}, adicionado com sucesso!")
                lista_compras = dict(zip(lista_items,lista_quantidades))
            case 2: 
                Remover = str(input("Informe o nome do item que deseja remover: ")).casefold()
                if Remover in lista_compras:
                    lista_compras.pop(Remover)
                    print(f"Produto: {Remover} Removido com Sucesso!")

            case 3:
                print(lista_compras)
            case 4:
                controlador = input("Desejar continuar o programa: ")






