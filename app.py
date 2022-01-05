import pandas as pd

level_2_df = pd.read_csv('data/level_2_selected_items.csv')
df1 = level_2_df[level_2_df['Код уровня'].astype(str).str.contains("RUD")]
print(df1)
