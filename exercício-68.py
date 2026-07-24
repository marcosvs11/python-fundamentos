from time import sleep
from random import randint
numero_comp = 0
vitoria = 0
sep = 40 * '='
tit = 'ÍMPAR OU PAR?'.center(40, ' ')
print(sep)
print(tit)
print(sep)
while True:
    escolha = input('Você quer PAR ou ÍMPAR? (I/P): ').strip().upper()
    # Variáveis para mostrar a escolha do computador.
    if escolha == 'I':
        computador = 'PAR'
    elif escolha == 'P':
        computador = 'ÍMPAR'
    # Caso o usuário digite uma letra diferente.
    else:
        print('Opção inválida, tente novamente!')
        continue
    print(f'O computador ficou com {computador}.')
    print(40 * '-')
    try: 
        numero = int(input('Digite o número escolhido: '))
        # Escolha aleatória de um número entre 0 e 20
        numero_comp = randint(0, 20)
        sleep(0.5)
        print(f'O computador escolheu o número {numero_comp}.')
        soma = numero_comp + numero
        # Variáveis necessárias para mostrar na mensagem sobre a escolha de cada um.
        if soma % 2 == 0:
            parcial = 'PAR' 
        else: 
            parcial = 'ÍMPAR'
        # Condição de vitória do usuário.
        if soma % 2 == 0 and escolha == 'P' or soma % 2 == 1 and escolha == 'I':
            resultado = 'VOCÊ FOI O VENCEDOR!'
            vitoria += 1
        # Senão, o computador vence.
        else:
            resultado = 'VOCÊ PERDEU!'
        print(40 * '-')
        print('PROCESSANDO...')
        print(40 * '-')
        sleep(1)
        print(f'O número {soma} é {parcial}')
        print(resultado)
        # O exercício para quando o usuário perde.
        if resultado == 'VOCÊ PERDEU!':
            print(f'Mas venceu {vitoria} vezes!')
            break
        else:
            print('Vamos jogar novamente, até eu ganhar!')
            print(40 * '-')
            sleep(1)
    except ValueError:
        print('Está pergunta aceita apenas números inteiro!\nTente novamente.')
        continue