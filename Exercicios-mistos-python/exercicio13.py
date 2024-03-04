"""
13. O cardápio de uma lanchonete é o seguinte:
<pre>
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
</pre>

"""
Pedidos_Final = []
Quantidade = 0
iniciar = "sim"
while iniciar == "sim":
         print("Especificação   Código  Preço \nCachorro Quente 100     R$ 1,20 \nBauru Simples   101     R$ 1,30 \nBauru com ovo   102     R$ 1,50\nHambúrguer      103     R$ 1,20\nCheeseburguer   104     R$ 1,30\nRefrigerante    105     R$ 1,00")
         print("Por favor, escolha o seu pedido baseado no código do produtos.")

         Pedidos = int(input("informe o código dos produtos que deseja: "))
         
         match Pedidos:
                 case 100:
                         Quantidade = int(input("informe a quantidade de produtos que deseja: "))
                         Valor = ("O valor total é de: {:.2}".format(Quantidade * 1.20))
                 case 101:
                         Quantidade = int(input("informe a quantidade de produtos que deseja: "))
                         Valor = ("O valor total é de: {:.2}".format(Quantidade * 1.30))
                 case 102:
                         Quantidade = int(input("informe a quantidade de produtos que deseja: "))
                         Valor = ("O valor total é de: {:.2}".format(Quantidade * 1.50))
                 case 103:
                         Quantidade = int(input("informe a quantidade de produtos que deseja: "))
                         Valor = ("O valor total é de: {:.2}".format(Quantidade * 1.20))
                 case 104:
                         Quantidade = int(input("informe a quantidade de produtos que deseja: "))
                         Valor = ("O valor total é de: {:.2}".format(Quantidade * 1.30))
                 case 105:
                         Quantidade = int(input("informe a quantidade de produtos que deseja: "))
                         Valor =  ("O valor total é de: {:.2}".format(Quantidade * 1.0))
                 case _:
                         print("Código invalido, por favaor, siga o cardápio")
                         Pedidos = int(input("informe o código dos produtos que deseja: "))
                
         Anotacao = ("Código: {}".format(Pedidos))
         Quantidade_Anotacao = ("Quantidade: {}".format(Quantidade))
                         
         Pedidos_Final.append([Anotacao,Quantidade_Anotacao, Valor])
         iniciar = input("Deseja continuar efetuando o pedido??(sim ou não): ")

            
print(Pedidos_Final)

         
    
