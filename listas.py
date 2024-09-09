frutas = ["maçã","banana", "laranja"]

frutas.append("siriguela")

print(frutas[0])
print(frutas[1])
print(frutas[2])

print(frutas[-1])
print(frutas[-2])
print(frutas[-3])

print(frutas)

frutas.insert(3,"mexerica") #insere no índice 3
print(frutas)

frutas.remove("banana") #remove a primeira ocorrência de um item na lista
print(frutas)

fruta_removida = frutas.pop(3) #remove o item do índice específico
print(frutas)
print(fruta_removida)

frutas.sort() #coloca os itens em ordem crescente
print(frutas)

frutas.reverse() #inverte a ordem dos itens
print(frutas)

#listas de compreensão

numeros = [1, 2, 3, 4, 5, 6]
quadrados = [x ** 2 for x in numeros if x % 2 ==0] #aplica o quadrado no número se for par

print(quadrados)

