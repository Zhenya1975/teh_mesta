import pandas as pd


def level_1_checklist_data(df):
    '''Подготовка данных для чек-листа level_1'''
    level_1_checklist_data = []
    level_1_values = []
    for index, row in df.iterrows():
        dict_temp = {}
        dict_temp['label'] = " " + str(row['Код уровня']) + ' ' + str(row['Наименование'])
        dict_temp['value'] = row['Код уровня']
        level_1_checklist_data.append(dict_temp)
        level_1_values.append(row['Код уровня'])
    return level_1_checklist_data, level_1_values
