matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_coluna3 = 0
maior_linha2 = float('-inf')
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite o valor da matriz {[i]}{[j]}: '))
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]
        if j == 2:
            soma_coluna3 += matriz[i][j]
        if i == 1:
            if matriz[i][j] > maior_linha2:
                maior_linha2 = matriz[i][j]
print(40*'-')
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()
print(40*'-')
print(f'Soma dos valores pares: {soma_pares}')
print(f'Soma dos valores da 3ª coluna: {soma_coluna3}')
print(f'Maior valor da 2ª linha: {maior_linha2}')