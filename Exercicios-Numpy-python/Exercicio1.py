import numpy as np 

salarios_funcionarios = np.array([3000, 2500,3500 ,4000, 2000, 4500, 3800, 4800])
media_salarial = np.mean(salarios_funcionarios)

salarios = sum((salarios_funcionarios > media_salarial))
print(("A quantiade de funcionarios com salarios acima da média é de: {}".format(salarios)))
