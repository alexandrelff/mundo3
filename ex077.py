# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('rua', 'avenida', 'estrada', 'rodovia', 'ponte', 'viaduto', 'cruzamento', 'girador')
for palavra in palavras:
    print(f'\nA paravra {palavra} tem ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
