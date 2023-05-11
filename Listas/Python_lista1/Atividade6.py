"""  algoritmo que receba o salário-base de um funcionário, calcula e mostra o seu salário a receber,
sabendo-se que esse funcionário tem gratificação de R$ 50,00 e paga imposto de 10% sobre o salário-base."""

Salario_Base = float(input("INFORME AQUI O SEU SALARIO-BASE: "))
Imposto = (Salario_Base * 10) / 100
Salario_Liquido = (Salario_Base + 50) - Imposto

print(f"O seu salario à receber é de: {Salario_Liquido:.2f}")
