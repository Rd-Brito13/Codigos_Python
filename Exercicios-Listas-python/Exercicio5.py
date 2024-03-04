#### 1. Faça um Programa que leia as vendas dos vendedores, mostre a venda de cada vendedor com o seu nome e a média de vendas. 

vendas = [1000, 1500, 1200, 1300]
vendedores = ["Fulano", "Beltrano", "Ciclano", "Lira"]

for i in range(len(vendas)):
    print("O vendedor {}, tem uma quandidade de vendas de: {}".format(vendedores[i], vendas[i]))

media = sum(vendas) / len(vendedores)
print("A média é de: {}".format(media))
