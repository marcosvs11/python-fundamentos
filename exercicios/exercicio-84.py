pessoas = []
dados = []
maior = float('-inf')
menor = float('inf')
i = 1
while True:
    dados.append(input(f'Nome da {i}° pessoa:  ').capitalize())
    dados.append(float(input(f'Peso: ')))
    if dados[1] > maior:
        maior = dados[1]
    if dados[1] < menor:
        menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    i += 1
    resp = input('Quer adicionar mais pessoas? (S/N): ').strip().upper()
    if resp != 'S':
        print('GERANDO RESULTADO...')
        break
print(50*'-')
print(f'Os dados cadastrados foram: {pessoas}')
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso cadastrado foi {maior}kg, registrado por: ', end='')
for individual in pessoas:
    if individual[1] == maior:
        print(f'{individual[0]} - ', end='')
print()
print(f'O menor peso cadastrado foi {menor}kg, registrado por: ', end='')
for individual in pessoas:
    if individual[1] == menor:
        print(f'{individual[0]} - ', end='')
