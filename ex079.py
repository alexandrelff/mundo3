# Faça um programa onde o usuário possa digitar vários valores numéricos, e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos os valores digitados, em ordem crescente.
valores = list()
while True:
    n = int(input('Digite um valor: '))
    if n in valores:
        print('Valor duplicado, não foi adicionado.')
    else:
        print('Valor adicionado!')
        valores.append(n)
    op = ' '
    while op not in 'sn':
        op = str(input('Deseja continuar? [S/N] ')).strip().lower()
    if op in 'n':
        break
valores.sort()
print(f'Os valores digitados foram: {valores}')
