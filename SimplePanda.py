import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv("C:\\Users\\mysti\\Coding\\GoToCode\\AWEFH.csv")

print(data.head())

print("")

print(data.tail())

print("")

print(data)

print("")

data.plot(kind='bar')




