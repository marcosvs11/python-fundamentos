def leiaDinheiro(msg):
    """
    Recebe uma string para realizar a validação para poder transformar em float.
    """
    while True:
        numerico = str(input(msg)).strip().replace(',', '.')
        # Aceita, no máximo, um separador decimal!
        if numerico.replace('.', '', 1).isdecimal():
            return float(numerico)
        else:
            print('Entrada inválida, digite um número corretamente!')
