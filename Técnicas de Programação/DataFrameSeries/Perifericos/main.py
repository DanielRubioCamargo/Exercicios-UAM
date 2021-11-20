import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

perifericos_df = pd.read_excel("C:\\Users\\drubi\\Documents\\Repositórios GitHub\\Exercicios-UAM\\Técnicas de Programação\\DataFrameSeries\\Perifericos\\dataframetesteperifericos.xlsx")

def show_dataframe_general_comparision_graph(dataframe,xAxis:str,yAxis:str,graphTitle="Título",lineDesc="Legenda",chosenColor="r"):
    plt.figure(figsize=(8,5))
    plt.bar(dataframe[xAxis],dataframe[yAxis],label = lineDesc,color = chosenColor)
    plt.title(graphTitle)
    plt.xlabel(xAxis)
    plt.ylabel(yAxis)
    plt.legend(loc = 1)
    plt.show()

def main():
    print("-"*75)
    display(perifericos_df)
    print("-"*75)
    xDecision = str(input("Insira o dado do eixo X : ")).title()
    yDecision = str(input("Insira o dado do eixo Y : ")).title()
    graphTitle = str(input("Insira o título do gráfico : "))
    labelTitle = str(input("Insira a legenda : "))
    try:
        show_dataframe_general_comparision_graph(perifericos_df,xDecision,yDecision,graphTitle,labelTitle)
    except:
        print("\033[1;31mErro! Passagem de parâmetros incorreta!\033[m")

if __name__ == "__main__":
    main()