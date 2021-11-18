import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

data = pd.read_excel("C:\\Users\\drubi\\Documents\\Repositórios GitHub\\Exercicios-UAM\\Técnicas de Programação\\DataFrameSeries\\Dados.xlsx")

agesList = list()
for c in range(1,36):
    agesList.append(c)

ages = data[["Nome","Idade"]]

mean = ages["Idade"].mean()

plt.figure(figsize=(10,6))
plt.bar(ages["Nome"],ages["Idade"],label = "Idades",ls = "solid",color = "r")
plt.title("Idades da turma (Media de idades : {})".format(int(mean)))
plt.yticks(agesList)
plt.show()

display(ages)