# -*- coding: utf-8 -*-
import pandas as pd

_CHARACTOR_ENCODING = "utf-8"
# ------ no changes beyond this point --------

def save_to_excel(df, file_name):
  engine = 'openpyxl'
  writer = pd.ExcelWriter(file_name, engine)
  df.to_excel(writer, 'Sheet1')

def save_to_csv(df, file_name):
  df.to_csv(path_or_buf=file_name, encoding=_CHARACTOR_ENCODING)

def save_to_json(df, file_name):
  with open(file_name, 'w', encoding=_CHARACTOR_ENCODING) as file:
    df.to_json(path_or_buf=file, orient='records', force_ascii=False)
