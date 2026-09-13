#__init__ = inicialização
def dobrar (valor = 0, form=False):
    """
    Retorna o dobro do valor recebido. Se form = True, devolverá uma string monetária.
    """
    resultado = valor * 2
    if form:
        resultado = moeda(resultado)
    return resultado

def metade(valor = 0, form=False):
    """
    Retorna a metade do valor recebido. Se form = True, devolverá uma string monetária.
    """
    resultado = valor / 2
    if form:
        resultado = moeda(resultado)
    return resultado

def diminuir(valor = 0, taxa = 0, form=False):
    """
    Retorna o valor com um descrécimo percentual de acordo com a taxa recebida. Se form = True, devolverá uma string monetária
    """
    resultado = valor - (valor * (taxa / 100))
    if form:
        resultado = moeda(resultado)
    return resultado

def aumentar(valor = 0, taxa = 0, form=False):
    """
    Retorna o valor com um acréscimo percentual de acordo com a taxa recebida. Se form = True, devolverá uma string monetária
    """
    resultado = valor + (valor * (taxa / 100))
    if form:
        resultado = moeda(resultado)
    return resultado

def moeda(valor = 0):
    """
    Retorna o valor com formatação monetária em reais e tranforma em strings.
    """
    resultado = f'R${valor:.2f}'.replace('.', ',')
    return resultado

def resumo(valor, taxaAcrescimo, taxaDecrescimo):
    sep = 40 * '-'
    tit = 'RESUMO MONETÁRIO'.center(40, ' ')
    print(sep)
    print(tit)
    print(sep)
    print(f'{"Valor recebido:":<21}{moeda(valor):>11}')
    print(f'{"Dobro do valor:":<21}{dobrar(valor, form=True):>11}')
    print(f'{"Metade do valor":<21}{metade(valor, form=True):>11}')

    descricao = f'Acréscimo de {taxaAcrescimo}%:'
    print(f'{descricao:<21}{aumentar(valor, taxaAcrescimo, form=True):>11}')

    descricao = f'Decréscimo de {taxaDecrescimo}%:'
    print(f'{descricao:<21}{diminuir(valor, taxaDecrescimo, form=True):>11}')
