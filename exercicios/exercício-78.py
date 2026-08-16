# Criei uma lista para ir adcionando números dentro do For.
numeros = []
# Menor número possível para garantir a primeira iteração.
maior = float('-inf')
# Mesmo raciocínio, só que dessa vez o menor número possível.
menor = float('inf')
for posicao, i in enumerate(range(1,6), start=1):
    numeros.append(int(input(f'Digite o {i}° número: ')))
    if numeros[i-1] > maior:
        maior = numeros[i-1]
        pos_maior = [posicao]
    elif numeros[i-1] == maior:
        pos_maior.append(posicao)
    if numeros[i-1] < menor:
        menor = numeros[i-1]
        pos_menor = [posicao]
    elif numeros[i-1] == menor:
        pos_menor.append(posicao)
if len(pos_maior) > 1:
    sintaxe_maior = f'digitado nas posições {pos_maior}.'
else:
    sintaxe_maior = f'digitado na posição {pos_maior}'
if len(pos_menor) > 1:
    sintaxe_menor = f'digitado nas posições {pos_menor}'
else:
    sintaxe_menor = f'digitado na posição {pos_menor}'
print(f'O maior número é o {maior}, {sintaxe_maior}')
print(f'O menor número é o {menor}, {sintaxe_menor}')