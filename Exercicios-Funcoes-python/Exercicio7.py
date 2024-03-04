"""
Mantenha o programa da lista de compras com dicionário, mas agora use funções para organizar o código. Crie funções para cada uma das opções do menu: `adicionar_item`, `remover_item` e `ver_lista`. Crie também uma função para mostrar o menu. O programa deve continuar funcionando da mesma forma, mas agora o código deve estar organizado em funções.
"""

def Adicionar(lista_objetos,lista_quanti,lista_final):
    Item = str(input("Informe o item para adicionar na lista: "))
    Quantidade = input("Informe a quantidade de item: ")
    Item.casefold()
    Quantidade.casefold()
    lista_objetos.append(Item)
    lista_quanti.append(Quantidade)
    lista_final.update(dict(zip(lista_objetos,lista_quanti)))
    return print("Item: {}, e Quantidade: {}, adicionado com sucesso!".format(Item,Quantidade))

def Remover(lista_final):
    remove = input("Informe no nome do item que deseja remover: ").casefold()
    if remove in lista_final:
        lista_final.pop(remove)
        print(f"Item: {remove}, removido com sucesso!")
    else:
        print(f"Este item: {remove}, não existe na lista!")

def Exibir(Lista):
    return print(Lista)


    
    



lista_compras = {}
lista_items = []
lista_quantidades = []
controlador = "não"
while controlador == "não":
    print("1 - Adicionar itens e quantidade a lista de compra: \n2 - Remover itens a lista de compra:\n3 - Mostrar a situação da lista:\n4 - Encerrar o Programa: ")
    Decisao = int(input("Informe a opção desejada: "))
    if Decisao >= 5:
        print("Opção invalida, tente novamente: ")
        
    else:
        match Decisao:
            case 1:
                Adicionar(lista_items,lista_quantidades,lista_compras)
            case 2:
                Remover(lista_compras)
            case 3:
                Exibir(lista_compras)
            case 4:
                controlador = input("Deseja encerrar o programa?: ").casefold()
                if "sim" in controlador:
                    print("Programa encerrado!")
                else:
                    print("Continue!")

