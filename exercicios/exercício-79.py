from time import sleep
i = 1
# Lista vazia para poder usar .append()
valores = []
# Loop infinito para fazer as perguntas até o usuário parar.
while True:
    print()
    # Pergunta + .append(), para adicionar o valor diretamente na lista.
    valores.append(int(input(f'Digite o {i}° valor: ')))
    # Condição para verificar se o último número digitado é repitido ou não.
    if valores.count(valores[-1]) > 1:
        print('Valor inválido por ser duplicado!')
        # Caso repetido, excluo o último elemento
        del valores[-1]
        # Voltar para o ínicio até digitar o número válido
        continue
    else:
        print('Valor ADCIONADO com sucesso!')
    resp = input('Quer adicionar mais números? [S/N]: ').upper().strip()
    # Condição de parada para o usuário.
    if resp != 'S':
        print()
        print('ORGANIZANDO A ORDEM DOS NÚMEROS...')
        sleep(1.5)
        break
    i += 1
# Organização dos números em ordem crescente.
valores.sort()
print(valores)