#Passo 1 - Importar a biblioteca pandas (Apelidar de pd)
import pandas as pd #Alias(Pseudonimo) = pd
from openpyxl import Workbook #It's necessáry to run code

#Passo 2 - Declarar a variável file_name para receber o diretório(Copy path) do arquivo excel
#          Declarar variável df(Data Frame) para receber os dados variável file_name
file_name = "C:/Users/rodri/OneDrive/Python/Exercicios/Análise de dados/Cusro_Python_Pandas_Digital_Innovation-master/datasets/Gapminder.csv"
df = pd.read_csv(file_name, sep=';')#Sep - It will separeted the columns of the excel file with ;

#Passo 3 - Reading excel file
print(df.head())

