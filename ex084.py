# Faça um programa que leia o nome e peso de várias pessoas. No final, mostre:
# [A] Quantas pessoas foram cadastradas
# [B] Uma listagem com as pessoas mais pesadas
# [C] Uma listagem com as pessoas mais leves
cadastro = list()
pessoa = list()
maiorPeso = 0
menorPeso = 100
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))
    if pessoa[1] > maiorPeso:
        maiorPeso = pessoa[1]
    if pessoa[1] < menorPeso:
        menorPeso = pessoa[1]
    cadastro.append(pessoa[:])
    pessoa.clear()
    op = ' '
    while op not in 'sn':
        op = str(input('Deseja continuar? [S/N]')).strip().lower()
    if op == 'n':
        break
print('-=' * 15, end='-')
print(f'\nVocê cadastrou {len(cadastro)} {"pessoa." if len(cadastro) <= 1 else "pessoas."}')
print(f'O maior peso foi {maiorPeso}Kg. Peso de ', end='')
for i in range(0, len(cadastro)):
    if cadastro[i][1] == maiorPeso:
        print(cadastro[i][0], end='; ')
print(f'\nO menor peso foi {menorPeso}Kg. Peso de ', end='')
for pessoa in cadastro:
    if pessoa[1] == menorPeso:
        print(pessoa[0], end='; ')
