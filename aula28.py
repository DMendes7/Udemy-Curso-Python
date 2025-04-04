nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome tem espaço')
    else:
        print('Seu nome não tem espaço')
    print(f'Su nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome eh: {nome[0]}')
    print(f'A última letra do seu nome eh: {nome[-1]}')

else:
    print('Digite seu nome e idade')
    exit()
