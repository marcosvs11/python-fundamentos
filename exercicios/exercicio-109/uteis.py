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
    resultado = f'R${valor:,.2f}'.replace('.', ',')
    return resultado
