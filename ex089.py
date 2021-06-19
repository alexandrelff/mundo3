# Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
# as notas de cada aluno individualmente
turma = list()
aluno = list()
notas = list()
while True:
    aluno.append(str(input('Nome: ')).strip())
    for i in range(0, 2):
        notas.append(float(input(f'Nota {i + 1}: ')))
    aluno.append(notas[:])
    turma.append(aluno[:])
    notas.clear()
    aluno.clear()
    res = ' '
    while res not in 'sn':
        res = str(input('Deseja continuar? [S/N] '))
    if res in 'n':
        break
print('-=' * 10, end='-')
print()
print('No.', f'{"Nome":<10}', f'Média')
for i in range(0, len(turma)):
    media = (turma[i][1][0] + turma[i][1][1]) / 2
    print(f'{i:<3}', f'{turma[i][0]:<10}', f'{media}')
