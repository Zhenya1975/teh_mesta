import pandas as pd

teh_mesta_df = pd.read_csv('data/teh_masta_full_list.csv', dtype=str)
eo_list = pd.read_csv('data/eo_list.csv', dtype=str)
result_df = pd.read_csv('data/result_df.csv', dtype=str)

teh_mesto_main_eo = {}
for index, row in result_df.iterrows():
  teh_mesto = row['teh_mesto']
  teh_mesto_eo_list = eo_list.loc[eo_list['teh_mesto'] == teh_mesto]
  print('teh_mesto: ', teh_mesto, 'teh_mesto_eo_list:', teh_mesto_eo_list)

  main_eo_name = teh_mesto_eo_list['Описание'].iloc[0]
  print('teh_mesto: ', teh_mesto, 'main_eo_name:', main_eo_name)