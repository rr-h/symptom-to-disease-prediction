import pandas as pd

try:
    df = pd.read_spss('model.sav')
    df.to_csv('output.csv')
except Exception as e:
    print(f"An error occurred: {e}")
