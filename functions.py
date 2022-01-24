import pandas as pd


def level_checklist_data(df):
    '''Подготовка данных для чек-листа level_1'''
    level_1_checklist_data = []
    level_1_values = []
    for index, row in df.iterrows():
        dict_temp = {}
        dict_temp['label'] = " " + str(row['Код уровня']) + ' ' + str(row['Наименование'])
        dict_temp['value'] = row['code']
        level_1_checklist_data.append(dict_temp)
        level_1_values.append(row['code'])
    return level_1_checklist_data, level_1_values




def cut_df_by_dates_interval(df, date_field_name, start_date, end_date):
    """Выборка в диапазоне дат. Пример: date_field_name: 'close_date',  start_date, end_date - в формате datetime.date"""

    start_date = start_date
    end_date = end_date
    after_start_date = df.loc[:, date_field_name] >= start_date
    before_end_date = df.loc[:, date_field_name] <= end_date
    between_two_dates = after_start_date & before_end_date
    result_df = df.loc[between_two_dates]
    return result_df