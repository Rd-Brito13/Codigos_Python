preco_tecnologia = {'notebook asus': 2450, 'iphone': 4500, 'samsung galaxy': 3000, 'tv samsung': 1000, 'ps5': 3000, 'tablet': 1000, 'notebook dell': 3000, 'ipad': 3000, 'tv philco': 800, 'notebook hp': 1700}

def ehmaior2000(maior):
    return maior[1] > 2000

maior_valor = dict(filter(ehmaior2000, preco_tecnologia.items()))
print(maior_valor)

maior_valor2 = dict(filter(lambda maior: maior[1] > 2000, preco_tecnologia.items()))
print(maior_valor2)