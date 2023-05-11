"""
Faça um algoritmo que receba quatro notas de um aluno, calcule e mostre
a média aritmética das notas e a mensagem de aprovado ou reprovado, considerando para aprovação média 7.
"""
Nota = float(input("INFORME AQUI A PRIMEIRA NOTA: "))
Nota1 = float(input("INFORME AQUI A SEGUNDA NOTA: "))
Nota2 = float(input("INFORME AQUI A TERCEIRA NOTA: "))
Nota3 = float(input("INFORME AQUI A QUARTA NOTA: "))
Media = (Nota + Nota1 + Nota2 + Nota3) / 4

if(Media >= 7):
    print(f"Media de: {Media:.2f} \nAPROVADO")
else:
    print(f"Media de: {Media:.2f} \nREPROVADO")

