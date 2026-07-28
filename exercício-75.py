numeros = []
pares = 0
for i in range(1, 5):
    numero = int(input(f'Digite o {i}° número: '))
    if numero % 2 == 0:
        pares += 1
    numeros.append(numero)
escolhidos = tuple(numeros)
print(f'Os números escolhidos: {escolhidos}')
if escolhidos.count(9) == 0:
    print('O número 9 foi digitado em nenhum momento.')
else:
    print(f'O número 9 foi digitado {escolhidos.count(9)} vezes.')
try:
    print(f'O número 3 foi digitado na {escolhidos.index(3) + 1}ª posição.')
except ValueError:
    print('O número 3 não foi encontrado.')
if pares == 0:
    print('Não foi digitado números PARES.')
else:
    print(f'Foi digitado {pares} números PARES. ')