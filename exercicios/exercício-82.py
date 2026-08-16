from time import sleep
# Lista completa.
valores = []
# Lista somente com valores pares.
v_pares = []
# Lista somente com valores ímpares.
v_impares = []
# Variável para enumerar o valor digitado.
i = 1
while True:
    try:
        # .append() para adicionar valores direto na lista.
        valores.append(int(input(f'Digite o {i}° valor: ')))
        # Condição para verificar se é par. Else é impar.
        if valores[-1] % 2 == 0:
            # Adionar valor também na lista de números pares.
            v_pares.append(valores[-1])
        else:
            # Else adiciona o valor na lista de números ímpares.
            v_impares.append(valores[-1])
        # Condição de parada.
        resp = input('Quer adicionar mais números: (S/N): ').strip().upper()
        if resp != 'S':
            print('CALCULANDO VALORES...')
            sleep(2)
            break
    # Tratamento de erro para conferir se está digitando número inteiro.
    except ValueError:
        print('Digite um número válido! Tente novamente.')
        continue
    i += 1
print(40*'-')
print(f'Lista Completa: {valores}')
# Condição de exceção, caso não tenha número par.
if len(v_pares) > 0:
        print(f'Lista Com Números Pares Digitados: {v_pares}')
else:
     print('Não foram encontrado valores PARES!')
# Mesmo caso, mas se não tiver número ímpar.
if len(v_impares) > 0:
    print(f'Lista Com Números Ímpares Digitados: {v_impares}')
else:
     print('Não foram encontrado valores ÍMPARES!')