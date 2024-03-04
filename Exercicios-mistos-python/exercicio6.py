""" 3. Faça um programa que leia e valide as seguintes informações (e para cada uma delas, continue pedindo a informação até o usuário inserir corretamente):
 Nome: maior que 3 caracteres;
 Idade: entre 0 e 150;
 Salário: maior que zero;
 Sexo: 'f' ou 'm';
 Estado Civil: 's', 'c', 'v', 'd';
 O programa tem um crontrolador pro while e é póssivel encerrar ou continuar o programa quando quiser."""

Dados_Cadastrados = []
Controlador = input("Deseja iniciar o programa?(sim ou não): ")
while Controlador !="não":
    nome = input("informe o seu nome: ")

    while len(nome) < 4:
        print("por favor, o nome seu nome deve contar mais que 3 caracteres.")
        nome = input("insira novamente o seu nome: ")
        

    idade = int(input("informe a sua idade: "))

    while idade > 150:
        print("por favor, idade deve estar entre 0 e 150.")
        idade =  int(input("informe novamente a sua idade: "))

    salario = float(input("informe o seu salário: "))

    while salario <= 0:
        print("salario invalido, informe o seu salário maior que 0.")
        salario = float(input("informe novamente o seu salário: "))

    sexo = input("informe o seu sexo: ")

    while sexo != "Masculino" and sexo != "Feminino":
        print("Sexo invalido, informe novamente.")
        sexo = input("informe novamente o seu sexo (masculino ou feminino): ")

    est_civil = input("informe o seu estado civil: ")

    while est_civil != "Solteiro" and est_civil != "Casado" and est_civil != "Viuvo" and est_civil != "Divórciado":
        print("Estado Cívil inválido")
        est_civil = input("informe novamente o estado cívil (Solteiro, Casado, Viuvo ou Divórciado: ")

    Dados_Cadastrados.append([nome,idade,salario,sexo,est_civil])
    Controlador = input("Deseja iniciar o programa?(sim ou não): ")
print(Dados_Cadastrados)



    