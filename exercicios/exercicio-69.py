from time import sleep
cont = 1
mais_18 = 0
quant_masculino = 0
quant_feminino_20 = 0
sep = 40 * '='
tit = 'Cadastrando Pessoas'.center(40, ' ')
print(sep)
print(tit)
print(sep)
# Loop infinito propositalmente.
while True:
    try:
        # Cadastro individual com idade e sexo.
        idade = int(input(f'Digite a idade da {cont}° pessoa: '))
        sexo = input('Qual o sexo? (M/F): ').upper().strip()
        # Condição caso o sexo pré determinado não é ativado.
        if sexo != 'M' and sexo != 'F':
            print('Opção inválida!\nTente novamente.')
            continue
        # Condição para que pessoas com mais de 18 anos sejam contadas.
        if idade >= 18:
            mais_18 += 1
        # Condição para que pessoas com o sexo masculino sejam contadas.
        if sexo == 'M':
            quant_masculino += 1
        # Condição para mulheres com mais de 20 anos sejam contadas.
        if sexo == 'F' and idade < 20:
            quant_feminino_20 += 1
        # Condição para usuário decidir se vai cadastrar mais ou não.
        resp = input('Quer cadastrar mais pessoas? (S/N): ').upper().strip()
        print(40*'-')
        cont += 1
        # Parada - Quando o usuário decidir encerrar.
        if resp != 'S':
            print('CARREGANDO RESULTADO...')
            sleep(1)
            break
    except ValueError:
        print('Está pergunta aceita apenas números!\nTente novamente.')
        continue
# Formatação de saída.
print(40*'-')
print(f'Quantidade de pessoas com mais de 18 anos: {mais_18}')
print(f'Quantidade de homens: {quant_masculino}')
print(f'Quantidade de mulheres menores de 20 anos: {quant_feminino_20}')
print(40*'-')