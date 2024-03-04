# Exercício 6 - Desafio
# No final da reunião de apresentação dos números, seu chefe perguntou:
# E se nos meses de 2023 que a gente vendeu menos do que 2022 a gente tivesse pelo menos empatado com 2022 (ou seja, se nos meses de 2023 em que as vendas foram menores do que o mesmo mês em 2022, o valor de vendas tivesse sido igual a 2022)
# Qual teria sido o nosso crescimento de 2023 frente a 2022?

vendas_22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000}
vendas_23 = {"jan": 17000, "fev": 15000, "mar": 17500, "abr": 16900, "mai": 16000, "jun": 18500}

for mes in vendas_23:
    valor22 = vendas_22[mes]
    valor23 = vendas_23[mes]
    percentual = (valor23/valor22) -1
    if percentual < 0:
        vendas_23[mes] = valor22

    print("Em {}, a variação do percentual é de: {:.1%}".format(mes, percentual))

total_23 = sum(vendas_23.values())
total_22 = sum(vendas_22.values())
crescimental_total = total_23 / total_22 - 1
print("O crescimento total foi de: {:.1%}".format(crescimental_total))

