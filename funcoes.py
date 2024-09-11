def saudacao():
    print("Olá meu querido amigo, você é um amigo.")

saudacao()

def saudacao_2(nome):
    print(f"Olá, {nome}!")

saudacao_2("Felipe")#aqui foi dado o argumento do parâmetro

#valores de retorno

def soma(a, b):
    return a + b

resultado = soma(3, 4)

print(resultado)

#Funções anônimas(lambda)

quadrado = lambda x: x ** 2

print(quadrado(5))

#variáveis locais e globais

def funcao():
    variavel_local = 10
    print(variavel_local) #sendo acionada dentro da função

funcao()

variavel_global = 20

def funcao_2():
    print(variavel_global)

funcao_2()

print(variavel_global)
#print(variavel_local) #quando declarado desse jeito retorna um erro, pois é uma variável local.

#docstring

def area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.

    Args:
        base (float): A base do retângulo.
        altura (_type_): A altura do retângulo.

    Returns:
    float: A área do retangulo
    """

    return base * altura

print(area_retangulo(5, 9))

#funções com número variável de argumentos

def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(soma_variavel(2, 4, 5))
print(f"O resultado é:", soma_variavel(45,66,76))

