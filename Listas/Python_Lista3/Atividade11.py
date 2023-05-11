"""
11.	A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e o número de filhos. A prefeitura deseja saber:

•	a média do salário da população;
•	a média do número de filhos;
•	o maior salário;
•	a percentagem de pessoas com salários até R$ 150,00.

"""
Soma_Salario = 0
Media_Salario = 0
Soma_Filhos = 0
Media_Filhos = 0
Maior_Salario = 0
Porcentagem_Pessoa_Salario = 0

for i in range(0, 5, 1):
      Salario = float(input(f"Familia{i+1}.INFORME O SEU SALARIO: "))
      Qtd_Filhos= int(input(f"Familia{i+1}.INFORME Q QUATIDADE DE FILHOS: "))

      Soma_Salario += Salario
      Media_Salario = Soma_Salario / 5
      Soma_Filhos += Qtd_Filhos
      Media_Filhos = Soma_Filhos / 5
      Maior_Salario = max(Salario)







print(f"o maior salario é: {Maior_Salario}")

print(f"A media salarial da população é de: {Media_Salario:.2f}")
print(f"A media de filhos da população é de: {Qtd_Filhos:.2f}")
