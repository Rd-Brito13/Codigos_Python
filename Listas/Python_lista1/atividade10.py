"""
10.	O custo ao consumidor de um carro novo é a soma do preço de fábrica com o
percentual  de lucro do distribuidor e dos impostos aplicados ao preço de fábrica. 
Faça um algoritmo que receba o preço de fábrica de um veículo, o percentual de lucro do distribuidor e o percentual de impostos. Calcule e mostre:
"""
Preco_Fabrica = float(input("INFORME AQUI O PREÇO DE FABRICA DO VEICULO: "))
Percentual_de_Lucro = float(input("INFORME O Percentual de lucro: " ))
Impostos_Aplicados = float(input("INFORME O PERCENTUAL DE IMPOSTOS: "))
Preco_Do_Veiculo = (Preco_Fabrica * Percentual_de_Lucro + Preco_Fabrica *  Impostos_Aplicados) / 100 + Preco_Fabrica
print(f"O preco do veiculo é de: {Preco_Do_Veiculo:.2f}")