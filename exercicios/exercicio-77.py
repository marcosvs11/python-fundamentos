varias_palavras = 'Amor', 'Msg', 'Reciprocidade', 'Respeito', 'Empatia', 'Genuidade', 'Generosidade', 'Carinho', 'Atraçao', 'Sol', 'Sorriso', 'Cacheada', 'Educada', 'Indecisa', 'Autonoma', 'KKK'
vogais = 'a', 'e', 'i', 'o', 'u'
vogais_encontradas = ''
# For para analisar cada palavra dentro da tupla.
for palavra in varias_palavras:
    # Variável criada para detectar se alguma palavra não tem vogal.
    s_vogal = 0
    print(f'\nA palavra {palavra.upper()} possui as vogais: ', end='')
    # Segundo For para analisar cada letra da palavra dentro da tupla, individualmente.
    for letra in palavra:
        # Condição para saber se tal letra é vogal ou não.
        if letra.lower() in vogais:
            # Variável para ficar mais didático.
            vogais_encontradas = letra
            print(vogais_encontradas.lower(), end=' ')
        else:
            s_vogal += 1
    # Se s_vogal for igual o tamanho da palavra, logo a mesma não tem vogal.
    if s_vogal == len(palavra):
        print('Não foi encontrado', end='')