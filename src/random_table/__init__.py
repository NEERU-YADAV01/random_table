import pandas as pd
from pathlib import Path

DEFAULT_TABLE = "../data/example-table.csv"

def load_table(filepath=DEFAULT_TABLE):
    example_table = pd.read_csv(filepath)
    example_table.columns = example_table.columns.str.strip()
    return example_table

def categories(filepath=DEFAULT_TABLE):
    example_table = load_table(filepath)
    return example_table.columns.to_list()
    