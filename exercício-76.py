produtos_preços = 'Playstation 5', 3799.97, 'Geladeira Frost Free', 2197.83, 'Amor Recíproco', 9999999.99, 'Claude Max', 549.99, 'MacBook Air M1', 2899.89, 'Camiseta I - Corinthians 26/27', 379.99
print(50*'=')
print(f'{'Tabela de Preços - Vieira Atacado':^50}')
print(50*'=')
# Usando o for e com o passo 2, consigo trazer as duas informações que preciso mostrar na primeira linha.
for i in range(0, len(produtos_preços), 2):
    # Mostra o nome do produto e em seguida o preço.
    print(f'{produtos_preços[i]:.<35}RS{produtos_preços[i+1]:,.2f}')