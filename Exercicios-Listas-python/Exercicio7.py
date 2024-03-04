#### 3. Foram anotadas as idades e salários de 30 funcionários. Faça um programa que determine quantos funcionários com mais de 25 anos possuem salário inferior à média de todos os salários.

idades = [35,32,50,33,48,50,33,48,22,49,35,38,20,47,49,48,34,21,48,44,48,30,25,42,42,23,25,23,38,35]
salarios = [3739,2219,3554,3978,4014,3270,4792,3879,2981,2384,4826,2460,3680,4318,1872,1770,4640,3929,3295,1729,3965,4267,4007,1916,2987,2943,3852,4543,2055,1730]
contador = 1
media_salarios = (sum(salarios)) / len(salarios)

for i in range(len(idades)):
    if idades[i] > 25 and salarios[i] < media_salarios:
        print("A quantidade de funcionarios é de: {}".format(contador))
        contador += 1
        

