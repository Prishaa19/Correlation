import plotly.express as px
import csv
import numpy as np

def fig(file):
    with open(file) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Days Present", y="Marks In Percentage")
        fig.show()

def marks(file):
    markPercentage = []
    daysPresent = []
    with open(file) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            markPercentage.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))

    return {"x" : markPercentage, "y": daysPresent}

def Correlation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in percentage and Days present  \n=",correlation[0,1])

def setup():
    file  = "marks.csv"

    datasource = marks(file)
    Correlation(datasource)
    fig(file)

setup()