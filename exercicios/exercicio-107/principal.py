import uteis

valor = float(input('Digite um valor: R$'))
dobro = uteis.dobrar(valor)
metade = uteis.metade(valor)
print(f'O dobro de {valor} é {dobro}')
print(f'A metade de {valor} é {metade}')
taxa = float(input('Digite uma taxa em porcentagem : '))
aumento = uteis.aumentar(valor, taxa)
desconto = uteis.diminuir(valor, taxa)
print(f'Aumentando {taxa}% de {valor} é {aumento}')
print(f'Descontando {taxa}% de {valor} é {desconto}')
