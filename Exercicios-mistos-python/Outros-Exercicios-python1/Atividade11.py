"""
faça um algoritmo que receba o número de horas trabalhadas e o valor do salário
mínimo. Calcule e mostre o salário a receber seguindo as regras abaixo:

a) a hora trabalhada vale a metade do salário mínimo;
b) o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada;
c) o imposto equivale a 3% do salário bruto;
d) o salário a receber equivale ao salário bruto menos o imposto;
"""
Salario_Minimo = float(input("INFORME O VALOR DO SEU SALARIO MINIMO: "))
Horas_Trabalhadas = float(input("INFORME A QUANTIDADE DE HORAS TRABALHADAS NO MÊS: "))
Hora_TRABALHADA = Salario_Minimo / 2
print(f"O VALOR DE CADA HORA TRABALHADA É DE: {Hora_TRABALHADA:.2f}")
Salario_Bruto =  Horas_Trabalhadas * Hora_TRABALHADA
print(f"O SALÁRIO BRUTO É DE: {Salario_Bruto:.2f}")
Imposto = (Salario_Bruto * 3) / 100
print(f"O IMPOSTO É DE: {Imposto:.2f}")
Salario_Liquido = Salario_Bruto - Imposto
print(f"O SALÁRIO A RECEBER É DE: {Salario_Liquido:.2f}")
