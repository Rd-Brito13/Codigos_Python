"""
Faça um algoritmo que receba dois números e execute as operações listadas a seguir de acordo com a escolha do usuário.

"""

Numero = float(input("INFORME AQUI O PRIMEIRO NUMERO: "))
Numero1 = float(input("INFORME AQUI O SEGUNDO NUMERO: "))

opi = True



while(opi == True):


    print("                  TABELA DE CLASSIFICAÇÃO                      ")
    print("1 - MEDIA ENTRE OS NUMERO DIGITADOS")
    print("2 - DIFERENÇA DO MAIOR PELO MENOR")
    print("3 - PRODUTO ENTRE OS NUMERO DIGITADOS")
    print("4 - DIVISÃO DO PRIMEIRO PELO SEGUNDO NUMERO")
    print("5 - DESEJA ENCERRAR O PROGRAMA?")

    op = int(input("FAÇA SUA ESCOLHA: "))

    if(op == 1):
        Media = (Numero + Numero1) / 2
        print(f"A media é de: {Media:.2f} ")




    elif(op == 2):
        if (Numero > Numero1):
            print("A Diferença é de:", Numero - Numero1)

        else:
            print("A DIFERENÇA É DE:", Numero1 - Numero)




    elif(op == 3):
        Produto = Numero * Numero1
        print(f"O PRODUTO É DE: {Produto:.2f}")




    elif(op == 4):
        Divisao = Numero / Numero1
        print(f"A DIVISÃO É DE: {Divisao:.2f}")




    elif (op == 5):
        print("Programa encerrado")
        break

    else:
        print("Opção invalida. Por Favor, escolha uma opção valida.")

    continuar = input("Deseja Continuar? (SIM/NÃO): ")

    if(continuar.upper() != "SIM"):
        print("Programa Encerrado")
        break






