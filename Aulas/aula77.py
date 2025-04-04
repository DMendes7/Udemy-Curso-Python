# ATIVIDADE

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qntPerguntas = len(perguntas)
perguntaAtual = 0
acertos = 0

while perguntaAtual < qntPerguntas:
    print(f'{perguntas[perguntaAtual]['Pergunta']}\n')
    for i, valor in enumerate(perguntas[perguntaAtual]['Opções']):
        print(f'{i}) {valor}')
    print()
    resposta = (input("Escolha uma opcao: "))

    try:
        intResposta = int(resposta)
        if(intResposta > 3 or intResposta < 0):
            print('❗| Opção invalida')
            continue
        else:
            exit

    except ValueError:
        print('❗| A opção deve ser um numero\n')
        continue
    except IndexError:
        print('Opção invalida\n')    

    if int(perguntas[perguntaAtual]['Opções'][intResposta]) == int(perguntas[perguntaAtual]['Resposta']):
        acertos += 1
        print('\nParabens 🎆 | Você acertou\n')
    else:
        print('\nParece que você errou 😥\nMas não fique triste\n')
        
    perguntaAtual += 1

print(f'Você acertou {acertos} de {qntPerguntas}\n')