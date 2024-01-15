import re
import random


#nove_digitos = ''

#for i in range(9):
    #nove_digitos += str(random.randint(0, 9))
#print(nove_digitos)



# 1. Receber o CPF
lista_cpf = []  # Lista para armazenar os CPFs
lista_numerica = []
lista_mult = []
soma = 0
i = 0
peso = 10

# CPF digitado e armazenado na lista_cpf
lista_cpf = input('Digite o CPF:\n ')

# Remove os caracteres não numéricos da lista_cpf
lista_cpf = ''.join(filter(str.isdigit, lista_cpf))

#opção 2 para remover os caracteres não numéricos da lista_cpf
# Remove os caracteres não numéricos da lista_cpf
#lista_cpf = re.sub('[^0-9]', '', lista_cpf)

# Converte a lista_pdf para uma lista de inteiros
lista_numerica = [int(digito) for digito in lista_cpf]


while i <= 8:
    lista_mult = peso * lista_numerica[i]  # Multiplicando cada um dos valores por uma contagem regressiva começando de 10
    soma = soma + lista_mult  # Somando cada resultado
    i = i + 1
    peso = peso - 1

resto = (soma *10) % 11  # obitendo o resto da divisão

if resto > 9:
    primeiro_digito = 0  # Se o resultado anterior for maior que 9: resultado é 0
else:
    primeiro_digito = resto  # contrário disso: resultado é o valor e o resto da divisão


# Segundo dígito
soma = 0
i = 0
peso = 11
#lista_numerica.append(primeiro_digito)  # Adicionando o primeiro dígito na lista_numerica

while i <= 9:
    lista_mult = peso * lista_numerica[i]  # Multiplicando cada um dos valores por uma contagem regressiva começando de 11
    soma = soma + lista_mult  # Somando cada resultado
    i = i + 1
    peso = peso - 1

resto = (soma *10) % 11  # obitendo o resto da divisão

if resto > 9:
    segundo_digito = 0  # Se o resultado anterior for maior que 9: resultado é 0
else:
    segundo_digito = resto

#lista_numerica.append(segundo_digito)  # Adicionando o segundo dígito na lista_numerica

print('primeiro_digito: ', primeiro_digito)
print('segundo_digito: ', segundo_digito)