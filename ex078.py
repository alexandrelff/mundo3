#Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = list()
for n in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(f'Foram digitados os valores {valores}')
print(f'O maior valor digitado foi o número {max(valores)} na posição ', end='')
for n in range(0, 5):
    if valores[n] == max(valores):
        print(f'{n}...', end='')
print(f'\nO menor valor digitado foi o número {min(valores)} na posição ', end='')
for n in range(0, 5):
    if valores[n] == min(valores):
        print(f'{n}...', end='')
