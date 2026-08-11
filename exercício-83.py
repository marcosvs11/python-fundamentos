# Loop infinito para o usuário digitar a frase correta.
while True:
    # O verificador vai voltar para o 0.
    verificar_parenteses = 0
    frase = input('Digite uma frase qualquer que tenha PARÊNTESES: ').strip().upper()
    # Loop For para passar letra por letra.
    for letra in frase:
        # Verificando se tem abertura do parênteses.
        if letra == '(':
            # Se sim, +1 para o verificador.
            verificar_parenteses += 1
        # Verificando se tem o fechamento.
        elif letra == ')':
            # Se sim, -1 para o verificador
            verificar_parenteses -= 1
        # Se o verificador ficar negatiovo, significa que o usuário fechou o parênteses sem ter aberto um.
        # Isso já configura como um erro, desse modo, interrompo o programa e ja imprimo a mensagem de ERRO.
        if verificar_parenteses < 0:
            break
    # Mensagem personalizado caso não tenha parênteses.
    if frase.count('(') == 0 and frase.count(')') == 0:
        print('Está frase não possui PARÊNTESES!')
        break
    # Se verificador igual a 0, significa que teve a abertura e fechamento dos parênteses de forma correta.
    if verificar_parenteses == 0:
        print('Parabéns, o seu uso de PARÊNTESES está impecável!')
        break
    print('Identidicado o uso incorreto PARÊNTESES!\nTente novamente...')
    print()
