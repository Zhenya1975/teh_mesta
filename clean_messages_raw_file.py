import pandas as pd

def clean_messages(df):
  # удаляем строки, в которых нет данных в поле СистСтатус ЗаказТОРО
  result_df = df
  result_df.dropna(subset=['СистСтатус ЗаказТОРО', ], inplace=True)
  return result_df