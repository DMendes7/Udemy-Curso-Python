# https://github.com/luizomf/cursopython2023/blob/main/aula61.py

#cpf = input("Digite o CPF: ")
cpf = '72682489070'
digito = 0
primeiro_digito = 0
segundo_digito = 0
multiplicador = 10

# Calculando o primeiro dígito
for i in range(9):
    digito += int(cpf[i]) * multiplicador
    print(f'i ={i}, Multi: {multiplicador}, CPF_D: {cpf[i]}, Sum: {digito}')
    multiplicador -= 1

digito *= 10
print(f'Digito * 10 = {digito}')

digito = digito % 11
print(f'Resto da divisão por 11 = {digito}')

if digito > 9:
    primeiro_digito = 0
else:
    primeiro_digito = digito

print(f'1-D: {primeiro_digito}')

multiplicador = 11
digito = 0

for i in range(10):
    digito += int(cpf[i]) * multiplicador
    print(f'i ={i}, Multi: {multiplicador}, CPF_D: {cpf[i]}, Sum: {digito}')
    multiplicador -= 1

digito *= 10
print(f'Digito * 10 = {digito}')

digito = digito % 11
print(f'Resto da divisão por 11 = {digito}')

if digito > 9:
    segundo_digito = 0
else:
    segundo_digito = digito

print(f'2-D: {segundo_digito}')

if primeiro_digito == int(cpf[9]) and segundo_digito == int(cpf[10]):
    print('CPF Válido')
else:
    print('CPF Inválido')
