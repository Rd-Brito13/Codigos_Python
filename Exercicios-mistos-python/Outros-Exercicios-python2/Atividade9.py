"""
Faça um algoritmo que receba a idade e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostre em qual grupo de risco essa pessoa se encaixa.


"""

Idade = int(input("INFORME AQUI A SUA IDADE: "))
Peso = float(input("INFORME AQUI O SEU PESO: "))

if(Idade < 20 and Peso <= 60):
    print("9")
elif(Idade >= 20 and Idade <= 50 and Peso <= 60):
    print("6")
elif(Idade > 50 and Peso <= 60):
    print("3")
elif(Idade < 20 and Peso >= 60 and Peso <= 90):
    print("8")
elif(Idade  >= 20 and Idade <= 50 and Peso >= 60 and Peso <= 90 ):
    print("5")
elif(Idade > 50 and Peso >= 60 and Peso <= 90):
    print("2")
elif(Idade < 20 and Peso > 90):
    print("7")
elif(Idade >= 20 and Idade <= 50 and Peso > 90):
    print("4")
elif(Idade > 50 and Peso > 90):
    print("1")

