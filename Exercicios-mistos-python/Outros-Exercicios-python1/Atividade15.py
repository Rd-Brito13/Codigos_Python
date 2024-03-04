"""
 Faça um algoritmo que receba o custo total de um espetáculo teatral e o preço do
convite  desse espetáculo. Esse algoritmo deve calcular e
mostrar a quantidade de convites que devem ser vendidos para que pelo menos o custo do espetáculo seja alcançado.
"""
Custo_Total = float(input("INFORME O CUSTO TOTAL: "))
Ingressos = float(input("INFORME O VALOR DE CADA INGRESSO: "))
Despesas_EM_Conta = Custo_Total // Ingressos
print(f"A quantidade de convites para bancar o custo é de: {Despesas_EM_Conta:.2f}")
