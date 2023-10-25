frase = 'ad r ano dos sa n t os'
i = 0
letra_maisvezes = ''
maior_quant_letras = 0

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    i += 1
    quant_letra = frase.count(letra_atual)

    if maior_quant_letras <= quant_letra:
        maior_quant_letras = quant_letra
        letra_maisvezes = letra_atual


print(f'{letra_maisvezes} {maior_quant_letras}')