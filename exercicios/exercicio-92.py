from datetime import date
ano_atual = date.today().year
dados = {}
dados['nome'] = str(input('Digite o seu nome: ')).title()
ano_nasc = int(input('Ano de nascimento: '))
dados['idade'] = ano_atual - ano_nasc
dados['ctps'] = int(input('Digite o N° da sua CTPS (0 se não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Digite o ano em que foi contratado: '))
    dados['salário'] = float(input('Digite o seu salário: R$'))
    dados['aposentadoria'] = (35 - (ano_atual - dados['contratação'])) + dados['idade']
    if dados['aposentadoria'] <= 0:
        dados['aposentadoria'] = 'tempo mínimo de contribuição atingido'
print(40 * '-')
for k, v in dados.items():
    print(f'{k} tem o valor {v}')