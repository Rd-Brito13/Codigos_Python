"Digamos que temos uma lista de vendedores e as quantidas vendidas e queremos identificar todos os vendedores que batem a meta de 50 vendas"
vendas = [941, 548, 2156, 378, 20 ,46]
vendedores = ["Fernando", "Judas", "Maria", "Jordania", "Tânia", "Fernanda"]
meta = 50
i = 0

while vendas[i] >= meta:
    print("A quantidade de vendas do vendedor(a): {}, foi: {}".format(vendedores[i], vendas[i]))
    i += 1
    
        
    