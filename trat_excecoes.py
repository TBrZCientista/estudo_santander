try: #contém o código que pode gerar um exceção
    resultado = 10 / 0
    print (resultado)
except ZeroDivisionError: #especifica a exceção que será capturada e lidada.
    print("Erro: Divisão por zero.")
except ValueError:
    print("Erro: Valor inválido.")

try:
    arquivo = open("arquivo.txt", "r")
except:
    print("Erro: Arquivo não localizado")
#finally:
    #arquivo.close()

#exceções personalizadas

def funcao(a ,b):
    if a == b:
        raise Exception("Descrição do Erro.")
    
try:
    funcao()
except Exception as e:
    print(f"Erro: {str(e)}")

