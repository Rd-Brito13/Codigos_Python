"""
10.	Faça um algoritmo que receba:

•	o código do produto comprado;
•	a quantidade comprada de um produto;

Calcule e mostre:

•	o preço unitário do produto comprado segundo a Tabela I;
•	o preço total da nota;
•	o valor do desconto, segundo a Tabela II e aplicado sobre o preço total da nota;
•	o preço final da nota depois do desconto.

"""
Codigo = int(input("DIGITE AQUI O CODIGO DO PRODUTO: "))
Quantidade = int(input("DIGITE AQUI A QUANTIDADE COMPRADA DO PRODUTO: "))


def Teste():
    if(Codigo >= 1  and Codigo <= 10):
        Produto = 10.00
        print(f"O VALOR DO PRODUTO É DE: {Produto:.2f}")
        Preco_Nota = Produto * Quantidade
        print(f"O VALOR TOTAL DA NOTA É DE: {Preco_Nota:.2f}")
        if (Preco_Nota <= 250.00):
            Desconto = Preco_Nota - ((Preco_Nota * 5) / 100)
            print(f"O VALOR TOTAL DO DESCONTO É DE: {Desconto:.2f}")
        elif (Preco_Nota >= 250.00 and Preco_Nota <= 500):
            Desconto = Preco_Nota - ((Preco_Nota * 10) / 100)
            print(f"O VALOR TOTAL DO DESCONTO É DE:: {Desconto:.2f}")
        elif (Preco_Nota > 500):
            Desconto = Preco_Nota - ((Preco_Nota * 15) / 100)
            print(f" O VALOR TOTAL DO DESCONTO É DE: {Desconto:.2f}")


Teste()

def Teste2():
    if(Codigo >= 11 and Codigo <= 20):
        Produto = 15.00
        print(f"O VALOR DO PRODUTO É DE: {Produto:.2f}")
        Preco_Nota = Produto * Quantidade
        print(f"O VALOR TOTAL DA NOTA É DE: {Preco_Nota:.2f}")
        if (Preco_Nota <= 250.00):
            Desconto = Preco_Nota - ((Preco_Nota * 5) / 100)
            print(f"O VALOR TOTAL DO DESCONTO É DE: {Desconto:.2f}")
        elif(Preco_Nota >= 250.00 and Preco_Nota <= 500):
            Desconto = Preco_Nota - ((Preco_Nota * 10) / 100)
            print(f"O VALOR TOTAL DO DESCONTO É DE: {Desconto:.2f}")
        elif (Preco_Nota > 500):
            Desconto = Preco_Nota - ((Preco_Nota * 15) / 100)
            print(f"O VALOR TOTAL DO DESCONTO É DE: {Desconto:.2f}")

Teste2()

def Teste3():
    if(Codigo > 21 and Codigo <= 30):
        Produto = 20.00
        print(f"O VALOR DO PRODUTO É DE: {Produto:.2f}")
        Preco_Nota = Produto * Quantidade
        print(f"O VALOR TOTAL DA NOTA É DE: {Preco_Nota:.2f}")
        if (Preco_Nota <= 250.00):
            Desconto = Preco_Nota - ((Preco_Nota * 5) / 100)
            print(f"O VALOR TOTAL DO DESCONTO É DE:: {Desconto:.2f}")

        elif (Preco_Nota >= 250.00 and Preco_Nota <= 500):
            Desconto = Preco_Nota - ((Preco_Nota * 10) / 100)
            print(f"O VALOR TOTAL DO DESCONTO É DE:: {Desconto:.2f}")
        elif (Preco_Nota > 500):
            Desconto = Preco_Nota - ((Preco_Nota * 15) / 100)
            print(f"O VALOR TOTAL DO DESCONTO É DE:: {Desconto:.2f}")
Teste3()

def Teste4():
    if(Codigo > 30 and Codigo <= 40):
        Produto  = 30.00
        print(f"O VALOR DO PRODUTO É DE: {Produto:.2f}")
        Preco_Nota = Produto * Quantidade
        print(f"O VALOR TOTAL DA NOTA É DE: {Preco_Nota:.2f}")
        if (Preco_Nota <= 250.00):
            Desconto = Preco_Nota - ((Preco_Nota * 5) / 100)
            print(f"O VALOR TOTAL DO DESCONTO É DE: {Desconto:.2f}")
        elif (Preco_Nota >= 250.00 and Preco_Nota <= 500):
            Desconto = Preco_Nota - ((Preco_Nota * 10) / 100)
            print(f"O VALOR TOTAL DO DESCONTO É DE: {Desconto:.2f}")
        elif (Preco_Nota > 500):
            Desconto = Preco_Nota - ((Preco_Nota * 15) / 100)
            print(f"O VALOR TOTAL DO DESCONTO É DE: {Desconto:.2f}")
Teste4()


