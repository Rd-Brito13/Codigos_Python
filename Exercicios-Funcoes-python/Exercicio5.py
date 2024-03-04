"""
Escreva um programa que permita que um usuário crie uma lista de compras.
# O usuário deve ser capaz de adicionar itens, remover itens e visualizar a lista.
# 
# Estruture seu programa da seguinte forma:
# 
# 1. Crie uma lista vazia para armazenar os itens da lista de compras.
# 2. Crie um loop infinito que imprima um menu de opções ao usuário e permita que ele escolha uma opção.
# 3. Dentro do loop, use uma declaração if para executar a tarefa apropriada de acordo com a escolha do usuário.
# 4. Se o usuário escolher adicionar um item, solicite que ele digite o nome do item e adicione-o à lista.
# 5. Se o usuário escolher remover um item, solicite que ele digite o nome do item e remova-o da lista.
# 6. Se o usuário escolher ver a lista, mostre cada item da lista em sua própria linha.
# 7. Se o usuário escolher sair, encerre o loop usando break.

"""


lista_compras = []
controlador = 0
while controlador == 0:
    print("1 - Adicionar itens a lista de compra: \n2 - Remover itens a lista de compra:\n3 - Mostrar a situação da lista:\n4 - Encerrar o Programa: ")
    Decisao = int(input("Escolha uma opção: "))

    match Decisao:
        case 1: 
            Novo_Produto = input("Informe o Produto a ser adicionado: ").casefold().split()
            lista_compras.append(Novo_Produto)
            print(f"Produto: {Novo_Produto}. Adicionado com Sucesso!")
        case 2: 
            Remover = input("Informe o Produto existente na lista a ser removido: ").casefold().split()
            for Produto in lista_compras:
                if Produto == Remover:
                    lista_compras.remove(Remover)
                    print(f"Produto {Remover}, removido com sucesso!")
                else: 
                    print(f"Este produto: {Remover}, não consta na lista. Falha na remoção!")
        case 3: 
            print(lista_compras)
        case 4: 
            controlador += 1
            print("Programa encerrado!")


    