"""
Um banco concederá um crédito especial aos seus clientes de acordo com o saldo médio no último ano. Faça um algoritmo que receba o saldo médio de um cliente
 e calcule o valor do crédito, de acordo com a tabela a seguir. Mostre o saldo médio e o valor do crédito.
"""
Saldo_Medio = float(input("INFORME AQUI O SEU SALDO MÉDIO: "))

if(Saldo_Medio > 400):
    Credito1 = (Saldo_Medio * 30) / 100
    print(f"O seu cŕedito especial é de: {Credito1:.2f}")
    Resultado1 = Credito1 + Saldo_Medio
    print(f"O seu novo saldo é de: {Resultado1:.2f}")
elif(Saldo_Medio > 300 and Saldo_Medio <= 400):
    Credito2 = (Saldo_Medio * 25) / 100
    print(f"O seu cŕedito especial é de: {Credito2:.2f}")
    Resultado2 = Credito2 + Saldo_Medio
    print(f"O seu novo saldo é de: {Resultado2:.2f}")
elif(Saldo_Medio > 200 and Saldo_Medio <= 300):
    Credito3 = (Saldo_Medio * 20) / 100
    print(f"O seu cŕedito especial é de: {Credito3:.2f}")
    Resultado3 = Credito3 + Saldo_Medio
    print(f"O seu novo resultado é de: {Resultado3:.2f}")
elif(Saldo_Medio <= 200):
    Credito4 = (Saldo_Medio * 10) / 100
    print(f"O seu cŕedito especial é de: {Credito4:.2f}")
    Resultado4 = Credito4 + Saldo_Medio
    print(f"O seu novo resultado é de: {Resultado4:.2f}")

