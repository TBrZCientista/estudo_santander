#tuplas são imutáveis, ótimas para guardar dados que não poder ser mexidos

ponto = (2, 6, 8)

print(ponto[1])
print(ponto[2])

minha_tupla = (1, 3, 5, 8, 8, 9, 33)

print(minha_tupla.index(8)) #retorna 3, pois o 8 aparece primeiro no índice 3
print(minha_tupla.count(8)) #retorna a quantidade de vezes que o número aparece na tupla
print(len(minha_tupla)) #retorna a quantidade de itens na tupla