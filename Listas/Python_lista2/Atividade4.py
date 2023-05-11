"""
Uma empresa decide  dar um aumento de 30% com salários inferiores a R$ 500,00. Faça um algoritmo que receba o salário do funcionário
e mostre o valor do salário reajustado ou uma mensagem, caso o funcionário não tenha direito ao aumento.
"""
Salario_Base = float(input("INFORME AQUI O SEU SALARIO: "))
if(Salario_Base < 500):
    Aumento = (Salario_Base * 30) / 100 + Salario_Base
    print(f"O seu salario atual é de: {Aumento:.2f}")
else:
    print(f"Você não tem direito ao aumento. Salário atual: {Salario_Base:.2f}")