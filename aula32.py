num = input("Digite um número: ")

if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print(f'{num} é par')
    else:
        print(f'{num} é ímpar')
else:
    print("O numero digitado não é um número inteiro")

#=======================================================================

hora = input("Digite uma hora: ")

if hora.isdigit():
    hora = int(hora)
    if hora < 0 or hora > 23:
        print("Hora inválida")
    else:
        if hora <= 11:
            print("Bom dia")
        elif hora <= 17:
            print("Boa tarde")
        else:
            print("Boa noite")
else:
    print("A hora digitada não é um número inteiro")

#=======================================================================

nome = input("Digite seu nome: ")

if len(nome) <= 4:
    print("Seu nome é curto")

elif len(nome) <= 6:
    print("Seu nome é normal")
    
else:
    print("Seu nome é grande")