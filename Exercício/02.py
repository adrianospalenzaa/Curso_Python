"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero = input("Digite um número inteiro:\n ")
#
# try:  # tenta executar o código
#     numero = int(numero)
# except:  # caso ocorra algum erro, executa o código abaixo
#     print(f'{numero} não e inteiro')
#     exit(0)  # encerra o programa
#
# else:
#     if numero % 2 == 0:
#         print(f'o numero {numero} e par.')
#     else:
#         print(f'o numero {numero} e impar.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# hora = int(input('Digite a hora.\n '))
#
# if hora in range(0, 12):
#     print('Bom dia!')
# elif hora in range(12, 18):
#     print('Boa Tarde!')
# elif hora in range(18, 24):
#     print('Boa Noite!')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome.\n ')


if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) == 5 or len(nome) == 6:
    print('Seu nome é normal')
elif len(nome) >= 7:
    print('Seu nome é muito grande')

