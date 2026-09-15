from necessarios import numeros

def arqExiste(nomeArquivo):
    try:
        # 'x'cria um arquivo em branco.
        # 'ecoding=utf-8' tranforma em código binário para o computador entender.
        with open(nomeArquivo, 'x', encoding='utf-8') as arquivo:
            pass
    except FileExistsError:
        print('Arquivo encontrado!')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso!')


def addPessoa(nomeArquivo, nome = '<desconhecido>', idade = 0):
    if nome == '':
        nome = '<desconhecido>'
    # saindo do bloco with, o arquivo é fechado automaticamente.
    with open(nomeArquivo, 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{nome};{idade}\n')


def mostrarArquivo(nomeArquivo):
    try:
        with open(nomeArquivo, 'r', encoding='utf=8') as arquivo:
            for linha in arquivo:
                dado = linha.split(';')
                dado[1] = dado[1].replace('\n', '')
                print(f'{dado[0]:<40}{dado[1]:>3} anos')


    except FileNotFoundError:
        print('Esse arquivo ainda não foi criado, digite 1 para criar!')
