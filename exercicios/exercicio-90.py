aluno = {} 
aluno['nome'] = str(input('Digite o nome do aluno(a): ')).strip().capitalize()
aluno['media'] = float(input(f'Digite a média do {aluno['nome']}: '))
if aluno['media'] < 6:
    aluno['situacao'] = 'REPROVADO'
elif aluno['media'] < 7:
    aluno['situacao'] = 'RECUPERAÇÃO'
else:
    aluno['situacao'] = 'APROVADO'
print(40 * '-')
print(f'O nome do aluno(a) é {aluno['nome']}...')
print(f'O {aluno['nome']} ficou com a média {aluno['media']}...')
print(f'Por isso, ele(a) foi {aluno['situacao']}!')

# Poderia usar:
# for k, v in aluno.items():
#     print(f'{k} é igual a {v}')
