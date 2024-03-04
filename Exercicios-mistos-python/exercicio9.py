"""
6. Faça um programa que peça para o usuário inserir o faturamento dos últimos 5 meses (individualmente) e informe o maior faturamento
"""

lista_faturamentos = []
controlador = 0

while controlador < 5 :
    mes = input("informe o mês: ")
    faturamentos = float(input(f"informe o faturamento do mês de {mes} de: "))
    lista_faturamentos.append([mes,faturamentos])
    print("adicionado com sucesso!")
    controlador += 1

for mes, faturamento in range(lista_faturamentos):
    if max(faturamento):
        print(mes, faturamento)
    


    


