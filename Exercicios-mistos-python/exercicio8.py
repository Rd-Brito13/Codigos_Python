"""
5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
"""

Controlador = input("Deseja iniciar o programa?(sim ou não): ")
while Controlador == "sim":
        Pop_Pais_A = float(input("Informe a população total do País A: "))
        Pop_Pais_B = float(input("Informe a população do país B: "))
        while  Pop_Pais_A <= 0 or Pop_Pais_B <= 0:
             print("Nenhuma das populações podem estar zeradas.")
             Pop_Pais_A = float(input("Informe a população total do País A: "))
             Pop_Pais_B = float(input("Informe a população do país B: "))

        Taxa_Pais_A = float(input("Informe a taxa de crescimento do país A: "))
        Taxa_Pais_B = float(input("Informe a taxa de crescimento do país B: "))
        
        while Taxa_Pais_A <= 0 or Taxa_Pais_B <= 0:
             print("Nenhuma das taxas podem estar zeradas.")
             Taxa_Pais_A = float(input("Informe a taxa de crescimento do país A: "))
             Taxa_Pais_B = float(input("Informe a taxa de crescimento do país B: "))
        
        tempo = 0

        while Pop_Pais_A < Pop_Pais_B:
            Pop_Pais_A *= Taxa_Pais_A
            Pop_Pais_B *= Taxa_Pais_B
            tempo += 1
        print("Serão necessário aproximadamente:", tempo," anos para igualar ou superar a população B")
        Controlador = input("Deseja iniciar o programa?: ")