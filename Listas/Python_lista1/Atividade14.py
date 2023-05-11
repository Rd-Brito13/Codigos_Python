"""Sabe-se que o quilowatt de energia custa um quinto do salário mínimo. Faça
um algoritmo que receba o valor do salário mínimo e a quantidade de quilowatts consumida por uma residência. Calcule e mostre:"""

Salario_Minimo = float(input("INFORME O VALOR DO SALARIO MINIMO: "))
Quilowatt = float(input("INFORME A QUANTIDADE DE QUILOWATT: "))
Valor_Quilo = (Salario_Minimo / 5) * 1
print(f"O VALOR EM REAIS DE CADA QUILOWATT É DE: {Valor_Quilo:.2f}")
Valor_Pago = Quilowatt * Valor_Quilo
print(f"O VALOR EM REAIS PAGO É DE: {Valor_Pago:.2f}")
Valor_Desconto =  Valor_Pago - ((Valor_Pago * 15) / 100)
print(f"O VALOR COM O DESCONTO É DE: {Valor_Desconto:.2f}")

