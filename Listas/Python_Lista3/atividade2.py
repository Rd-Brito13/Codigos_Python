"""
Faça um algoritmo que receba a idade de dez pessoas e que calcule e mostre a quantidade de pessoas com idade maior ou igual a 18 anos.


"""

contagem = 0
menor_idade = 0

for idade in range(10):
    idade = int(input("Infome a sua idade: "))

    if (idade >= 18):
        contagem += 1


    elif(idade < 18):
        menor_idade += 1

print(f"Quantidade de pessoas maiores de idade é de: {contagem}")
print(f"Quantidade de pessoas menor de idade é de: {menor_idade}")





