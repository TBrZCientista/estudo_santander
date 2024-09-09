pessoa = {"nome": "Felipe Freitas", "idade": 37, "cidade": "Itaboraí", "estado_civil": "casado"}

print(pessoa["estado_civil"])
print(pessoa["nome"])
print(pessoa.get("nome"))

print(pessoa.keys()) #retorna quais são as chaves do dicionário
print(pessoa.values()) #retorna os valores das chaves do dicionário
print(pessoa.items()) #retorna os pares chave-valor do dicionário

pessoa.update({"profissão":"Backoffice"}) #atualiza o dicionário, acrescentando o que for colocado entre colchetes
print(pessoa)