frutas = ["maça", "banana", "laranja"]
contador = 0

for fruta in frutas:
    print (fruta)

while contador < 5 :
    print(contador)
    contador+=1

print("\n Veremos a tabuada de dois.")
contador = 1
while contador <= 10:
    print("2 x",contador,"=",contador *2)
    contador+= 1

print("\n Veremos a tabuada de dois.")
for contador in range(1,11):
    print("2 x",contador,"=",contador *2)

contador = 0 

while True:
    print("\n", contador)
    contador += 1

    if contador == 5:
        break

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

#O comando pass é mais utilizado para guardar bloco de código para implementação
#posterior. for i in range(5):
#pass

