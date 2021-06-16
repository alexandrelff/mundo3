# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular
produtos = ('Monitor', 700, 'Mouse', 70, 'Cabo HDMI', 45, 'Mousepad', 54, 'Teclado', 120)
print('*' * 13, 'NOTA FISCAL', '*' * 13)
print('-' * 39)
for i in range(0, len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<30}', end='')
    else:
        print(f'R${produtos[i]:>7.2f}')
print('-' * 39)
