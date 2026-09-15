def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
            if numero < 0:
                print('Entrada inválida, digite um número positivo!')
                continue
            return numero
        except ValueError:
            print('Entrada inválida, digite um número inteiro!')
