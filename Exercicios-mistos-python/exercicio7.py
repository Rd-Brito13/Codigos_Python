"""4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento."""

Pop_Pais_A = 80000
Pop_Pais_B = 200000
tempo = 0

while Pop_Pais_A < Pop_Pais_B:
    Pop_Pais_A *= 1.03
    Pop_Pais_B *= 1.105
    tempo += 1
    
print("Serão necessário aproximadamente:", tempo, " anos para igualar ou superar a população B")

