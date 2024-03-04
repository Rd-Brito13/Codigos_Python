produtos = ["abc145", "abe1578","dab258","beb698", "beb174"]

def padronizar_texto(texto):
    texto = texto.upper()
    texto = texto.replace("  "," ")
    texto = texto.strip()
    return texto

produtos_padronizados = []
"""
Feito com for
for i , produto in enumerate(produtos):
   produtos[i]= padronizar_texto(produto)
   produtos_padronizados.append(padronizar_texto(produto))

print(produtos)
print(produtos_padronizados)
"""
produtos_padronizados = list(map(padronizar_texto, produtos))
print(produtos)
print(produtos_padronizados)