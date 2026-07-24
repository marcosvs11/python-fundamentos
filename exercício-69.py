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
while True:
    try:
        idade = int(input(f'Digite a idade da {cont}° pessoa: '))
        sexo = input('Qual o sexo? (M/F): ').upper().strip()
        if sexo != 'M' and sexo != 'F':
            print('Opção inválida!\nTente novamente.')
            continue
        if idade >= 18:
            mais_18 += 1
        if sexo == 'M':
            quant_masculino += 1
        if sexo == 'F' and idade < 20:
            quant_feminino_20 += 1
        resp = input('Quer cadastrar mais pessoas? (S/N): ').upper().strip()
        print(40*'-')
        cont += 1
        if resp != 'S':
            print('CARREGANDO RESULTADO...')
            sleep(1)
            break
    except ValueError:
        print('Está pergunta aceita apenas números!\nTente novamente.')
        continue
print(40*'-')
if mais_18 == quant_masculino == quant_feminino_20 ==0:
    mais_18 = quant_masculino = quant_feminino_20 = 'Não foi encontrado nos cadastros!'
print(f'Quantidade de pessoas com mais de 18 anos: {mais_18}')
print(f'Quantidade de homens: {quant_masculino}')
print(f'Quantidade de mulheres menores de 20 anos: {quant_feminino_20}')
print(40*'-')