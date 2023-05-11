""" Faça um algoritmo para calcular e mostrar a que distância deve star um escada da
 parede. O usuário deve fornecer o tamanho da escada e a altura em que se deseja pregar o quadro. """

import math
Escada = float(input("INFORME O TAMANHO DA ESCADA: "))
Quadro = float(input("INFORME A ALTURA EM QUE SE DESEJA PEGAR O QUADRO: "))
Hipotenusa = (Escada ** (1/2))
Hipotenusa1 = Hipotenusa ** 2
Quadro2 = Quadro ** 2
Distancia = Quadro2 - Hipotenusa 

print(f"A distancia é de: {Distancia:.2f}")