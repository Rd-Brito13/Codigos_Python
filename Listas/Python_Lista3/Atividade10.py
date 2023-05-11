"""
Faça um algoritmo que receba várias idades e que calcule e mostre a média das idades digitadas. Finalize digitando idade igual a zero.
"""
Soma_Idades = 0

Media_Idades = 0
for i in range(10):
    Idade = int(input(f"Pessoa{i+1}. DIGITE A SUA IDADE: "))

    Soma_Idades += Idade
    Media_Idades = Soma_Idades / 10

print(f"A media entre as idades é de: {Media_Idades:.2f}")
