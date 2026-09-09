def notas(boletim, sit=False):
    """
    Função que analisa as notas e classifica em situações.

    Argumentos:
        boletim = uma lista não vazia que pode receber várias notas adicionadas no programa principal.
        sit = permite usuário decidir visualizar a situação dele. Se True, inclui a situação, mas o padrão é False

    Retorna:
        Um dicionário com informações de quantidade de notas, nota maior, nota menor, média e situação (sendo opcional).
    """
    avaliacao = {}
    soma = 0
    avaliacao['total'] = (len(boletim))
    avaliacao['maior'] = max(boletim)
    avaliacao['menor'] = min(boletim)
    for nota in boletim:
        soma += nota
    media = soma / len(boletim)
    avaliacao['média'] = media
    if sit:
        if media < 6:
            situacao = 'REPROVADO'
        elif media < 7:
            situacao = 'RECUPERAÇÃO'
        else:
            situacao = 'APROVADO'
        avaliacao['situação'] = situacao

    return avaliacao

c = 1
resp = 'S'
rendimento = []
while resp != 'N':
    try:
        nt = float(input(f'Digite a {c}° nota: '))
    except ValueError:
        print('Entrada inválida, digite apenas valores númericos!')
        continue
    if nt < 0 or nt > 10:
        print('Entrada inválida, digite notas entra 0 e 10!')
        continue
    rendimento.append(nt)
    while True:
        resp = str(input('Quer adicionar mais? (S/N): ')).strip().upper()
        if resp in ('S', 'N'):
            break
        print('Entrada inválida, digite apenas "N" ou "S".')
    c += 1

while True:
    # Pergunta sobre a situação do aluno.
    perg = str(input('Quer visualizar a situação? (S/N): ')).strip().upper()
    if perg in ('S', 'N'):
        break
    print('Entrada inválida, digite apenas "N" ou "S".')

# Valor Booleano
mostrarSituacao = perg == 'S'

resultado = notas(rendimento, mostrarSituacao)
print(resultado)
# help(notas) -> Quando for necessário, só retirar.
