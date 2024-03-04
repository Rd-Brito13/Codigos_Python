import numpy as np 

tempo_de_ciclo = np.array([5.5, 5.7, 5.9,6.0,5.8,5.6,5.7,7.2,4.8])
media = np.mean(tempo_de_ciclo)
print(f"media: {media}")
desvio_padrao = np.std(tempo_de_ciclo)
print(f"tempo do desvio padrão {desvio_padrao}")

condicao = (tempo_de_ciclo > media + 2 *desvio_padrao )|(tempo_de_ciclo < media - 2 * desvio_padrao)
anomalias = np.where(condicao)
print(f"Tempo desviado: {tempo_de_ciclo[anomalias]}")