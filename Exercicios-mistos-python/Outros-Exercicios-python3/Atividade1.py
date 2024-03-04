"""
Faça um algoritmo que verifique e mostre os números entre 1000 e 2000 (inclusive) que, quando divididos por 11, produzam resto igual a 5.

"""

for i in range(1000, 2001, 1):
    if i % 11 == 5:
        print(i)
