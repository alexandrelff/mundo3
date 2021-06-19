# Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta
from random import randint
from time import sleep
palpite = list()
print('-=' * 15, end='-')
print(f'\n{"PALPITE DA MEGA SENA":^30}')
print('-=' * 15, end='-')
print()
n = int(input('Quantos jogos você deseja? '))
print('-=' * 3, f'SORTEANDO {n} JOGOS', '=-' * 3)
for i in range(0, n):
    jogo = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    palpite.append(jogo[:])
    jogo.clear()
for i in range(0, n):
    print(f'Jogo {i + 1}: {palpite[i]}')
    sleep(1)
print('-=' * 5, 'BOA SORTE!', '=-' * 5)

