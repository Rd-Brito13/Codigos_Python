"""2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações."""

Loguin = input("Informe o seu loguin: ")
Senha = input("Informe a sua senha(a senha não deve ser igual ao loguin): ")

while Senha == Loguin:
    print("o loguin n pode ser igual a senha")
    Loguin = input("Informe o seu loguin: ")
    Senha = input("Informe a sua senha(a senha não deve ser igual ao loguin): ")



 
