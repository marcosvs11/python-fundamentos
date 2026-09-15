from necessarios import menu, numeros, textos, arquivos

arqNome = 'cadastramento.txt'
arquivos.arqExiste(arqNome)

while True:
    menu.mostrarMenu('CADASTRAMENTO', ['Adicionar uma pessoa', 'Listar pessoas cadastradas', 'Encerrar programa'])
    opcao = numeros.leiaInt('Digite a sua opção: ')

    if opcao == 1:
        textos.titulo('CADASTRO NOVO')
        nome = str(input('Digite o seu nome: ')).strip()
        idade = numeros.leiaInt('Digite a sua idade: ')
        arquivos.addPessoa(arqNome, nome, idade)

    elif opcao == 2:
        textos.titulo('LISTAS DOS CADASTRADOS')
        arquivos.mostrarArquivo(arqNome)

    elif opcao == 3:
        print()
        print('ENCERRANDO PROGRAMA...'.center(50, ' '))
        break

    else:
        print('Entrada inválida, digite uma opção válida!')
