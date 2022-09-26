import statistics

data = [8, 9, 1.25, 0.25, 7, 1.25, 10]
media = statistics.mean(data)
mediana = statistics.median(data)
variacao = statistics.variance(data)

print(media)
print(mediana)
print(statistics.variance(data))# Calculates the variance from a sample of data = Calcula a variação dos dados amostrados

