
""" Receber o Salário d eum funcionário, calcular e mostrar o novo salário, com aumento de 25% encima do salário base"""

Salario = float(input("Informe aqui o seu salario atual: "))
Novo_Salario = (Salario * 25) / 100 + Salario
print(f"O seu novo salario é de: {Novo_Salario:.2f}")
