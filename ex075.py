# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# [A] Quantas vezes apareceu o valor 9;
# [B] Em que posição foi digitado o primeiro valor 3;
# [C] Quais foram os números pares
valores = (int(input('Digite o primeiro valor: ')), int(input('Digite o primeiro valor: ')),
           int(input('Digite o primeiro valor: ')), int(input('Digite o primeiro valor: ')))

print(f'O número 9 foi digitado {valores.count(9)} {"vez" if valores.count(9) == 1 else "vezes"}')
if 3 in valores:
    print(f'O número 3 aparece primeiro na {valores.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado.')
for i in range(0, 4):
    if valores[i] % 2 == 0:
        print('Números pares:  ')
        for n in valores:
            if n % 2 == 0:
                print(f'{n}', end=' ')
        break
    else:
        print('Não existem números pares.')
        break




