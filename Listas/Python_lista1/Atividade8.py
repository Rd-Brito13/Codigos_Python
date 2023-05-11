"""algoritmo que receba um número positivo e maior que zero, calcule e mostre:

        a) o número digitado ao quadrado;
        b) o número digitado ao cubo;
        c) a raiz quadrada do número digitado;
        d) a raiz cúbica do número digitado;
"""

Numero = float(input("Digite aqui um numero positivo maior que zero: "))
Numero_Quadrado = Numero ** 2
print(f"o Numero ao Quadrado é: {Numero_Quadrado:.2f}")
Numero_Cubo = Numero ** 3
print(f"o NUmero ao CUbo é: {Numero_Cubo:.2f}")
Raiz_Quadrada = Numero ** (1/2)
print(f"a Raiz Quadrada do numero é: {Raiz_Quadrada:.2f}")
Raiz_Cubica = Numero ** (1/3)
print(f"A Raiz Cubica do numero é: {Raiz_Cubica:.2f}")
