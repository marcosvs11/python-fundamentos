import os
# Permite que uso o 'cat' para exibir ajuda diretamente no terminal, evitando o paginador do linux.
os.environ['MANPAGER'] = 'cat'

def ajuda(msg):
    """
    Exibição de documentação da função ou biblioteca/módulo informado.
    """
    help(msg)

# Programa principal
while True:
    print(40 * '-')
    print('SISTEMA DE AJUDA'.center(40, ' '))
    print(40 * '-')
    resp = str(input('Digite Função ou Biblioteca ("Fim" para sair): ')).strip()
    if resp.lower() == 'fim':
        print('Desligando...')
        break
    elif not resp:
        print('Digite uma Função ou Biblioteca válida!')
        continue
    else:
        ajuda(resp)
