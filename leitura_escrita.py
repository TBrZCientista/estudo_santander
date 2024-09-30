
#abrindo arquivos externos e lendo o conteúdo

arquivo = open("listas.py", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

#para abrir um arquivo e escrever, colocamos o "w" no lugar do "r"
#caso queiramos escrever algo no arquivo, usamos nome_da_funcao.write

#para manejar a abertura e fechamento automáticos usamos "with"

with open("tuplas.py", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)