from random import randint
# Uso o randint para gerar 5 números entre 0 a 10.
aleatorios = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
# Mostrar os números gerados.
print(f'Números gerados: {aleatorios}')
# Utilizo a função max para pegar o maior número
print(f'Maior número: {max(aleatorios)}')
# Utilizo a função min para pegar o menor número
print(f'Menor número: {min(aleatorios)}')
