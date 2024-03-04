"""Receber notas e pesos de um aluno e calcular a média ponderada"""

Nota = float(input("Digite aqui a primeira nota: "))
Peso = int(input("Digite aqui o peso da primeira nota: "))
Nota2 = float(input("Digite aqui a segunda nota: "))
Peso2 = int(input("Digite aqui o Peso da segunda nota: "))
Nota3 = float(input("Digite aqui a terceira nota: "))
Peso3 = int(input("Digite aqui o peso da terceira nota: "))

Nota1 = Nota * Peso
Notaa2 = Nota2 * Peso2
Notaa3 = Nota3 * Peso3
Pesos = Peso + Peso2 + Peso3
Media_Ponderada = (Nota1 + Notaa2 + Notaa3) / Pesos

print(f"A sua media ponderada é de: {Media_Ponderada:.2f}")