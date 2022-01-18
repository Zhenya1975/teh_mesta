import pandas as pd

teh_mesta_full_list = pd.read_csv('data/origin_codes_df.csv', dtype=str)
teh_mesta_full_list.fillna('no_data', inplace=True)

# по умолчанию result_df - это полный список всех техмест
result_df = teh_mesta_full_list

level_1_full_value_list = teh_mesta_full_list['level_1'].unique() # полный список уникальных значений из level_1
level_2_full_value_list = teh_mesta_full_list['level_2'].unique() # полный список уникальных значений из level_2
level_3_full_value_list = teh_mesta_full_list['level_3'].unique() # полный список уникальных значений из level_3
level_4_full_value_list = teh_mesta_full_list['level_4'].unique() # полный список уникальных значений из level_4
level_5_full_value_list = teh_mesta_full_list['level_5'].unique() # полный список уникальных значений из level_5
level_6_full_value_list = teh_mesta_full_list['level_6'].unique() # полный список уникальных значений из level_6
level_7_full_value_list = teh_mesta_full_list['level_7'].unique() # полный список уникальных значений из level_7
level_8_full_value_list = teh_mesta_full_list['level_8'].unique() # полный список уникальных значений из level_8
level_upper_full_value_list = teh_mesta_full_list['level_upper'].unique() # полный список уникальных значений из level_upper

def initial_result_df_prep(filter_level_1, filter_level_2, filter_level_3, filter_level_4, filter_level_5, filter_level_upper):
  if len(filter_level_1)==0:
    level_1_filters = level_1_full_value_list
  else:
    level_1_filters = filter_level_1
  
  if len(filter_level_2)==0:
    level_2_filters = level_2_full_value_list
  else:
    level_2_filters = filter_level_2
  
  if len(filter_level_3)==0:
    level_3_filters = level_3_full_value_list
  else:
    level_3_filters = filter_level_3

  if len(filter_level_4)==0:
    level_4_filters = level_4_full_value_list
  else:
    level_4_filters = filter_level_4
  
  if len(filter_level_5)==0:
    level_5_filters = level_5_full_value_list
  else:
    level_5_filters = filter_level_5
  
  if len(filter_level_upper)==0:
    level_upper_filters = level_upper_full_value_list
  else:
    level_upper_filters = filter_level_upper
  
  initial_result_df = result_df.loc[
    result_df['level_1'].isin(level_1_filters)&
    result_df['level_2'].isin(level_2_filters)&
    result_df['level_3'].isin(level_3_filters)&
    result_df['level_4'].isin(level_4_filters)&
    result_df['level_5'].isin(level_5_filters)&
    result_df['level_upper'].isin(level_upper_filters)
  ]
  eo_list = pd.read_csv('data/eo_list.csv')
  result_df_eo = pd.merge(initial_result_df, eo_list, on='teh_mesto', how = 'left')
  result_df_eo.to_csv('data/result_df_eo.csv')

  return initial_result_df, result_df_eo