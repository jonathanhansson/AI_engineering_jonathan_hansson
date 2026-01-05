from constants import DATA_PATH
import pandas as pd
import json

df = pd.read_csv(DATA_PATH / "Iris.csv", index_col=0)

class Iris:
    def __init__(self, limit = 100):
        self.df_full = df
        self.df = df.head(limit)
    
    def filter_flower(self, species):
        self.df = self.df_full.query("Species == @species")
        return self

    def to_json(self):
        data = self.df.to_json(orient="records")
        return json.loads(data)
    
