def dobrar(numero):
    """
    Função que dobra um número.

    Argumentos:
        numero = valor escolhido pelo usuário.

    Retorna:
        O dobro do valor escolhido pelo usuário.
    """

    resultado = numero * 2
    return resultado

def metade(numero):
    """
    Função que calcula a metade de um número.

    Argumentos:
        numero = valor escolhido pelo usuário.

    Retorna:
        A metade do valor escolhido pelo usuário.
    """

    resultado = numero / 2
    return resultado

def aumentar(numero, taxa):
    """
    Função que calcula aumento do número inicial em porcentagem.

    Argumentos:
        numero = valor escolhido pelo usuário.
        taxa = valor, em porcentagem, que será aumentado.

    Retorna:
        O aumentado de acordo com a porcentagem desejada e o valor escolhido pelo usuário.
    """

    resultado = numero + (numero * taxa / 100)
    return resultado

def diminuir(numero, taxa):
    """
    Função que calcula o desconto do número inicial em porcentagem.

    Argumentos:
        numero = valor escolhido pelo usuário.
        taxa = valor, em porcentagem, que será descontado.

    Retorna:
        O desconto de acordo com a porcentagem desejada e a taxa escolhida pelo usuário.
    """

    resultado = numero - (numero * taxa / 100)
    return resultado
