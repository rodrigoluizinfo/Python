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

#print("")
# print('\n')
# print("#Head = Cabeçalho - Show the first five lines")
# print(df.head())
# print('\n')
# print("#Tail = rodapé - Show the first five lines")
# print(df.tail())
# print('\n')
# print("#Show the five lines(Random)")
# print(df.sample())#Show the five lines(Random)
# print('\n')
# print("#Show the types of values")
# print(df.dtypes)
# print('\n')
#
# print("#Changing type LojaID to object")
# df["LojaID"] = df["LojaID"].astype("object")
# print(df.dtypes)
# print('\n')

# print("#Before fillna")
# print("#Adding the number of cells per column with null values \n"
#       "#Somando a quantidade de celulas por colunas com valores nulos ")
# isnull = df.isnull().sum()
# print(isnull)
# print('\n')
#
# print("#Changing null values per mean values \n"
#       "#Substituindo valores nulos pela média")
# fillna = df["Vendas"].fillna(df["Vendas"].mean, inplace=True)#inplace = True -> Changing in memory
# print('\n')
#
# print("Changin null values per zero values \n"
#       "Substituindo valores nulos por zero")
fillna = df["Vendas"].fillna(0, inplace=True)
# print('\n')
#
# print("#After fillna")
# print("#Adding the number of cells per column with null values \n"
#       "#Somando a quantidade de celulas por colunas com valores nulos ")
# isnull = df.isnull().sum()
# print(isnull)
#
# print("#Drop null values"
#       "Apagando todos os valores vazios")
dropna = df.dropna(inplace=True)
#
# print("#Drop null values per column Vendas"
#       "Apagando todos os valores nulos na coluna Vendas")
dropna_subset = df.dropna(subset=["Vendas"], inplace=True)
#
# print("#Delete rows with null values in all columns"
#       "Deletar linhas com valores nulos em todas as colunas")
dropna_how = df.dropna(how="all", inplace=True)
print("\n")

print("Created a new column call Receita")
df["Receita"] = df["Vendas"].mul(df["Qtde"])#Multiply column Vendas with Qtde = Column Receita
print(df.head())
print("\n")

print("Max value \n"
      "Maior valor")
max_receita = df["Receita"].max
print(max_receita)
print("\n")

print("Minimum value \n"
      "Menor valor")
min_receita = df["Receita"].min
print(min_receita)
print("\n")

print("Top 3 \n"
      "3 melhores")
nlargest = df.nlargest(3, "Receita")#Top 3 = 3 melhores
print(nlargest)
print("\n")

print("Worst 3 \n"
      "3 piores")
nsmallest = df.nsmallest(3, "Receita")#Worst 3 = 3 piores
print(nsmallest)
print("\n")

print("Grouping by city \n"
      "Agrupamento por cidade")
print(df.groupby("Cidade")["Receita"].sum())
print("\n")

print("Sorting dataset \n"
      "Ordenando conjunto de dados")
print(df.sort_values("Receita", ascending=False).head(10))













