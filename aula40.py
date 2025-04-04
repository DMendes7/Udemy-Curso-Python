'''https://github.com/luizomf/cursopython2023/blob/main/aula40.py'''

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

while num1 and num2:
    print("1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\n5 - Sair")
    opcao = int(input("Escolha uma opção: "))
    print("\n")
    if opcao == 1:
        print(f"{num1} + {num2} = {num1 + num2}\n")
    elif opcao == 2:
        print(f"{num1} - {num2} = {num1 - num2}\n")
    elif opcao == 3:
        print(f"{num1} * {num2} = {num1 * num2}\n")
    elif opcao == 4:
        print(f"{num1} / {num2} = {num1 / num2}\n")
    elif opcao == 5:
        break
    else:
        print("Opção inválida!")
