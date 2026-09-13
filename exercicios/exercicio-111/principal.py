from utilidadescev import moeda
from utilidadescev import dado

valor = dado.leiaDinheiro('Digite um valor: R$')
taxaAcrescimo = dado.leiaDinheiro('Digite uma taxa em porcentagem para acréscimo: ')
taxaDecrescimo = dado.leiaDinheiro('Digite outra taxa percentual para decréscimo: ')
moeda.resumo(valor, taxaAcrescimo, taxaDecrescimo)
