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
print('\n')
print("Head = Cabeçalho - Show the first five lines")
print(df.head())
print('\n')
print("Tail = rodapé - Show the first five lines")
print(df.tail())
print('\n')
print("Show the five lines(Random)")
print(df.sample())#Show the five lines(Random)
print('\n')
print("Show the types of values")
print(df.dtypes)
print('\n')

print("Changing type LojaID to object")
df["LojaID"] = df["LojaID"].astype("object")
print(df.dtypes)

#Class paused at 08:20





