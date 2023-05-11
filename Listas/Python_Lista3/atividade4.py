"""
Uma loja utiliza o código “V” para transação à vista e “P” para transação à prazo. Faça um algoritmo que receba o código e o valor de 15 transações. Calcule e mostre:
"""

TotalVista = 0.0
TotalPrazo = 0.0
ValorTotal = 0.0
PrestacaoPrazo = 0.0

for i in range(3):
    Codigo = input("Infome o tipo de transação, sendo que (V) corresponde à vista e (P) corresponde à Prazo: ")
    Transacoes = float(input("INFORME AQUI O VALOR DAS TRANSIÇÕES: "))


    if(Codigo == "V"):
        TotalVista += Transacoes

    elif(Codigo == "P"):
        TotalPrazo += Transacoes
        PrestacaoPrazo = TotalPrazo / 3

    ValorTotal += Transacoes

print("Valor total das compras à vista é de: R$ %.2f" % TotalVista)
print("Valor total das compras à prazo é de: R$ %.2f" % TotalPrazo)
print("A primeira prestação  é de: R$ %.2f" % PrestacaoPrazo)
print("Valor total das compras é de: R$ %.2f" % ValorTotal)


