""" recebe o salário-base de um funcionário, calcula e mostra o salário a receber,
sabendo-se que esse funcionário tem gratificação de 5% sobre o salário-base e paga o imposto de 7% sobre o salário-base."""

Salario_Base = float(input("INFORME AQUI O SEU SALARIO_BASE: "))
Gratificacao  = (Salario_Base * 5) / 100 + Salario_Base
Imposto =  Gratificacao - (Salario_Base * 7) / 100
print(f"o seu salario liquido é de: {Imposto:.2f}")
