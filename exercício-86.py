matriz = [[], [], []]
for i in range(0,3):
    for j in range(0,3):
        numeros = int(input(f'Digite a matriz [{i}][{j}]: '))
        if i == 0:
            matriz[0].append(numeros)
        elif i == 1:
            matriz[1].append(numeros)
        else:
            matriz[2].append(numeros)
print(30 * '-')
for linha in matriz:
    print()
    for num in linha:
        print(f'[{num:^5}]', end='')
        