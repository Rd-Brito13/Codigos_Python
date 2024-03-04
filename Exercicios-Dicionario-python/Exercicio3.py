# Exercício 3
# Dada a lista de preços de produtos, uma loja resolveu fazer um reajuste nos preços dos produtos. 
# calcule o novo valor dos produtos com base nas seguintes regras:
# Preços até 1.000 vão ter um reajuste de 10% (ou seja, o novo preço será 110% do preço atual)
# Preços até maiores que 1.000 até 2.000 vão ter reajuste de 15%
# Preços acima de 2.000 vão ter reajuste de 20%

precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}

for Produto in precos:
    if precos[Produto] <= 1000:
        precos[Produto] += (precos[Produto] * 10) / 100
        
    elif precos[Produto] > 1000 and precos[Produto] <= 2000:
        precos[Produto] -= (precos[Produto] * 15) / 100
        
    elif precos[Produto] > 2000:
        precos[Produto] -= (precos[Produto] * 20) / 100

print(precos)