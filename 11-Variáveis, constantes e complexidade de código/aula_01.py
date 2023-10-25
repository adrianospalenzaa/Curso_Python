velocidade = 60 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

RANGE1 = 99 # Mudar minimo
RANGE2 = 101 # Mudar maximo

if velocidade > RADAR_1 and (local_carro >= RANGE1 and local_carro <= RANGE2):
    print('Veiculo acima da velocidade permitida para o local!')
else:
    print('Veiculo dentro da velocidade permitida para o local.')

    """Letras maiusculas são usadas para constantes, ou seja, 
    valores que não mudam durante a execução do programa."""
    #RANGE1 = 99
    #RANGE2 = 101 