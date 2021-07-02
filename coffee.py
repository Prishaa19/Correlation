import plotly.express as px
import csv
import numpy as np

def fig(file):
    with open(file) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Coffee in ml", y="sleep in hours")
        fig.show()

def marks(file):
    Coffee_in_ml = []
    sleep_hours = []
    with open(file) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Coffee_in_ml.append(float(row["Coffee in ml"]))
            sleep_hours.append(float(row["sleep in hours"]))

    return {"x" : Coffee_in_ml , "y": sleep_hours}

def Correlation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Coffee drunk and sleep   \n=",correlation[0,1])

def setup():
    file  = "coffee.csv"

    datasource = marks(file)
    Correlation(datasource)
    fig(file)

setup()