
lista_categoria = []

for i in range(10):
    Idade = float(input("Informe a sua idade: "))
    lista_categoria.append(Idade)
    print("Operação realizada com sucesso!")

Media = sum(lista_categoria) / len(lista_categoria)

if Media <= 0 or Media <= 25:
    print("A equipe pertence a categória Jovem, com uma media de: {}".format(Media))
elif Media > 25 or Media <= 60:
    print("A equipe pertence a categória Sênior, com uma media de: {}".format(Media))
else: 
    print("A equipe pertence a categória Idoso, com uma media de: {}".format(Media))



    
