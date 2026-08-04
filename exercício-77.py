varias_palavras = 'Amor', 'Msg', 'Reciprocidade', 'Respeito', 'Empatia', 'Genuidade', 'Generosidade', 'Carinho', 'Atraçao', 'Sol', 'Sorriso', 'Cacheada', 'Educada', 'Indecisa', 'Autonoma', 'KKK'
vogais = 'a', 'e', 'i', 'o', 'u'
vogais_encontradas = ''
for palavra in varias_palavras:
    s_vogal = 0
    print(f'\nA palavra {palavra.upper()} possui as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in vogais:
            vogais_encontradas = letra
            print(vogais_encontradas.lower(), end=' ')
        else:
            s_vogal += 1
    if s_vogal == len(palavra):
        print('Não foi encontrado', end='')