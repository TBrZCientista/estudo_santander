import math #aqui foi declarado o import, e o módulo a ser importado
import random
import datetime

resultado = math.sqrt(25) #sqrt calcula o quadrado de um número
print(int(resultado))

numero_aleatorio = random.randint(1, 15)
print(numero_aleatorio)

data_atual = datetime.datetime.now()
data_formatada = data_atual.strftime("%d/%m/%Y %H:%M:%S")
print(data_formatada)