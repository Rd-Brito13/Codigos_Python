"""
 ### Segunda versão da previsão de vendas
# 

# Mantenha a mesma funcionalidade do programa anterior, mas agora valide a entrada do usuário.
# Se o usuário digitar um valor inválido para vendas ou taxa de crescimento, mostre a mensagem
# "Entrada inválida. Por favor, digite um número para vendas e taxa de crescimento." e peça
# para o usuário digitar novamente. Tal validação deve ser feita usando try/except.
# 

"""

previsoes_vendas = {}

controlador = "não"
while controlador == "não":
    produto = input("informe o nome do produto: ").casefold()
    if "sair" in produto:
        break
    else: 
        try:
            venda_produto = float(input("Informe a quantidade de vendas do produto especificado: "))
            taxa_crescimento_produto = float(input("Informe a taxa de crescimento do produtdo especificado: "))
            vendas_previstas = venda_produto *(1 + taxa_crescimento_produto / 100)
            previsoes_vendas[produto] = vendas_previstas 
            
        except ValueError:
            print("Valores invalidos, digite apenas valores numericos")
            
for key,values in previsoes_vendas.items():
    print(f"o Produto: {key}, tem uma previsão de venda de: {values:.2f}")