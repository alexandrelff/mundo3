# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# [A] Apenas os 5 primeiros colocados;
# [B] Os últimos 4 colocados da tabela;
# [C] Uma lista com os times em ordem alfabética;
# [D] Em que posição na tabela está o time do Sport.

brasileirao20 = ('Flamento', 'Internacional', 'Atlético Mineiro', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras',
                 'Santos', 'Athletico Paranaense', 'Red Bull Bragantino', 'Ceará', 'Corinthians', 'Atlético Goianiense',
                 'Bahia', 'Sport', 'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')
print('=' * 10, 'CAMPEONATO BRASILEIRO SÉRIE A 2020', '=' * 10)
print('Os 5 primeiros colocados são: ')
for i in range(0, 5):
    print(f'{i + 1}º {brasileirao20[i]}')
print('-' * 25)
print('Os últimos 4 colocados: ')
for i in range(16, 20):
    print(f'{i + 1}º {brasileirao20[i]}')
print('-' * 25)
ordemAlf = sorted(brasileirao20)
print('Lista de times em ordem alfabética: ')
for time in ordemAlf:
    print(time)
print('-' * 25)
print('Prosição que terminou o Sport Clube Recife: ')
for pos, time in enumerate(brasileirao20):
    if time == 'Sport':
        print(f'O {time} terminou na {pos + 1}ª posição.')

