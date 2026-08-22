from time import sleep
pessoa = {}
agenda = []
mulheres = []
idade_alta = []
media_idade = 0
while True:
    pessoa['nome'] = str(input('Digite o nome: ')).title()
    # Loop até digitar o sexo correto.
    while True:
        pessoa['sexo'] = str(input('Sexo M ou F: ')).strip().upper()
        if pessoa['sexo'] != 'M' and pessoa['sexo'] != 'F':
            print('Sexo inválido. Por gentileza, digite apenas M ou F.')
            continue
        break
    # Lista com mulheres.
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Digite sua idade: '))
    media_idade += pessoa['idade']
    # Copy(), pois dicionário não funciona [:].
    agenda.append(pessoa.copy())
    resp = str(input('Deseja continuar? (S/N): ')).strip().upper()
    if resp != 'S':
        print('CARREGANDO RESULTADOS...')
        sleep(2)
        break
print(40 * '-')
# Quantidade de pessoas.
quant_pessoas = len(agenda)
# Processo para média de idades.
media_idade = media_idade / quant_pessoas
# Navegando pela lista agenda para procurar nos dicionário a idade de cada um.
for i in range(len(agenda)):
    if agenda[i]['idade'] > media_idade:
        idade_alta.append(agenda[i]['nome'])
print(f'Foram cadastradas {quant_pessoas} pessoas.')
print(f'A média de idade do grupo é de {media_idade:.1f} anos.')
if len(mulheres) == 0:
    print('Não foram cadastradas mulheres no grupo.')
else:
    print(f'Mulheres no grupo: ', end='')
    for i, mulher in enumerate(mulheres):
        # No último nome a vírgula some.
        if i == len(mulheres) - 1:
            print(f'{mulher}.', end='')
        else:
            print(f'{mulher}', end=', ')
print()
if len(idade_alta) == 0:
    print('Nenhuma pessoa detectada com idade superior a média do grupo.')
else:
    print(f'Pessoas com a idade superior a média do grupo: ', end='')
    for i, individuo in enumerate(idade_alta):
        # Novamente, retiro a vírgula.
        if i == len(idade_alta) - 1:
            print(f'{individuo}.', end='')
        else:
            print(f'{individuo}', end=', ')