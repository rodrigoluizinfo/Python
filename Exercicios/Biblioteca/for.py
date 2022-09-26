# for x in range  (100):
#     print (x)
#
# for x in range (1, 101):
#     print (x)

# a = int(input("Digite um número: "))
#
# for x in range (1, a):
#     resto = a % x
#     print (resto)

# a = int(input("Digite um número: "))
#
# for x in range (1, a+1):
#     resto = a % x
#     print (resto)

# a = int(input("Digite um número: "))
#
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#        #div = div + 1 #Teste lógico para validar se o número é primo e apresentar o resultador for do laço for
#        div += 1 #Teste lógico para validar se o número é primo e apresentar o resultador for do laço for
#
# if div == 2:
#     print("O número {} " .format(a) + "é primo")
# else:
#     print("O número {} " .format(a) + "não é primo")

""" for num in range(101):
    div = 0
    for x in range(1, num+1):
        resto = num % x
        #print(x, resto)
        if resto == 0:
           #div = div + 1 #Teste lógico para validar se o número é primo e apresentar o resultador for do laço for
           div += 1 #Teste lógico para validar se o número é primo e apresentar o resultador for do laço for

    if div == 2:
        print(num) """

# a = int(input("Digite um número: "))
#
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#            #div = div + 1 #Teste lógico para validar se o número é primo e apresentar o resultado for do laço for
#            div += 1 #Teste lógico para validar se o número é primo e apresentar o resultador for do laço for
#
#     if div == 2:
#         print(num)

text = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in text:
        if letra.upper() in VOGAIS:
            print(letra, end="")

print()

#VOGAIS = Quando a variável está em maísculo, é uma constante
#.upper = Deixa o texto ou conteúdo string da variável em MAIÚSCULO
#letra.upper() foi necessário para fazer a leitura das letras em maíusculo, devido ao valor da constante
#end="" = Apresenta os valores na mesma linha










