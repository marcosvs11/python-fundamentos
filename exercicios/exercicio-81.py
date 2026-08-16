from time import sleep
valores = []
i = 1
while True:
    # Tratamento de erro necessário.
    try:
        # Lista adcionando itens até o usuário parar.
        valores.append(int(input(f'Digite o {i}° número: ')))
        # Condição de parada;
        resp = input('Quer digitar mais números? (S/N): ').strip().upper()
        if resp != 'S':
            print('CARREGANDO RESULTADOS...')
            sleep(2)
            break
    except ValueError:
        print('Número Inválido! Tente Novamente...')
        continue
    # Variável para manter controle de quantos números estão sendo adcionados.
    i += 1
print(40*'-')
print(f'Foram digitados {i} números!')
# Declaração para realizar a ordem decrescente.
valores.sort(reverse=True)
print(f'Listas dos números decrescente: {valores}')
# Condição para mostrar a posição do 5, caso esteja na lista.
if 5 in valores:
    print(f'O valor 5 foi digitado na posição {valores.index(5) + 2}!')
else:
    print('Não foi encontrado o valor 5!')
