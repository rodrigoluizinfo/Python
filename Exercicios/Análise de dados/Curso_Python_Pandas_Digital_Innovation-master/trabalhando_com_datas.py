#Step ONE - Import library of pandas with alias (pd)
import pandas as pd

#Step TWO - Declarar a variável file_name para receber o diretório(Copy path) do arquivo excel
# Declarar variável df(Data Frame) para receber os dados variável file_name
file_name1 = "datasets/Aracaju.xlsx"
file_name2 = "datasets/Fortaleza.xlsx"
file_name3 = "datasets/Fortaleza.xlsx"
file_name4 = "datasets/Recife.xlsx"
file_name5 = "datasets/Salvador.xlsx"

df1 = pd.read_excel(file_name1, engine="openpyxl")
df2 = pd.read_excel(file_name2, engine="openpyxl")
df3 = pd.read_excel(file_name3, engine="openpyxl")
df4 = pd.read_excel(file_name4, engine="openpyxl")
df5 = pd.read_excel(file_name5, engine="openpyxl")

df = pd.concat([df1, df2, df3, df4, df5])#Concatenate all data frames to one data frame(df)

print("\n")
print("#Changing column Data to type [int64]\n"
      "#Alterando coluna Data para tipo [int64]")
df["Data"] = df["Data"].view("int64")
print(df.dtypes)
print("\n")

print("#Changing column Data to type [datatime]\n"
      "#Alterando coluna Data para tipo [datetime]")
df["Data"] = pd.to_datetime(df["Data"])
print(df.dtypes)
print("\n")

print("#Creat a new column [Receita] \n"
      "#Criando uma nova columa [Receita]")
df["Receita"] = df["Vendas"].mul(df["Qtde"])
print("\n")

print("#Total revenue per year \n"
      "#Total de receita por ano")
print(df.groupby(df["Data"].dt.year)["Receita"].sum())
print("\n")

#groupby(Python) = Join(SQL)

print("#Create a new column [Ano_Venda] \n"
      "#Criando uma nova coluna [Ano_Venda]")
df["Ano_Venda"] = df["Data"].dt.year
print("\n")

#print(df.sample(5))

print("#Create a new column [Mes_Venda] \n"
      "#Criando uma nova coluna [Mes_Venda]")
df["Mes_Venda"] = df["Data"].dt.month
print(df.sample(5))
print("\n")

print("#Create a new column [Dia_Venda] \n"
      "#Criando uma nova coluna [Dia_Venda]")
df["Dia_Venda"] = df["Data"].dt.day
print(df.sample(5))
print("\n")

#print(df.sample(5))

print("#Date minimum \n"
      "Data mínima")
print(df["Data"].min())
print(df.sample(5))
print("\n")

print("#Showing the diference of days between column [Data] and [Data].min() - Date minimum \n"
      "#Mostrando a diferença de dias entre a coluna [Data] e a data mínima")
df["Diferenca_Dias"] = df["Data"] - df["Data"].min()
print(df.sample(5))
print("\n")

print("#Showing quarter according to date [Data] \n" 
      "#Mostrando o trimestre de acordo com a data")
df["Trimestre_Venda"] = df["Data"].dt.quarter
print(df.sample(5))
print("\n")

df = df.reset_index()
print("#Showing sales in march 2019 \n"
      "#Mostrando as vendas em março de 2019")
df["Vendas_Marco_2019"] = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]
df = df.set_index("Vendas_Marco_2019")
print(df.sample(5))
print("\n")













