def dobrar (valor = 0):
    """
    Retorna o dobro do valor recebido.
    """
    resultado = valor * 2
    return resultado

def metade(valor = 0):
    """
    Retorna a metade do valor recebido.
    """
    resultado = valor / 2
    return resultado

def diminuir(valor = 0, taxa = 0):
    """
    Retorna o valor com um descrécimo percentual de acordo com a taxa recebida.
    """
    resultado = valor - (valor * (taxa / 100))
    return resultado

def aumentar(valor = 0, taxa = 0):
    """
    Retorna o valor com um acréscimo percentual de acordo com a taxa recebida
    """
    resultado = valor + (valor * (taxa / 100))
    return resultado

def moeda(valor = 0):
    """
    Retorna o valor com formatação monetária em reais e tranforma em strings.
    """
    resultado = f'R${valor:,.2f}'.replace('.', ',')
    return resultado
