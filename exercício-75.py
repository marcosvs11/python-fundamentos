# Listas são mutáveis, por isso começarei com eles.
numeros = []
pares = 0
for i in range(1, 5):
    numero = int(input(f'Digite o {i}° número: '))
    # Verificação para contar pares.
    if numero % 2 == 0:
        pares += 1
    # Função para adicionar cada número digitado na lista criada.
    numeros.append(numero)
# Conversão da lista para tuplas
escolhidos = tuple(numeros)
print(f'Os números escolhidos: {escolhidos}')
# Função para contar quantas vezes aparece.
if escolhidos.count(9) == 0:
    print('O número 9 foi digitado em nenhum momento.')
else:
    print(f'O número 9 foi digitado {escolhidos.count(9)} vezes.')
# A função index necessita de um try/except para rodar sem dar erro quando não encontra.
try:
    print(f'O número 3 foi digitado na {escolhidos.index(3) + 1}ª posição.')
except ValueError:
    print('O número 3 não foi encontrado.')
if pares == 0:
    print('Não foi digitado números PARES.')
else:
    print(f'Foi digitado {pares} números PARES. ')