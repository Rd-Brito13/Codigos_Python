"""
Faça um algoritmo que receba a idade e opeso de 15 pessoas. Calcule e mostre as médias dos pesos das pessoas da mesma faixa etária.
 As faixas etárias são: de 1 a 10 anos, de 11 a 20 anos, de 21 a 30 anos e maiores de 31 anos.
"""

QuantidadeUM = 0
QuantidadeDOIS = 0
QuantidadeTRES = 0
QuantidadeQUATRO = 0
Um_a_Dez = 0
Onze_a_Vinte = 0
Vinted_a_Trista = 0
MainioTantrum = 0
Soma_Pesos = 0

for i in range(0, 15 ,1):
    Idade = int(input(f"Pessoa{i+1}. Informe a sua idade: "))
    Peso = float(input(f"Pessoa{i+1}. Informe o seu peso: "))

    if(Idade >= 1 and Idade <= 10):
        QuantidadeUM += 1
        Soma_Pesos += Peso
        Um_a_Dez = Soma_Pesos / 15



    elif(Idade >= 11 and Idade <= 20):
        QuantidadeDOIS += 1
        Soma_Pesos += Peso
        Onze_a_Vinte = Soma_Pesos / 15


    elif(Idade >= 21 and Idade <= 30):
        QuantidadeTRES += 1
        Soma_Pesos += Peso
        Vinted_a_Trista = Soma_Pesos / 15


    elif(Idade >= 31):
        QuantidadeQUATRO += 1
        Soma_Pesos += Peso
        MainioTantrum = Soma_Pesos / 15


print(f"A media de pesos da faixa etaria  de 1 a 10 anos é de: {Um_a_Dez:.2f}. \nA quantidade de pessoas presente nessa faixa etária é de: {QuantidadeUM}")
print(f"A media de peso entre a faixa etaria de 11 a 20 anos é de: {Onze_a_Vinte:.2f}. \nA quantidade de pessoas presente nessa faixa etária é de: {QuantidadeDOIS}")
print(f"A media de peso entre a faixa etaria de 21 a 30 anos é de: {Vinted_a_Trista:.2f}. \nA quantidade de pessoas presente nessa faixa etária é de: {QuantidadeTRES}")
print(f"A media de peso entre a faixa etaria de maior de 31 anos é de: {MainioTantrum:.2f}. \nA quantidade de pessoas presente nessa faixa etária é de: {QuantidadeQUATRO}")



