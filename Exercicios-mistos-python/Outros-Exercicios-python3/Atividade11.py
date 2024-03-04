"""	A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e o número de filhos. A prefeitura deseja saber:

•	a média do salário da população;
•	a média do número de filhos;
•	o maior salário;
•	a percentagem de pessoas com salários até R$ 150,00.

"""


#FUNÇÃO#
def Calcular_Medias():
      #VARIAVEIS UTILIZADAS PARA RETORNAS AS OPERAÇÕES RELACIONADAS AO SALÁRIO#
      Soma_Salario = 0
      Media_Salario = 0
      Contador_Media_Salario = 0
      Maior_Salario = 0


      # VARIAVEIS UTILIZADAS PARA RETORNAR OS VALORES RELACIONADAS AOS FILHOS #
      Soma_Filhos = 0
      Contador_Filho = 0
      Media_Filhos = 0
      # VARIAVEIS UTILIZADAS PARA RETORNAR OS VALORES RELACIONADAS AO SALARIO ATÉ 150 REAIS #
      Porcentagem_Pessoa_Salario = 0
      Porcentagem_Pessoa_Salario150 = 0

      #Loop FOR#
      for i in range(0, 5, 1):
            #DADOS DE ENTRADA#
            Salario = float(input(f"Familia {i+1}. INFORME O SEU SALARIO: "))
            Qtd_Filhos= int(input(f"Familia {i+1}. INFORME A QUATIDADE DE FILHOS: "))

            #MEDIA SALARIAL E MAIOR SALARIO DA POPULAÇÃO#
            Soma_Salario += Salario
            Contador_Media_Salario += 1
            Media_Salario = Soma_Salario / Contador_Media_Salario
            if (Salario > Maior_Salario):
                  Maior_Salario = Salario

            #MEDIA DOS FILHOS#
            Soma_Filhos += Qtd_Filhos
            Contador_Filho += 1
            Media_Filhos = Soma_Filhos / Contador_Filho

            #PORCENTAGEM SALARIAL ATÉ 150 REAIS#
            if(Salario <= 150):
                  Porcentagem_Pessoa_Salario += Salario

                  Porcentagem_Pessoa_Salario150 = Porcentagem_Pessoa_Salario / 5


      #EXIBIÇÃO PÓS CALCULOS#
      print(f"A MEDIA SALARIAL É DE: {Media_Salario:.2f}")
      print(f"O MAIOR SALARIO É: {Maior_Salario:.2f}")
      print(f"A MEDIA DE FILHOS DA POPULAÇÃO É DE: {Media_Filhos:.2f}")
      print(f"A PORCENTAGEM DE PESSOAS COM SALARIO ATÉ 150 REAIS É DE: {Porcentagem_Pessoa_Salario150:.2f}%")

Calcular_Medias()








