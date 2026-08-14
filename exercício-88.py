from random import sample
from time import sleep
q_jogos = int(input(('Digite quando jogos você quer: ')))
jogos_completo = []
dados = []
c = 0
print(40 * '-')
print('Jogos Sorteados'.center(40))
print(40 * '-')
for i in range(q_jogos):
    sorteados = sample(range(1, 61), 6)
    jogos_completo.append(sorteados)
for jogo in jogos_completo:
    c += 1
    print(f'Jogo {c}: {jogo}')
    sleep(1)
