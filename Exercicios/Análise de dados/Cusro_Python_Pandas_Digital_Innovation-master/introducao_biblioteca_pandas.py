#Step ONE - Import library of pandas with alias (pd)
import pandas as pd #Alias(Pseudonimo) = pd
from openpyxl import Workbook #It's necessáry to run code

#Step TWO - Declarar a variável file_name para receber o diretório(Copy path) do arquivo excel
#          Declarar variável df(Data Frame) para receber os dados variável file_name
file_name1 = "C:/Users/rodri/OneDrive/Python/Exercicios/Análise de dados/Cusro_Python_Pandas_Digital_Innovation-master/datasets/Gapminder.csv"
df = pd.read_csv(file_name, sep=';')#Sep - It will separeted the columns of the excel file with ;

#Rename columns excel file(Optional)
df = df.rename(columns={"country":"País", "continent":"Continente", "year":"Ano", "lifeExp":"Expectativa de vida", "pop":"População total", "gdpPercap":"PIB"})

# #Reading excel file
# print(df.head())
# print(df.head(10))#Show the ten firts lines excel file
# print(df.shape)#Show total lines and columns
# print(df.columns)
# print(df.dtypes)
# print(df.tail())#Show the last lines excel file
# print(df.describe())#Show all functions to analyse a excel file with pandas
# print(df["Continente"].unique())#Show only one result of object
# print(df.loc[df["Continente"] == "Oceania"])#Find "Continente" in the excel file array
# object_oceania = df.loc[df["Continente"] == "Oceania"]#Storing the code in the variable
# print(object_oceania.head())#Showing the result of variable
# print(object_oceania["Continente"].unique())#Show only one result of object "Continente"
# print(df.groupby("Continente")["País"].nunique())#Shows count country each continent
# print(df.groupby("Ano")["Expectativa de vida"].mean())#Shows lifes expectancy each year
# print(df["PIB"].sum())#Sum of values of colum PIB
# print(df["PIB"].mean())#Mean of values of colum PIB









