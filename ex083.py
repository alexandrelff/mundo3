# Faça um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
# analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
exp = str(input('Digite uma expressão: '))
pilha = list()
for i in exp:
    if i == '(':
        pilha.append(i)
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(i)
            break
if len(pilha) == 0:
    print('Sua expressão é válida.')
else:
    print('Sua expressão NÃO é válida.')
