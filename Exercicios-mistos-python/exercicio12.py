"""
9. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""

Votos_Candidato_A = []
Votos_Candidato_B = []
Votos_Candidato_C = []

eleitores =  int(input("Informe o numero total de eleitores: "))

for eleitor in range(eleitores):
    candidato = int(input("informe em qual canditado deseja votar(1, 2 ou 3).: "))
    if candidato == 1:
        print("Voto confirmado")
        Votos_Candidato_A.append(candidato)
    elif candidato == 2:
        print("Voto confirmado")
        Votos_Candidato_B.append(candidato)
    elif candidato == 3:
        print("Voto confirmado")
        Votos_Candidato_C.append(candidato)


print("A quantidade de votos do Candidato A é de: {}. Candidato B: {}, Candidato C: {}".format(sum(Votos_Candidato_A), sum(Votos_Candidato_B), sum(Votos_Candidato_C)))




