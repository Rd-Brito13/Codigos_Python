"""
Faça um algoritmo que receba a idade e o peso de sete pessoas. Calcule e mostre:

•	a quantidade de pessoas com mais de 90 quilos;
•	a média das idades das sete pessoas.

"""

Qtd_Maior_90kg = 0
Soma_Idades = 0

for i in range(6):
    Idade = int(input(f"Pessoa {i+1}. Informe aqui a sua idade:"))
    Peso = float(input(f"Pessoa {i+1}. Informe aqui o seu peso: "))

    if(Peso > 90):
        Qtd_Maior_90kg += 1


    Soma_Idades += Idade
    Media_Idades = Soma_Idades / 7



print(f"A quantidade de pessoa acima de 90kg é de: {Qtd_Maior_90kg}")
print(f"A media entre as idades é de: {Media_Idades:.2f}")
