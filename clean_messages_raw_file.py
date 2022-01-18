import pandas as pd

def clean_messages(df):
  
  result_df = df
  # удаляем строки, в которых нет данных в поле СистСтатус ЗаказТОРО
  result_df.dropna(subset=['СистСтатус ЗаказТОРО', ], inplace=True)
  # удаляем колонку Код ABC
  result_df.drop(['Код ABC', 'Номер адреса', 'ОснСредство'], inplace=True, axis=1)
  return result_df