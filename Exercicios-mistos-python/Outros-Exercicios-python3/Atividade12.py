"""
12.	Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados de idade, sexo (M/F) e salário. Faça um algoritmo que calcule e mostre:

•	a média  dos salários do grupo;
•	a maior e menor idade do grupo;
•	a quantidade de mulheres com salário até R$ 200,00;
•	a idade e o sexo da pessoa que possui o menor salário

"""
def Calcular_Estaticias():
    Total_Pessoas = 0
    Soma_Salarios = 0
    Maior_Idade = float('-inf')
    Menor_Idade = float('inf')
    Cout_Mulheres_Salario_ate = 0
    Menor_Salario = float('-inf')
    Menor_Salario_Idade = 0
    Menor_salario_Sexo = ''

    while True:
        Idade = int(input("INFORME A SUA IDADE (OU -1 PARA ENCERRAR): "))
        if(Idade == -1):
            break

        Sexo = str(input("INFORME O SEU SEXO (M/F): "))
        Salario = float(input("INFORME O SEU SALARIO: "))

        Total_Pessoas += 1
        Soma_Salarios += Salario

        if(Idade > Maior_Idade):
            Maior_Idade = Idade

        if(Idade < Menor_Idade):
            Menor_Idade = Idade

        if(Sexo == 'F' and Salario <= 200):
            Cout_Mulheres_Salario_ate += 1

        if (Salario < Menor_Salario):
            Menor_Salario = Salario
            Menor_Salario_Idade = Idade
            Menor_salario_Sexo = Sexo

        Media_Salario_Total =  Soma_Salarios / Total_Pessoas

        print("Média dos salários do grupo:", Media_Salario_Total)
        print("Maior idade do grupo:", Maior_Idade)
        print("Menor idade do grupo:", Menor_Idade)
        print("Quantidade de mulheres com salário até R$ 200,00:", Cout_Mulheres_Salario_ate)
        print("Pessoa com menor salário: Idade:", Menor_Salario_Idade, "Sexo:", Menor_salario_Sexo)

Calcular_Estaticias()




