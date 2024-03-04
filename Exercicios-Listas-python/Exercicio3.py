# Exercício 3
# Crie um sistema de consulta de bônus dos funcionários
# Seu sistema deve:
# - Pegar o valor de vendas do funcinoário por meio de um input
# - Calcular o bônus do funcionário de acordo com a seguinte regra:
#       - Se o funcionário vendeu mais de 1000 unidades, ele ganha R$2 de bonus para cada unidade vendida
#       - Se o funcionário vendeu mais de 5000 unidades, ele ganha R$2 de bônus para cada unidade + um valor fixo de R$1000
#       - Se o funcionário vendeu menos de 1000 unidades, ele n

vendas = int(input("informe a quantidade de vendas realizadas: "))

if vendas > 1000 and vendas <= 4999:
    valor_final = vendas * 2 
    print("O bonus dete funcionario é de: {}".format(valor_final))
elif vendas > 5000:
    valor_final = (vendas * 2) + 1000
    print("O bonus dete funcionario é de: {}".format(valor_final))
elif vendas <= 1000:
    print("O funcionario não atingiu nenhuma meta!")
