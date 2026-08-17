from random import randint
from time import sleep
jogadores = {}
c = 1
for i in range(4):
    jogadores[f'jogador {i+1}'] = randint(1, 6)
print(40 * '-')
print('Campeonato de Dado'.center(40))
print(40 * '-')
for k, v in jogadores.items():
    k = f'{k}'.upper()
    print(f'O {k} tirou o N° {v}')
    sleep(1)
print('CARREGANDO RANKING...')
sleep(1)
print(40 * '-')
print('RANKING'.center(40))
print(40 * '-')
ranking = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))
for k, v in ranking.items():
    k = f'{k}'.upper()
    print(f'Em {c}° lugar → O {k} com {v}')
    c += 1