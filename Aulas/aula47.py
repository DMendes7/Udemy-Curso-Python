# https://github.com/luizomf/cursopython2023/blob/main/aula47.py

import os

palavra = 'python'
letras_acertadas = ''
tentativas = 0
while True:
    letra = input('Digite uma letra: ')
    tentativas += 1
    if len(letra) > 1:
        print('Apenas uma letra é permitida!')
        continue

    if letra in palavra:
        letras_acertadas += letra
        os.system('cls')
        print(f'Letras acertadas: {letras_acertadas}')

    formatada = ''

    for secreto in palavra:
        if secreto in letras_acertadas:
            formatada += secreto
        else:
            formatada += '*'
    
    if formatada == palavra:
        print(f'Parabéns! A palavra é {palavra}')
        print(f'Você acertou em {tentativas} tentativas')
        tentativas = 0
        letras_acertadas = ''
        break