def multiplica(*args):
    total = 1
    for numero in args:
        print(f'{total} * {numero}')
        total *= numero
    return total

def parimpar(total):
    if total % 2 == 0:
        return 'Par'
    return 'Ímpar'

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
total = multiplica(*numeros)
print(total)

print(f'O numero {total}, é: {parimpar(total)}')

