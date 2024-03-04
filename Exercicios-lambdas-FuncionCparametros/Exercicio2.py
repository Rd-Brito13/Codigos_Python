"Criada uma função para retornar o valor e somar com o aumento de 30%, feito de duas maneira, por uma função definida e por uma expressão lambda"

preco_tecnologia = {'notebook asus': 2450, 'iphone': 4500, 'samsung galaxy': 3000, 'tv samsung': 1000, 'ps5': 3000, 'tablet': 1000, 'notebook dell': 3000, 'ipad': 3000, 'tv philco': 800, 'notebook hp': 1700}


def calcular_preco(preco):
    return preco * (1.3)

lista_preco = list(map(calcular_preco, preco_tecnologia.values()))
print(lista_preco)


lista_preco2 = list(map(lambda preco: preco * 1.3, preco_tecnologia.values()))
print(lista_preco2)

