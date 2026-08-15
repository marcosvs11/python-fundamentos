from time import sleep
alunos = []
dados = []
media = []
i = 1
boletim = ''
while True:
    nome = str(input('Digite o nome do aluno: ')).strip().capitalize()
    if nome == '':
        print('Nome inválido, tente novamente!')
        continue
    while True:
        try:
            nota1 = float(input('Digite a 1° nota: '))
            if nota1 > 10 or nota1 < 0:
                print('Número inválido, tente novamente!')
                continue
            break
        except ValueError:
            print('Este programa aceita apenas números.\nTente novamente!')
            continue
    while True:
        try:
            nota2 = float(input('Digite a 2° nota: '))
            if nota2 > 10 or nota2 < 0:
                print('Número inválido, tente novamente!')
                continue
            break
        except ValueError:
            print('Este programa aceita apenas números.\nTente novamente!')
            continue
    media = (nota1 + nota2) / 2
    dados.append(nome)
    dados.append(nota1)
    dados.append(nota2)
    dados.append(media)
    alunos.append(dados[:])
    dados.clear()
    resp = str(input('Quer adicionar mais alunos? (S/N): ')).strip().upper()
    if resp != 'S':
        print('CALCULANDO RESULTADOS...')
        sleep(2)
        break
# Criei uma função de uma linha para utilizar como parâmetro de organização o índice 3 da lista 'alunos', ou seja, a média.
alunos.sort(key=lambda x: x[3], reverse=True)
print(40 * '-')
print('MÉDIA FINAL'.center(40))
print(40 * '-')
for individual in alunos:
    print(f'{i}° Lugar → {individual[0]}: {individual[3]:.2f} ')
    i += 1
print()
while boletim != '999':
    boletim = str(input('Digite o nome do boletim que deseja (999 para interromper): ')).capitalize().strip()
    print(40 * '-')
    for individual in alunos:
        if boletim in individual[0]:
            print(f'NOTAS ALUNO(A) {individual[0]}'.center(40).upper())
            print(40 * '-')
            print(f'Nota 1: {individual[1]}')
            print(f'Nota 2: {individual[2]}')
            print()
print('ENCERRANDO...')

