"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')
"""----------------------------------------------"""
# Exemplo 2

contador = 0

while contador <= 10:
    contador = contador + 1
    print(contador)

print('Acabou')
"""----------------------------------------------"""
# Exemplo 3
'Operadores de atribuição com operadores aritméticos'

"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""
contador = 10

###

contador /= 5
print(contador)