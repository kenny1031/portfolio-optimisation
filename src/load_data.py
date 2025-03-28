import pandas as pd

def load_stock_data(filepath):
    data = pd.read_csv(filepath)
    return data