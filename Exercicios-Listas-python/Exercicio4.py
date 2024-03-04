#Exercício 4
# Crie um programa que consiga descobrir qual dos vendedores vendeu mais
# As vendas dos vendedores são listas com a quantidade vendida por cada vendedor

vendas = [
    [10, 20, 100, 80, 90, 100, 20, 30, 44, 55, 33, 34, 100, 90, 80, 39, 87, 45, 50, 50, 50, 50, 40, 30, 3, 93, 39, 49, 88],    
    [100, 1, 1, 4, 5, 90, 100, 20, 4, 5, 100, 100, 100, 100, 100, 93, 20, 15, 40, 90, 90, 90, 90, 90, 90, 33, 22, 44, 43, 34],
]

vendas1 = sum(vendas[0])
vendas2 = sum(vendas[1])

if vendas1 > vendas2:
    print("O vendedor 1 é o vencedor!, com a quantidade de vendas de: {}".format(vendas1))
else: 
    print("O vendedor 2 é o vencedor!, com a quantidade de vendas de: {}".format(vendas2))
    