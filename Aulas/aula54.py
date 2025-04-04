'''Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre.com
erros de índices inexistentes na lista.'''

lista = []

while True:
    print("1 - Inserir na lista")
    print("2 - Apagar da lista")
    print("3 - Listar a lista")
    print("4 - Sair")
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        item = input("Digite o item a ser inserido: ")
        lista.append(item)
    elif opcao == "2":
        if len(lista) == 0:
            print("Lista vazia")
        else:
            print("Lista atual: ")
            for i, item in enumerate(lista):
                print(f"{i}: {item}")
            try:
                indice = int(input("Digite o índice do item a ser apagado: "))
                if 0 <= indice < len(lista):
                    lista.pop(indice)
                else:
                    print("Índice inválido")
            except ValueError:
                print("Por favor, digite um número válido")
    elif opcao == "3":
        if len(lista) == 0:
            print("Lista vazia")
        else:
            print("Lista atual: ")
            for i, item in enumerate(lista):
                print(f"{i}: {item}")
    elif opcao == "4":
        break
    else:
        print("Opção inválida")
    print()