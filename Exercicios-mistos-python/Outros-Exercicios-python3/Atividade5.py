"""
Faça um algoritmo que receba a idade, a altura e o peso de 25 pessoas. Calcule e
      mostre:

•	A quantidade de pessoas com idade superior a 50 anos;
•	A média das alturas das pessoas com idade entre 10 e 20 anos;
•	A porcentagem de pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas.

"""


Qtd_Idade50 = 0
Contador_Altura = 0
Soma_Alturas_10_20 = 0
Inferior_40 = 0



for i in range(25):
    Idade = int(input(f"Pessoa{i+1}: INFORME A SUA IDADE: "))
    Altura = float(input(f"Pessoa{i+1}: INFORME A SUA ALTURA: "))
    Peso = float(input(f"Pessoa{i+1}: INFORME O SEU PESO:  "))

    if(Idade >= 50):
        Qtd_Idade50 += 1

    if(Idade >= 10 and  Idade <= 20):
        Soma_Alturas_10_20 += Altura
        Contador_Altura += 1


    if(Peso < 40):
        Inferior_40 += 1




Media_Alturas_10_20 = Soma_Alturas_10_20 / Contador_Altura
Porcentagem_Peso_inf = (Inferior_40 / 25) * 100


print(f"A quantidade de pessoas acima de 50 anos é de: {Qtd_Idade50}")
print(f"A MEDIA DE ALTURA ENTRE 10 E 20 ANOS É DE: {Media_Alturas_10_20:.2f}")
print(f"A PORCENTAGEM DE PESSOAS COM PESO INFERIOR A 40 É DE: {Porcentagem_Peso_inf:.2f}%")