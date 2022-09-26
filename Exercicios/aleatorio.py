import random

escolha = random.choice(['Julia', 'Ana', 'Maria', "Renata"])
exemplo = random.sample(range(100), 10)  # Entre 100 números, serão escolhidos 10 de forma aleatória
aleatorio = random.random() # Returns a random float number between 0 and 1 = Retorna um número decimal aleatório entre 0 e 1
variacao  = random.randrange(6) # Retorna um número aleatório de acordo com a range especificada, que no caso foi 6, então será de 0 a 6

print(escolha)
print(exemplo)
print(aleatorio)
print(variacao)


