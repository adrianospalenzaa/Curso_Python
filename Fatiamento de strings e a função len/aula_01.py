"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]   i = inicio, f = fim, p = passo
Obs.: a função len retorna a qtd
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[::-1])  # inverte a string
print(variavel[0:8:2])  # pega do inicio ao fim pulando de 2 em 2
print(len(variavel))  # retorna a qtd de caracteres da str
print(variavel[0:9]) # pega do inicio ao fim

