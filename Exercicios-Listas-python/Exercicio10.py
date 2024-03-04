"""
#### 7. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe \\$200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de \\$3000 em uma semana recebe \\$200 mais 9 por cento de \\$3000, ou seja, um total de \\$470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
<pre>
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
</pre>

Existem várias formas de fazer. Faça primeiro da forma que parecer mais intuitiva para você.

Em seguida, caso queira um desafio:
Desafio: Crie uma forma para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
"""

vendas = [1000, 2000, 3000, 4000, 5000, 6000, 5500, 4500, 3600]
faixas = []
menores_que_mil = 0
tamanho_faixas = 100
qtde_faixas = 9

for venda in vendas:
    bonus = venda * 0.09
    salario = 200 + bonus
    print(salario)
    faixa = int(bonus / tamanho_faixas) + 1
    faixas.append(faixa)
    
for i in range(qtde_faixas-1):
    print(f'Entre {i*100 + 200} e {i*100 + 299}:', faixas.count(i+1))
    menores_que_mil += faixas.count(i+1)
    
print('Mais que mil:', len(vendas) - menores_que_mil)