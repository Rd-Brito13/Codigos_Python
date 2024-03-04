import numpy as np 

#criando um gerador de numero aleatórios 

gerador = np.random.default_rng()
print(gerador)
#A função random(), por padrão sempre irá gerar numeros entre 0 e 1, multiplicando essa função por algum numero desejado, aumentará as possibilidades, e sempre irá gerar numeros floats.
numero_aleatorio = gerador.random() * 10
print(numero_aleatorio)
#É possivel gerar arrays  preenchidos pela função random(), a parametragem da função define quantos numeros serão gerados, e também é possivel multiplicar a função parar abrir o leque de possibilidades, como foi feito acima.
array_aleatorio = gerador.random(3) * 10
print(array_aleatorio)
"""
Supondo que voce seja um analista de vendas em uma empresa e queira entender melhor o desempenho das vendas de um produto especifico. No entanto, você não tem acesso aos dados reais de vendas de um certo produto, então você decide gerar alguns dados de vendas aleatórios para realizar sua análise.

Gere dados de vendas falsos para 30 dias
Vamos supor que as vendas de um produto podem variar de 50 a 200 por dia
Pode definir uma seed para garantir que os resultados sejam reproduziveis 
"""
#Aqui, está sendo reaproveitada a variavel que foi definida como gerador no começo do código, o parametro "seed = 0": com este parametro, significa que, eu posso usar qualquer numero inteiro para preencher o parametro e a pessoa que utilizar esta mesma "seed", irá manter o mesmo padrão de preenchimento de valores no array, seed = 0: irá preencher o array com uma sequencia padrão do 0, e assim por diante.
gerador = np.random.default_rng(seed=0)
#Aqui, está sendo utilizado o mestmo gerador que definimos no começo, e estamos utilizando a função integers(), está função retorna somente numeros inteiros, o parametro "low = 50": define que, os valores gerados será a partir de 50 e o parametro "high = 200": define que os valores serão até 200, e o parametro "size = 30": define que, serão gerados somente 30 numeros entre o low e high.
dados_vendas = gerador.integers(low=50, high=200, size=30)
print(dados_vendas)

#a função do numpy, "argmax()" e "argmin()", retorna o indice de um item do array, baseado na maior ou menor valor encontrado no array.
#Dia com a maior quantidade de vendas.
print("Dia com mais vendas:  {}".format( np.argmax(dados_vendas) + 1))
#Dia com a menor quantidade de vendas.
print("Dia com menos vendas:  {}".format( np.argmin(dados_vendas) + 1))

#Media de vendas
print("A media de vendas dos produtos durante o mês foram de: {}".format(np.mean(dados_vendas)))
