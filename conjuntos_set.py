conjunto_1 = {1, 2, 3}
conjunto_2 = {3, 4, 5, 6}
conjunto_3 = {5, 6, 7, 8, 9}

uniao = conjunto_1 | conjunto_2 #a barra em pé, une os dois conjuntos
print(uniao) 

intersecao = conjunto_1 & conjunto_2 # sinal de "&" mostra o que tem ao mesmo tempo nos dois conjuntos
print(intersecao)

diferenca = conjunto_1 - conjunto_2 #sinal de "-" mostra o que o conjunto 1 tem de diferente do conjunto 2
print(diferenca)

diferenca_simetrica = conjunto_1 ^ conjunto_2 # sinal de "^" mostra unido, o que tem exclusivo em cada conjunto
print(diferenca_simetrica)

conjunto_1.add(7) # .add acrescenta algo no conjunto
print(conjunto_1)

conjunto_1.remove(7) #.remove retira do conjunto o item informado
print(conjunto_1)

conjunto_2.discard(3) #.discard retira do conjunto o item informado caso exista no conjunto
print(conjunto_2)

print(conjunto_3)
conjunto_3.clear() #apaga todos os itens do conjunto
print(conjunto_3)
