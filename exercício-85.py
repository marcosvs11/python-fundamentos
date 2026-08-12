valores = []
pares = []
impares = []
for i in range (7):
    numero = int(input(f'Digite o {i+1}° valor: '))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
pares.sort()
impares.sort()
valores.append(pares[:])
valores.append(impares[:])
print(f'Lista inteira: {valores}')
if len(pares) == 0:
    valores[0] = 'Nenhum número PAR encontrado!'
print(f'Valores PARES: {valores[0]}')
if len(impares) == 0:
    valores[1] = 'Nenhum número ÍMPAR encontrado!'
print(f'Valores ÍMPARES: {valores[1]}')