primeiro_valor = int(input('Digite um Valor\n'))
segundo_valor = int(input('Digite outro Valor\n'))

if primeiro_valor > segundo_valor:
    maior = primeiro_valor
    menor = segundo_valor
else:
    menor = primeiro_valor
    maior = segundo_valor

print(f'O valor {maior} e maior queo o valor {menor}!')
