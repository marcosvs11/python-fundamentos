from utilidadescev import moeda

valor = float(input('Digite um valor: R$'))
taxaAcrescimo = float(input('Digite uma taxa em porcentagem para acréscimo: '))
taxaDecrescimo = float(input('Digite outra taxa percentual para decréscimo: '))
moeda.resumo(valor, taxaAcrescimo, taxaDecrescimo)
