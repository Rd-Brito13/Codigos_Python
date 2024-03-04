# Exercício 4
# Edite o programa antigo para ter os 2 dicionários, o de preços originais e o de novos preços
# Em seguida calcule o valor total de reajuste em R$ que teve entre a lista de produtos original e a lista final

precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}
novos_precos = {}

for Produto in precos:
    if precos[Produto] <= 1000:
        Novo_Valor = (precos[Produto] * 10) / 100
        Novo_2 = Novo_Valor + precos[Produto]
        novos_precos.update({Produto: Novo_2})
        
    elif precos[Produto] > 1000 and precos[Produto] <= 2000:
        Novo_Valor = (precos[Produto] * 15) / 100
        Novo_2 = precos[Produto] - Novo_Valor 
        novos_precos.update({Produto: Novo_2})
        
    elif precos[Produto] > 2000:
        Novo_Valor = (precos[Produto] * 20) / 100
        Novo_2 =  precos[Produto] - Novo_Valor
        novos_precos.update({Produto: Novo_2})
print(precos)
print(novos_precos)

total_lista_origi = sum(precos.values())
total_lista_nova = sum(novos_precos.values())
total_final = total_lista_origi - total_lista_nova
print("O total do reajuste foi de: {}".format(total_final))
