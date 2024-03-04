"""7. Faça um programa que peça para o usuário inserir o faturamento dos últimos 5 meses (individualmente) e informe o faturamento total (soma) e o faturamento médio por mês (média)."""

lista_faturamentos = []

for i in range(5):
    faturamento = float(input("Informe o valor do faturamento: "))
    lista_faturamentos.append(faturamento)
    print("operação realizada com sucesso!")

print("O valor do faturamento total é de: {}".format(sum(lista_faturamentos)))
print("A Média do faturamento é de: {}".format(sum(lista_faturamentos) / len(lista_faturamentos)))

