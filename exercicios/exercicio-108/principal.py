import uteis

valor = float(input('Digite um valor: R$'))
dobro = uteis.dobrar(valor)
metade = uteis.metade(valor)
print(f'O dobro de {uteis.moeda(valor)} é {uteis.moeda(dobro)}')
print(f'A metade de {uteis.moeda(valor)} é {uteis.moeda(metade)}')
taxa = float(input('Digite uma taxa em porcentagem : '))
aumento = uteis.aumentar(valor, taxa)
desconto = uteis.diminuir(valor, taxa)
print(f'Aumentando {taxa}% de {uteis.moeda(valor)} é {uteis.moeda(aumento)}')
print(f'Descontando {taxa}% de {uteis.moeda(valor)} é {uteis.moeda(desconto)}')
