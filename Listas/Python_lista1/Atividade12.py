"""
Um trabalhador recebeu seu salário e o depositou em sua conta corrente bancária. Esse trabalhador emitiu dois cheques e agora deseja saber seu saldo atual.
Sabe-se que cada operação bancária de retirada paga CPMF de 0,38% e o saldo inicial da conta está zerado.
"""
Deposito = float(input("DEPOSITE AQUI O SEU SALARIO: "))
Saldo1 = Deposito - ((Deposito * 0.38) / 100)
print(f"O SEU SALDO ATUAL É DE: {Saldo1:.2f}")
Saldo2 =  Saldo1 - ((Saldo1 * 0.38) / 100)
print(f"O SEU SALDO ATUAL É DE: {Saldo2:.2f}")
Saldo_Atual =  (Saldo1 + Saldo2) - Deposito

