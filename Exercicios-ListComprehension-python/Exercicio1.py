vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]

#Lista dos valores vendidos em 2019
vendas_produtos2019 = [vendas2019 for produtos, vendas2019, vendas2020 in vendas_produtos]
print("Vendas de 2019: {}".format(vendas_produtos2019))
#Maior venda de 2019
maior_venda2019 = max(vendas_produtos2019)
print("A maior venda é de: {}".format(maior_venda2019))
#O produto mais vendido de 2019 e o valor.
vendas_produtosmaxi = [(vendas2019, produto) for produto, vendas2019, vendas2020 in vendas_produtos]
maior_valor, maior_produto = max(vendas_produtosmaxi)
print("O produto mais vendido é: {}, com um valor de: {}".format(maior_produto, maior_valor))

