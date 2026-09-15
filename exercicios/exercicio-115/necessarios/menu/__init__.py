from necessarios import textos, numeros

def mostrarMenu(msg, lista):
    textos.titulo(msg)
    i = 1
    for item in lista:
        print(f'{i} - {item}')
        i += 1
