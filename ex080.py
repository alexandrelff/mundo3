# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção(sem usar o sort()). No final, mostre a lista ordenada na tela.
valores = list()
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if i == 0:
        valores.append(n)
        print('Valor adicionado na posição 0')
    elif n > valores[-1]:
        valores.append(n)
        print('Valor adicionado por último')
    else:
        for j in range(0, len(valores)):
            if n <= valores[j]:
                valores.insert(j, n)
                print(f'Valor adicionado na posição {j}')
                break
print(f'Os valores digitados foram: {valores}')
