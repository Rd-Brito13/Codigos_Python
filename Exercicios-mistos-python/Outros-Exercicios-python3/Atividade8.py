"""
Faça um algoritmo que receba dez números, calcule e mostre a soma dos números pares e a soma dos números primos.
"""

Numero_Par = 0
Numero_Impar = 0

for i in range(10):
    NUmeros = int(input(f"{i+1}: INFORME NUMEROS PARES E IMPARS: "))
    if(NUmeros %2 == 0):
        Numero_Par += 1
    else:
        Numero_Impar += 1

print(f"A QUANTIDADEDE NUMERO PAR: {Numero_Par}")

print(f"A QUANTIDADE DE NUMERO IMPAR {Numero_Impar}")