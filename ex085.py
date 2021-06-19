# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separado os valores ímpares e pares. No final, mostre os valores pares e ímpares em ordem crescente.
numeros = [[], []]
for i in range(1, 8):
    n = int(input(f'Digite o {i}º número: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print('-=' * 15, end='-')
print(f'\nOs valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')
