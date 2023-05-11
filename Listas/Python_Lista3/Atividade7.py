"""
7.	Faça um algoritmo que receba 10 números e que calcule e mostre a quantidade de números entre 30 e 90.
"""

Quantidade_Numero = 0

for i in range (10):
    Numero = float(input(f"{i+1}: Informe o numero desejado: "))

    if(Numero >= 30 and Numero <= 90):
        Quantidade_Numero += 1

print(f"A quantidade de numeros entre 30 e 90 é de: {Quantidade_Numero}")