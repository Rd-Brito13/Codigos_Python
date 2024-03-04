""" algoritmo que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:

        a) a idade desa pessoa;
        b) quantos anos essa pessoa terá em 2030;
"""
Ano_Nascimento = int(input("Digite aqui o seu ano de nascimento: "))
Ano_Atual = int(input("Digite aqui o ano atual: "))
Idade_Atual =  Ano_Atual - Ano_Nascimento
print(f"A sua idade é: {Idade_Atual}")
Idade_Futura = 2030 - Ano_Nascimento 
print(f"A sua Idade em 2030 séra: {Idade_Futura}")