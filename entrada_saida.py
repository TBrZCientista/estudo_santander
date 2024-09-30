#entrada de dados
nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))

print("Olá,", nome , "!")
print("Você tem", idade, "anos.")

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade")

#saída de dados

nome = "Felipe"
idade = 37

print(f"Olá, meu nome é {nome} e tenho {idade} anos.")