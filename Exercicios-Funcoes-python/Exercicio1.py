"""
# Exercícios

Para fazer um treino simples antes de avançarmos em mais functions, vamos criar uma function que resolve 1 "desafio simples"

## 1. Function para Cálculo de Carga Tributária

(Lembrando, não se atente ao funcionamento real da carga tributária, é apenas um exemplo imaginário para treinarmos as functions com algo mais prático)

Imagine que você trabalha no setor contábil de uma grande empresa de Varejo. 

Crie uma function que calcule qual o % de carga tributária que está sendo aplicado sobre um determinado produto, dado o preço de venda, o "lucro" e os custos (com exceção do imposto) dele.
"""

preco_venda = 2800
custo = 550
lucro = 1480

def Carga_Tributaria(preco_venda, custo, lucro):
     carga = preco_venda - custo - lucro
     return carga / preco_venda
print("O valor da carga tributaria é de: {:.2%}".format(Carga_Tributaria(preco_venda,custo,lucro)))
