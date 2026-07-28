# Tupla criado com os números em extenso.
numeros = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    escolhido = int(input('Digite um número entre 0 e 20: '))
    # Erro de digitação.
    if escolhido < 0 or escolhido > 20:
        print('Número inválido. Tente novamente!')
        continue
    # O número escolhido pelo usuário vira o índice da tupla e que traz o mesmo por extenso.
    print(f'Você escolheu o número {numeros[escolhido].upper()}')
    break