"""
5.	Faça um algoritmo que receba a idade, a altura e o peso de 25 pessoas. Calcule e
      mostre:

•	A quantidade de pessoas com idade superior a 50 anos;
•	A média das alturas das pessoas com idade entre 10 e 20 anos;
•	A porcentagem de pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas.

"""


Pessoas_Mais_50 = 0
Soma_Alturas_10_20_Anos = 0
Total_Peso_inferior_40 = 0
Qtd_Pessoas_10_20_anos = 0



for i in range(3):
    Idade = int(input(f"INFORME A SUA IDADE: {i+1}: "))
    Peso = float(input(f"INFOME O SEU PESO: {i+1}: "))
    Altura = float(input(f"INFORME A SUA ALTURA: {i+1}: "))

    if(Idade > 50):
        Pessoas_Mais_50 +=1

    elif(Idade >= 10 and Idade <= 20):
        Soma_Alturas_10_20_Anos += Altura

    elif(Peso < 40):
        Total_Peso_inferior_40 += Peso



    Media_Altura_10_20_anos =  Soma_Alturas_10_20_Anos / Qtd_Pessoas_10_20_anos
    print(f"A média das alturas das pessoas com idades entra 10 e 20 anos é de: {Media_Altura_10_20_anos:.2f}")

Porcentagem_peso_inferior_40 = (Total_Peso_inferior_40 / 25) * 100
print(f"A porcentagem de peso para pessoas inferior á 40 quilos é de: {Porcentagem_peso_inferior_40:.2f}")

print(f"A quantidade de pessoas com idade superior a 50 é de: {Pessoas_Mais_50}")
