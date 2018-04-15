import pandas as pd


def read_csv(file_name):
  columns=['Word']
  df_in = pd.read_csv(file_name, names=columns, header=None, skiprows=1)
  words = df_in['Word'].tolist()
  return words
