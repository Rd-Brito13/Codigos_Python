import numpy as np
import time


#criando um array np.array = função utilizada para a criação de um array no numpy
array = np.array([1,2,3,4,5,6])
#definindo que o array original irá receber a si mesmo, com  +1 somando a cada item

#Comparando o tempo para necessario para fazer a soma com a função  SUM do python e a função SUM do numpay
lista =  list(range(1, 10_000_001))
array = np.array(range(1,10_000_001))

inicio = time.time()
soma_lista = sum(lista)
fim = time.time()
print("O tempo para somar todos os valores com a função nativa python é: {}".format(fim - inicio))

inicio = time.time()
#np.sum() = Função numpy utilizado para somar os valores do array
soma_array = np.sum(array)
fim = time.time()
print("O tempo para somar todos os valores com a função sum do numpay é: {}".format(fim - inicio))

