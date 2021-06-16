# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# [A] Quantos números foram digitados.
# [B] A lista de valores, ordenada de forma decrescente.
# [C] Se o valor 5 foi digitado e está ou não na lista.
numeros = list()
while True:
    numeros.append(int(input('Digite um número: ')))
    op = ' '
    while op not in 'sn':
        op = str(input('Deseja continuar? [S/N] ')).strip().lower()
    if op == 'n':
        break
numeros.sort(reverse=True)
print('-=-' * 10)
print(f'Foram digitados {len(numeros)} números.')
print(f'Valores: {numeros}')
if 5 in numeros:
    print(f'O valor 5 aparece na posição {numeros.index(5)}')
else:
    print('O valor 5 não foi digitado.')
