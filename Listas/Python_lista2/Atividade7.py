"""
Faça um algoritmo que receba a idade de um nadador e mostre sua categoria usando as regras a seguir.
"""

Idade = int(input("DIGITE A SUA IDADE: "))

if(Idade >= 5 and Idade <= 7):
    print("Infatil")
elif(Idade >= 8 and Idade <= 10):
    print("Juvenil")
elif(Idade >= 11 and Idade <= 15):
    print("Adolescente")
elif(Idade >= 16 and Idade <= 30):
    print("Adulto")
else:
    print("Sênior")