dados = {}
tot_gols = 0
dados['nome'] = str(input('Digite o nome do jogador: ')).strip().upper()
dados['gols'] = []
jogos = int(input('Digite a quantidade de jogos que foram disputados: '))
for i in range(1, jogos + 1):
    qt_gols = int(input(f'Quantidade de GOLS feito na PARTIDA {i}: '))
    dados['gols'].append(qt_gols)
    tot_gols += qt_gols
dados['total'] = tot_gols
print(40 * '-')
print(dados)
print(40 * '-')
print(40 * '-')
for k, c in dados.items():
    print(f'O domínio {k} tem o valor {c}'.center(40))
print(40 * '-')
print(40 * '-')
print(f'ESTASTÍSCAS DO {dados['nome']}'.center(40))
print(40 * '-')
for i, c in enumerate(dados['gols']):
    print(f'Na partida {i+1}, marcou {c} gol'.center(40))
print(f'Total de gols marcados: {dados['total']}'.center(40))