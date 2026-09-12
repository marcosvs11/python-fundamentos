import uteis

valor = float(input('Digite um valor: R$'))
dobro = uteis.dobrar(valor, True)
metade = uteis.metade(valor, True)
print(f'O dobro de {uteis.moeda(valor)} é {dobro}')
print(f'A metade de {uteis.moeda(valor)} é {metade}')
taxa = float(input('Digite uma taxa em porcentagem : '))
aumento = uteis.aumentar(valor, taxa, True)
desconto = uteis.diminuir(valor, taxa, True)
print(f'Aumentando {taxa}% de {uteis.moeda(valor)} é {aumento}')
print(f'Descontando {taxa}% de {uteis.moeda(valor)} é {desconto}')
