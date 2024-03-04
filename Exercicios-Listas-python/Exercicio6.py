#### 2. Faça um Programa que crie uma lista com as médias de cada aluno, imprima as médias de cada aluno e a quantidade de alunos com média maior que 7.

alunos = ["José", "Joana", "Maria", "Carla", "Mauricio", "Andre", "Tiago", "Enzo", "Amanda", "Alessandra"]
notas = [
    [10, 9, 8, 8],
    [9, 7, 6, 4],
    [10, 10, 10, 10],
    [5, 3, 10, 9],
    [7, 6, 6, 6],
    [7, 7, 8, 7],
    [7, 7, 7, 9],
    [8, 5, 6, 7],
    [10, 9, 7, 4],
    [10, 1, 3, 3],
]

medias = []

for i in range(len(notas)):
    media = sum((notas[i])) / 4
    if media >= 7.0:
        medias.append([alunos[i], media])
    else:
        print("Perdeu {}, nota: {}".format(alunos[i], media))
print(medias)


       
        
    