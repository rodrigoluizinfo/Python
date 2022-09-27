# # print('\nCurso DIO - Introdução à programação com Python')
# #
# # # Variáveis pr
# # # a = 5
# # # b = 6
# #
# # Dados sendo solicitados
# a = int(input('Digite o primeiro valor: '))
# b = int(input('Digite o segundo valor: '))
#
# soma = a + b
# sub = a - b
# multi = a * b
# div = a / b
# resto = a % b
# #
# # print('============Sem concatenação==================\n')
# # print(soma)
# # print(sub)
# # print(multi)
# # print(div)
# # print(str(resto) + '\n')
# #
# # print('============Com concatenação(Incorreto)==================\n')
# # print('A soma é: ' + str(soma))
# # print('A subtração é: ' + str(sub))
# # print('A multiplicação é: ' + str(multi))
# # print('A divisão é: ' + str(div))
# # print('O resto é: ' + str(resto) + '\n')
#
# # print('============Com concatenação(Correto)==================\n')
# #
# # #Forma 1: A concatenção é feita ao apresentar o resultado
# # # print('A soma é: {soma}\n'
# # #       'A subtração: {sub}\n'
# # #       'A multiplicação é: {multi}\n'5
# # #       'A divisão é: {div}\n'
# # #       'O resto é: {resto}\n'
# # #       .format(soma=soma, sub=sub, multi=multi, div=div, resto=resto))
# #
# # #Forma 2: A concatenação é armazenada em uma variável
# # resultado = ('A soma é: {soma}\n'
# #       'A subtração: {sub}\n'
# #       'A multiplicação é: {multi}\n'
# #       'A divisão é: {div}\n'
# #       'O resto é: {resto}\n'.format(soma=soma, sub=sub, multi=multi, div=div, resto=resto))
# #
# # print(resultado)
# #
# #
# #
#
# """ curso = "pYtHon"
#
# print(curso.upper()) #All uppercase
#
# print(curso.lower()) #All lowercase
#
# print(curso.title()) #First letter uppercase """
#
# #Shorten blank values
#
# """ curso = "   Python "
#
# print(curso.strip())#Removes blank values spaces of left and right
#
# print(curso.lstrip())#Removes blank values spaces of left
#
# print(curso.rstrip())#Removes blank values spaces of right """
#
# """ curso = "Python"
#
# print(curso.center(10, "#"))#Adiciona # dentro do string na esquerda e direita até completar 10 caracteres, se não for informado o caracter, seja adicionado espaço em branco
# print(".".join(curso))#Contena com . os caracteres da string """
#
# # print('============Com concatenação(Correto)==================\n')
# #
# # #Forma 1: A concatenção é feita ao apresentar o resultado
# # # print('A soma é: {soma}\n'
# # #       'A subtração: {sub}\n'
# # #       'A multiplicação é: {multi}\n'5
# # #       'A divisão é: {div}\n'
# # #       'O resto é: {resto}\n'
# # #       .format(soma=soma, sub=sub, multi=multi, div=div, resto=resto))
#
# #O exemplo acima é o método .format, mas existe um método mais fácil de realizar o mesmo exemplo
#
# """ print('============Método(.format)==================\n')
# #
# #Forma 1: A concatenção é feita ao apresentar o resultado
# print('A soma é: {soma}\n'
#       'A subtração: {sub}\n'
#       'A multiplicação é: {multi}\n'
#       'A divisão é: {div}\n'
#       'O resto é: {resto}\n'
#       .format(soma=soma, sub=sub, multi=multi, div=div, resto=resto))
#
# print('============Método(f)==================\n')
# #
# print(f'A soma é: {soma}\n'
#       f'A subtração: {sub}\n'
#       f'A multiplicação é: {multi}\n'
#       f'A divisão é: {div}\n'
#       f'O resto é: {resto}\n')
# #Se tiver quebra de linha, é necessário chamar o método f em todas elas """
#
# print('============Método(f)==================\n')
# #
# print(f""" A soma é: {soma}\n'
#       'A subtração: {sub}\n'
#       'A multiplicação é: {multi}\n'
#       'A divisão é: {div}\n'
#       'O resto é: {resto}\n' """)
# #Ou adotar o método de string triplas, onde não é necessário colocar o método f em todas as linhas
#
# """ PI = 3.14159
#
# print(f'Valor de PI: {PI:.2f}')#Vai apresentar no máximo duas casas no final da sequência numérica
# print(f'Valor de PI: {PI: 10.2f}')#Vai apresentar no máximo 10 casas(Caso não valor, será adicionado espaços em branco) no início da sequência numérica e 2 casas no final dela """

texto = "Python para análise de dados"

#Fatiamaento
# print(texto[0:10] + '\n')
# print(texto[:10] + '\n')# :10 = 0:10
# print(texto[1:10] + '\n')

#Count
#*OBS: É case sensitive
print(texto.count("dados"))#Armazenado na apresentação

texto_count = texto.count("dados")#Armazenado na variável
print(texto_count)

#Replace
print(texto.replace("análise", "analise"))#Armazenado na apresentação

texto_alterado = texto.replace("análise", "analise")#Armazenado na variável
print(texto_alterado)


