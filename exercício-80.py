valores = []
# For para digitar os números da lista.
for i in range(5):
    valores.append(int(input(f'Digite o {i + 1}° valor: ')))
# For para fazer a verificação individual pelo indice da lista.
for num in range(5):
    # Declaração para reniciar e entrar no while
    c = 0
    # Ele sempre vai parar antes do último termo para a verificação com o num funcionar.
    while c != len(valores) - 1:
        # O objetivo é encontrar o menor número e jogar ele para trás.
        if valores[num] < valores[c]:
            valores[num], valores[c] = valores[c], valores[num]
        c +=1
print(valores)