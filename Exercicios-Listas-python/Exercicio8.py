"""
#### 5. As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
<pre>Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
. Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;
. O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; 

Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. O programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:</pre>
<pre>
O salário de cada funcionário, juntamente com o valor do abono;
O número total de funcionário processados;
O valor total a ser gasto com o pagamento do abono;
O número de funcionário que receberá o valor mínimo de 100 reais;
O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos.
<pre>
Projeção de Gastos com Abono
============================ 

"""

lista_salarios = [1000, 300, 500, 200, 1500, 3000, 3400, 5000, 7000, 2000, 600, 800, 250, 1500, 20000]

abonos = []
print(" Salários - Abonos")

conta_minima = 0

for salario in lista_salarios:
    abono = salario * 0.2
    if abono < 100:
        abono = 100
    abonos.append(abono)
    if abono == 100:
        conta_minima += 1
    print(f"R$ {salario} - R$ {abono}")

total_func = len(lista_salarios)
total_abono = sum(abonos)
maior_abono = max(abonos)
print("O total de funcionarios participando é de: {}".format(total_func))
print("O total gasto com abono é de: {}".format(total_abono))
print("O maior abono é de: {}".format(maior_abono))