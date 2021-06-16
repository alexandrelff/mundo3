# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores ímpares digitados, respectivamente
# Ao final, mostre o conteúdo das três listas geradas.
listA = list()
listPar = list()
listImp = list()
while True:
    listA.append(int(input('Digite um número: ')))
    op = ' '
    while op not in 'sn':
        op = str(input('Deseja continuar? [S/N] ')).strip().lower()
    if op == 'n':
        break
for n in listA:
    if n % 2 == 0:
        listPar.append(n)
    else:
        listImp.append(n)
print('-==-' * 10)
print(f'Os valores digitados foram: {listA}')
print(f'Números pares: {listPar}')
print(f'Números ímpares: {listImp}')
