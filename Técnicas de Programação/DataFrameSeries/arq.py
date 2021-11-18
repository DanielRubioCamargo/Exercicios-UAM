import pandas as pd
from IPython.display import display

sells = {"produto":["Arroz","Feijão"],"Preço":[5.5,7.75],"Quantidade":[50,70]}
sells_df = pd.DataFrame(sells)

data = pd.read_excel("C:\\Users\\drubi\\Documents\\Repositórios GitHub\\Exercicios-UAM\\Técnicas de Programação\\DataFrameSeries\\Dados.xlsx")

data["Pontuação"] = data["RA"] + data["Idade"]

idades = data["Idade"].value_counts()

mediaIdades = data.groupby("Idade").sum()

display(mediaIdades)