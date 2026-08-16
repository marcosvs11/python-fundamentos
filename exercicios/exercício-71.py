from time import sleep
sep = 40 * '='
tit = 'Banco Vieira Center'.center(40, ' ')
while True:
    try:
        # Variáveis para definir as células que será usadas.
        ced50 = ced20 = ced10 = ced1 = 0
        print(sep)
        print(tit)
        print(sep)
        valor = int(input('Digite o valor para sacar: '))
        # A condição para que quando o valor chegarem 0 ele encerra.
        while valor != 0:
            if valor >= 50:
                ced50 = valor // 50
                valor = valor - (ced50 * 50)
            elif valor >= 20:
                ced20 = valor // 20
                valor = valor - (ced20 * 20)
            elif valor >= 10:
                ced10 = valor // 10
                valor = valor - (ced10 * 10)
            else:
                ced1 = valor // 1
                valor = valor - (ced1 * 1)
        print('CALCULANDO CÉDULAS...')
        sleep(2)
        print('CÁLCULO CONCLUÍDO!')
        sleep(1)
        # Resultado final
        if ced50 != 0:
            print(f'{ced50} notas de R$50,00 recebidas.')
        if ced20 != 0:
            print(f'{ced20} notas de R$20,00 recebidas.')
        if ced10 != 0:
            print(f'{ced10} notas de R$10,00 recebidas.')
        if ced1 != 0:
            print(f'{ced1} notas de R$1,00 recebidas.')
        print(40 * '-')
        sleep(2)
        resp = input('Quer sacar mais dinheiro? (S/N): ').upper().strip()
        if resp != 'S':
            print('Encerrando Operação...')
            break
    except ValueError:
        print('Está pergunta aceita apenas números inteiros!\nTente novamente.')