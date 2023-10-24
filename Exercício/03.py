nome = 'Luiz Otávio'
linha = 0
nome_fim = ""

while linha < len(nome):
    letra = nome[linha]
    nome_fim += f'{letra}*'
    linha += 1

print(nome_fim)

