""" 2.	Faça um algoritmo que receba duas notas, calcule e mostre a média aritmética e a mensagem que stá na tabela a seguir
"""

Nota = float(input("INFORME AQUI A PRIMEIRA NOTA: "))
Nota1 = float(input("INFORME AQUI A SEGUNDA NOTA: "))
Media = (Nota1 + Nota) / 2

if (Media > 0 and Media <= 4):
    print(f"SUA MEDIA É DE: {Media:.2f}. REPROVADO")
elif (Media > 4 and Media <= 7):
    print(f"SUA MEDIA É DE: {Media:.2f}. EXAME")
elif (Media > 7 and Media <= 10):
    print(f"SUA MEDIA É DE: {Media:.2f}. RECUPERAÇÃO")
