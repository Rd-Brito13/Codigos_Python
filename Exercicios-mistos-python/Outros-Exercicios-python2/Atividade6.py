"""
 Faça um algoritmo que receba o preço de um produto, calcule e mostre, de acordo com as tabelas a seguir, o novo preço e classificação.
"""
Produto = float(input("INFORME AQUI O PREÇO DO PRODUTO: "))

if(Produto <= 50):
    Aumento = (Produto * 5) / 100 + Produto
    print(f"O valor atual do produto é de: {Aumento:.2f}")
elif(Produto > 50 and Produto <= 100):
    Aumento = (Produto * 10) / 100 + Produto
    print(f"O valor atual do produto é de: {Aumento:.2f}")
elif(Produto > 100):
    Aumento = (Produto * 15) / 100 + Produto
    print(f"O valor atual do produto é de: {Aumento:.2f}")

if(Aumento <= 80):
    print(f"O valor atual do produto é de: {Aumento:.2f} - Barato")
elif(Aumento > 50 and Aumento <= 100):
    print(f"O valor atual do produto é de: {Aumento:.2f} - Normal")
elif(Aumento >= 120 and Aumento <= 200):
    print(f"O valor atual do produto é de: {Aumento:.2f} - Caro")
elif(Aumento > 200):
    print(f"O valor atual do produto é de: {Aumento:.2f} - Muito Caro")

