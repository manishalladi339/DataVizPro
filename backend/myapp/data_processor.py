import pandas as pd
import json

def process_csv(file_path):
    df = pd.read_csv(file_path)
    return df.to_dict(orient='records')

def process_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    df = pd.json_normalize(data)
    return df.to_dict(orient='records')
