"""algoritmo que receba o valor de um
depósito e o valor da taxa de juros, calcule e mostre o valor do rendimento e o valor total depois do rendimento.
"""

Deposito = float(input("INFORME AQUI O VALOR DO DEPOSITO: "))
Taxa_Juros = float(input("INFORME AQUI O VALOR DA TAXA DE JUROS: "))
Redimento = (Deposito * Taxa_Juros) / 30
print(f"O valor do Rendimento é de: {Redimento:.2f}")
Deposito = Redimento + Deposito
print(f"O valor Depois do rendimento é de: {Deposito:.2f}")