"""
Faça um algoritmo que recba o preço de um produto e o seu código de origem e mostre sua procedência. A procedência obedece à tabela a seguir.

"""


Codigo = int(input("INFORME O CODIGO: "))

if(Codigo ==  1):
    print("Sul")
elif(Codigo == 2):
    print("Norte")
elif(Codigo == 3):
    print("Leste")
elif(Codigo == 4):
    print("Oeste")
elif(Codigo == 5 or Codigo == 6):
    print("Nordeste")
elif(Codigo == 7 or Codigo == 8 or Codigo == 9):
    print("Sudeste")
elif(Codigo >= 10 and Codigo <= 20):
    print("Centro-Oeste")
elif(Codigo >= 21 and Codigo <= 30):
    print("Nordeste")
