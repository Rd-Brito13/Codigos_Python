"""10. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um."""

valor_cd = []
qtd_cd = int(input("Informe o tamanho da sua coleção: "))

for cd in range(qtd_cd):
    cd_valor = float(input("Informe o Valor de cada CD's: "))
    valor_cd.append(cd_valor)
    

print("O valor medio é de: {:.1}, e o valor total investido é de: {:.1}".format(sum(valor_cd) / qtd_cd, sum(valor_cd)))

    
    
