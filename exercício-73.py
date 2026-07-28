# Dados da tabela do brasileirão no dia 27/07/2026
brasileirao = 'Palmeiras', 'Flamengo', 'Athletico-PR', 'Fluminense', 'Bragantino', 'Bahia', 'Botafogo', 'Atlético-MG', 'Corinthians', 'Coritiba', 'Cruzeiro', 'São Paulo', 'Vitória', 'Santos', 'Grêmio', 'Internacional', 'Vasco', 'Remo', 'Mirassol', 'Chapecoense'
print(40 * '-')
print(f'Os primeiros CINCO colocados: {', '.join(brasileirao[:5])}.')
print(40 * '-')
print(f'Os últimos 4 colocados: {', '.join(brasileirao[16:20])}.')
print(40 * '-')
print(f'Em ordem alfabética: {', '.join(sorted(brasileirao))}.')
print(40 * '-')
print(f'A Chapeconse está na {brasileirao.index('Chapecoense') + 1}ª posição.')
print(40 * '-')
