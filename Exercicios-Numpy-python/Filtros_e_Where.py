import numpy as np
#Criando o gerador de numeros aleatórios
base_salarios = np.random.default_rng(seed=55)
#Criando o array, com o gerador e definindo os valores entra 1000 e 5000, introduzindo 10 valores no array
salarios = base_salarios.integers(low = 1000, high = 5000, size = 10)
print(salarios)
#Media salarial
media_salarial = np.mean(salarios)
print("A media salarial é de: {}".format(media_salarial))

#A função do numpy, where(), é utilizada para filtrar dados de um array, por padrão, faz a condifional (if, else, maior, menor..., e retorna um array com os indices aceitos pela condição )
#funcionarios acima da media
funcionarios_acima = np.where(salarios > media_salarial)
#Desta maneira, está retornando o padrão do where, está retornando um array com os indices aceitos pela condição
print(funcionarios_acima)
#é possivel, passar um array de indices para que seja printado o valor de cada indice, desta forma, estamos fazendo o np.where() e printando  array contendo os salários e passando pra ele os indices que devem ser retornados dele mesmo.
print(salarios[funcionarios_acima])
#Também é possivel retornar diretamente no print, sem a necessidade de utilizar da função where, somente printando o array de salarios e exigindo que retorne somente os valores baseado na condição imposta e será retornado um array com os valores permitidos pela condição, desta seguinte maneira.
print(salarios[salarios > media_salarial])

#Utilizando do if e do else dentro do where(), com esta linha abaixo, significa que, eu posso passar o tratamento para saber qual valor dentro do array é maior que a media salarial pré-estabelecida, e estou retornando as strings, "acima da média" caso seja verdadeira a condição e "abaixo da média", caso seja falsa a condição.
print(np.where(salarios > media_salarial, "acima da média", "abaixo da média"))

#Utilizando o mesmo exemplo acima, agora, será utilizado de maneira diferente.
salarios_bonificado = np.where(salarios < media_salarial, salarios * 1.5, "Não será bonificado")
print(salarios)
print(salarios_bonificado)

#Utilizando do mesmo exemplo, agora, com duas condições e utilizando o operador "and", no numpy é utilizando o simbolo de "&".
salarios_ajustados = np.where((salarios >= 3000) & (salarios <= 4500), salarios * 1.5, "Não será bonificado")
print(salarios_ajustados)
#Utilizando o mesmo exemplo, agora, com duas condições e utilizando o operador "or", no numpy é simbolizado por "|".
vizualizacao_salarial = np.where((salarios < 3000) | (salarios > 5000))
print(salarios[vizualizacao_salarial])
