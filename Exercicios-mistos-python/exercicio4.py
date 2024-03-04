'''1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.'''

nota = float(input("informe uma nota de 0 a 10: "))
while nota > 10:
    print("valor inválido")
    nota = float(input("informe novamente a nota (de 0 a 10): "))
    if nota >= 0 and nota  <= 10:
        print("valor aceito")
    
   
