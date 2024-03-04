""" Receber o salário de um funcionario e o seu percentual de aumento, calcular e mostrar de quanto é o aumento (encima do salário base) e de quanto é o novo salário"""

Salario = float(input("INFORME AQUI O SEU SALARIO ATUAL: "))
Percentual_Aumento = float(input("INFORME AQUI O PERCENTUAL DO SEU AUMENTO: "))
Valor_Aumento = (Salario * Percentual_Aumento) / 100
print(f"O percentual do seu aumento é de: {Valor_Aumento:.2f}")
Novo_Salario = Salario + Valor_Aumento
print(f"O seu novo salario é de: {Novo_Salario:.2f}")
