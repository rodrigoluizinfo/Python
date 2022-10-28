# # def exibir_mensagem():
# #     print("Olá mundo!")
# #
# # def exibir_mensagem2(nome):
# #     print(f"Seja bem vindo: {nome}!")
# #     #print("Seja bem vindo: {nome} " .format(nome))
# #
# # #The difference between exibir_mensagem2 and exibir_mensagem3 is that in exibir_mensagem2
# # # I need to pass a parameter or the code runs with error
# # def exibir_mensagem3(nome="Anônimo"):
# #     print(f"Seja bem vindo: {nome}!")
# #
# # exibir_mensagem()
# # exibir_mensagem2(nome="Rodrigo")
# # exibir_mensagem3(nome="Rodrigo Luiz")
#
# def calcular_total(numeros):
#     soma = sum(numeros)
#     print(f"A soma total e: {soma}")
#     return soma
#
# def salvar_carro(marca, modelo, ano, placa):
#     print(f"Carro inserido com sucesso!!! -> {marca}/{modelo}/{ano}/{placa}")
#
# calcular_total([10, 20, 30])
#
# #If the variable is allocated elsewhere, the results will not be correct
# #salvar_carro("Palio", "Fiat", "2015", "ABC-1234")
#
# #In this way, the variable has the correct value
# #salvar_carro(marca="Fiat", modelo="Palio", ano="2015", placa="ABC-1234")
#
# #In this case, a dictionary is passing as an argument in the function
# # (**) Represents as kwargs
# salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": "2015", "placa": "ABC-1234"})

#------------------------------------------------------------------------------

def exibir_poema(data_extensao, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave,valor in kwargs.items()])
    mensagem = f"{data_extensao}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "Zen of Python",
    "Beautiful is than ugly.",
    autor="Tim Peters",
    ano=1999
)




