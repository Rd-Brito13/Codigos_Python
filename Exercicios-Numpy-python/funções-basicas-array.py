import numpy as np 
#criando o array e definindo os valores
quantidades  = np.array(range(10, 16))
precos_unitarios = np.array([20,50,97,69,31,51])
#Esta função, utiliza de dois arrays separados, para retornar a multiplicação de cada valor e a soma dos arrays
soma_valor_unitario = np.dot(quantidades,precos_unitarios)
print("A soma do valores uniaários é de: {}".format(soma_valor_unitario))

#passando esses valores para um novo array e multiplicando cada valor antigo por 10% de si mesmo e somando aos valores antigos, por fim, exibindo este array
novos_precos = precos_unitarios * 1.1
print(f"Os novos precos são: {novos_precos}")

#extraindo o maior e menor valor presente no array
maior_valor = np.max(precos_unitarios)
print(f"O maior valor é: {maior_valor}")
menor_valor = np.min(precos_unitarios)
print(f"O menor valor é: {menor_valor}")

#ordenando o array em ordem crescente
precos_crescente = np.sort(precos_unitarios)
print(precos_crescente)

#Somando todos os valores do array e atribuindo esta soma a uma nova variavel e exibindo-os
soma_precos = np.sum(precos_unitarios)
print(f"A soma dos preços é: {soma_precos}")

#extraindo a media do array
media_precos = np.mean(precos_unitarios)
print(f"A media do array é: {media_precos}")


