from time import sleep
total = 0
mais_mil = 0
# Para garantir que seja feita a primeira iteração.
preço_menor = float('inf')
mais_barato = ''
sep = 40 * '='
tit = 'Mercado Vieira'.center(40, ' ')
while True:
    try:
        print(sep)
        print(tit)
        print(sep)
        # Utilizei capitalize porque pretendo usar no futuro.
        produto = input('Digite o nome do produto: ').strip().capitalize()
        preço = float(input('Digite o preço: R$'))
        # Soma do total.
        total += preço
        # Para mostrar produtos acima de 1000 reais
        if preço > 999:
            mais_mil += 1
        # Para mostrar o nome do produto mais barato
        if preço < preço_menor:
            preço_menor = preço
            mais_barato = produto
        # Condição de parada
        resp = input('Quer adicionar mais produtos? (S/N): ').strip().upper()
        if resp != 'S':
            print('Calculando o valor final...')
            sleep(1)
            break
    except ValueError:
        print('Está pergunta aceita apenas números!\nTente novamente.')
        continue
print(40*'-')
print(f'Valor Total: R${total:,.2f}.')
print(f'Produtos acima de R$1.000,00: {mais_mil}.')
print(f'O produto {mais_barato} foi o mais barato.')
    