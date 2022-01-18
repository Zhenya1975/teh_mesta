import pandas as pd

origin_df = pd.read_csv('data/teh_masta_full_list.csv', dtype=str)
origin_codes_df = origin_df.loc[:,['Техническое место', 'Название технического места', 'Вышестоящее ТехМесто']]
origin_codes_df['code'] = "first" + origin_codes_df['Техническое место']
new = origin_codes_df['code'].str.split("-", expand = True)
origin_codes_df['level_1'] = new[0]
origin_codes_df['level_2'] = new[1]
origin_codes_df['level_3'] = new[2]
origin_codes_df['level_4'] = new[3]
origin_codes_df['level_5'] = new[4]
origin_codes_df['level_5'] = new[5]
origin_codes_df['level_6'] = new[6]
origin_codes_df['level_7'] = new[7]
origin_codes_df['level_8'] = new[8]

origin_codes_df.to_csv('data/origin_codes_df.csv')


