"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
    - Você vai propor uma palavra secreta
    qualquer e vai dar a possibilidade para
    o usuário digitar apenas uma letra.

    - Quando o usuário digitar uma letra, você
    vai conferir se a letra digitada está
    na palavra secreta.

    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;

    - Se a letra digitada não estiver
    na palavra secreta; exiba *.

Faça a contagem de tentativas do seu
usuário.
"""
palavra_secreta = 'perfume'
letra_certa = ''
numeros_tentarivas = 0

while True:

    letra_digitada = input('Digite uma letra!\n')
    numeros_tentarivas += 1
    if len(letra_digitada) > 1:
        print('Digite somente uma letra!')
        continue

    if letra_digitada in palavra_secreta:
        letra_certa += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_certa:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Palavra Formada', palavra_formada)

    if palavra_formada == palavra_secreta:
        print('Parabéns você acertou!')
        print('A palavra secreta era', palavra_secreta)
        print('Você tentou', numeros_tentarivas, 'vezes')
        letra_certa = ''
        numeros_tentarivas = 0


