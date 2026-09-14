def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
            return numero
        except ValueError:
            print('Entrada inválida, digite um número inteiro!')

def leiaFloat(msg):
    while True:
        try:
            numero = float(input(msg).replace(',', '.'))
            return numero
        except ValueError:
            print('Entrada inválida, digite um número válido!')


numI = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {numI}')

numF = leiaFloat('Digite um número real: ')
print(f'Você digitou o número {numF}')
