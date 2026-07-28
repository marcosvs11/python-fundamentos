pares = 0
for i in range(1, 5):
    numero = int(input(f'Digite o {i}° número: '))
    if numero % 2 == 0:
        pares += 1
    if i == 1:
        valor1 = numero
    elif i == 2:
        valor2 = numero
    elif i == 3:
        valor3 = numero
    elif i == 4:
        valor4 = numero
escolhidos = valor1, valor2, valor3, valor4
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