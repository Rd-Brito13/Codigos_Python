"Criando um gerador de funções, determinando a função calcular_imposto e requisitando uma parametragem chamada de imposto, e trazendo o retorno da função uma expressão lambda para, ter o parametro preco, satisfeito e multiplicar e somar o valor do preco vezes o imposto"

def calcular_imposto(imposto):
    return lambda preco: preco* (1+imposto )

calcular_taxa_produto = calcular_imposto(0.1)
calcular_taxa_servico = calcular_imposto(0.15)
calcular_taxa_royalties = calcular_imposto(0.25)

print(calcular_taxa_produto(100))
print(calcular_taxa_servico(358))
print(calcular_taxa_royalties(250))