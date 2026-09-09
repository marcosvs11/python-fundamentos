def leiaInt(msg):
    while True:
        numero = str(input(msg))
        # if numero.isnumeric(): -> Não aceita números negativos
        try:
            numero = int(numero)
            return numero
        # else:
        except ValueError:
            print('Entrada inválida, digite apenas números inteiros!')


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
