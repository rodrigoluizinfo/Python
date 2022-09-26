from datetime import date

hoje = date.today()
nascimento = date(1991, 1, 31)

idade = hoje - nascimento
dias_vida = idade.days

# Todas as 3 formas abaixo funcionam na versão 3.7.9

# print("Eu tenho " + str(idade) + "dias de vida")
# print("Eu tenho " + str(dias_vida) + " dias de vida")
print ("Eu tenho", + dias_vida, "dias de vida")