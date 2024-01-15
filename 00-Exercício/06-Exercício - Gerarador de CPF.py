import random
#nove_digitos = '116339657'

# 1. Gerar os primeiros nove dígitos aleatórios
nove_digitos = ''.join([str(random.randint(0, 9)) for _ in range(9)])

# Converte a string para uma lista de inteiros
lista_numerica = [int(digito) for digito in nove_digitos]


# Calcula o primeiro dígito verificador
soma = 0
cont_regressivo = 10
for i in range(9):
    soma += cont_regressivo * lista_numerica[i]
    cont_regressivo -= 1

resto = (soma * 10) % 11
primeiro_digito = 0 if resto > 9 else resto


# Calcula o segundo dígito verificador
soma = 0
cont_regressivo = 11
lista_numerica.append(primeiro_digito)

for i in range(10):
    soma += cont_regressivo * lista_numerica[i]
    cont_regressivo -= 1

resto = (soma * 10) % 11
segundo_digito = 0 if resto > 9 else resto


# Adiciona os dígitos verificadores à lista_numerica
lista_numerica.extend([segundo_digito])

# Converte a lista_numerica para string
cpf_gerado = ''.join(map(str, lista_numerica))

print('CPF Gerado:', cpf_gerado)
