"""
# ## Previsão de vendas

# ### Primeira versão da previsão de vendas

# Escreva um programa que preveja as vendas totais para cada produto em uma empresa.
# O usuário deve digitar o nome do produto, as vendas do mês atual e a taxa de crescimento,
# e o programa deve calcular as vendas previstas para o próximo mês.
# 
# Estruture seu programa da seguinte forma:
# 
# 1. Crie um dicionário vazio para armazenar as previsões de vendas.
# 2. Crie um loop infinito que solicite ao usuário o nome do produto, as vendas do mês atual e a taxa de crescimento.
# 3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
# 4. Se o usuário digitar 'sair', encerre o loop usando break.
# 5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular as vendas previstas e adicione-as ao dicionário.
# 6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar as previsões de vendas para cada produto.
# 
# Exemplo de saída:
# 
# ```
# Digite o nome do produto (ou 'sair' para sair): iphone
# Digite as vendas do mês atual: 10000
# Digite a taxa de crescimento (%): 10
# Digite o nome do produto (ou 'sair' para sair): capinha para iphone
# Digite as vendas do mês atual: 200
# Digite a taxa de crescimento (%): 20
# Digite o nome do produto (ou 'sair' para sair): sair
# iphone: Previsão de vendas do próximo mês = R$ 11000.00
# capinha para iphone: Previsão de vendas do próximo mês = R$ 240.00
# ```
# 

"""

previsoes_vendas = {}

controlador = "não"
while controlador == "não":
    produto = input("informe o nome do produto: ").casefold()
    if "sair" in produto:
        break
    else: 
        venda_produto = float(input("Informe a quantidade de vendas do produto especificado: "))
        taxa_crescimento_produto = float(input("Informe a taxa de crescimento do produtdo especificado: "))
        vendas_previstas = venda_produto *(1 + taxa_crescimento_produto / 100)
        previsoes_vendas[produto] = vendas_previstas 


for key,values in previsoes_vendas.items():
    print(f"o Produto: {key}, tem uma previsão de venda de: {values:.2f}")