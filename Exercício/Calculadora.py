# .lower() -> Transforma tudo em minúsculo
# .startswith('s') -> Verifica se a string começa com 's'

while True:

    primeiro_numero = input('Digite o primeiro número.\n ')
    segundo_nuemro = input('Digite o Segundo número.\n ')
    operacao = input('Escolha a operação. "+" "-" "*" "/"\n')

    numeros_validos = None
    primeiro_numero_float = 0
    segundo_numero_float = 0

    try:
        primeiro_numero_float = float(primeiro_numero)
        segundo_numero_float = float(segundo_nuemro)
        numeros_validos = True
    except:
        numeros_validos = None
    if numeros_validos is None:
        print('Um ou ambos dos numeros são invalidos!')
        continue

    operacao_valida = '+*-/'

    if operacao not in operacao_valida:
        print('Operador invalido!')
        continue

    if len(operacao) > 1:
        print('Informe somente um operador!')
        continue

    if operacao == "+":
        print(f' A soma dos valores é --> {primeiro_numero_float + segundo_numero_float}')
    elif operacao == "-":
        print(f' A subitração dos valores é --> {primeiro_numero_float - segundo_numero_float}')
    elif operacao == "*":
        print(f' A multiplicação dos valores é --> {primeiro_numero_float * segundo_numero_float}')
    elif operacao == "/":
        print(f' A divisão dos valores é --> {primeiro_numero_float / segundo_numero_float}')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')  # Se a resposta começar com 's' ele sai do programa
    if sair is True:
        break
