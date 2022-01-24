import pandas as pd
import datetime
from datetime import date, timedelta
import functions

orders = pd.read_csv('data/orders.csv')

# запланированные заказы APP1
app1_orders = orders.loc[orders['Вид заказа']=='APP1']

# конвертируем даты в даты
app1_orders = app1_orders.copy()
date_column_list = ['БазисСрокНачала']
for date_column in date_column_list:
    app1_orders.loc[:, date_column] = pd.to_datetime(app1_orders[date_column], infer_datetime_format=True, format='%d.%m.%Y')
    app1_orders.loc[:, date_column] = app1_orders.loc[:, date_column].apply(lambda x: datetime.date(x.year, x.month, x.day))
# сортируем по колонке close_event
app1_orders.sort_values(['БазисСрокНачала'], inplace=True)


first_day_of_selection = date(2022, 1, 1)
last_day_of_selection = date(2022, 1, 31)


orders_df_selected_by_dates = functions.cut_df_by_dates_interval(app1_orders, 'БазисСрокНачала',
                                                                        first_day_of_selection,
                                                                        last_day_of_selection)


# получаем список заказов с признаком УТВГ
orders_df_selected_by_dates = orders_df_selected_by_dates.copy()
user_status = orders_df_selected_by_dates['ПользовСтатус'].str.split(" "
#, expand = True
)
orders_df_selected_by_dates['user_status'] = user_status

utvg = []
for index, row in orders_df_selected_by_dates.iterrows():
  user_status = row['user_status']
  if 'УТВГ' in user_status or 'УТВГ*' in user_status:
    utvg.append(1)
  else:
    utvg.append(0)
orders_df_selected_by_dates['utvg'] = utvg

tkbe = []
for index, row in orders_df_selected_by_dates.iterrows():
  user_status = row['user_status']
  if 'ТКБЕ' in user_status or 'ТКБЕ*' in user_status:
    tkbe.append(1)
  else:
    tkbe.append(0)
orders_df_selected_by_dates['tkbe'] = tkbe

utvm = []
for index, row in orders_df_selected_by_dates.iterrows():
  user_status = row['user_status']
  if 'УТВМ' in user_status:
    utvm.append(1)
  else:
    utvm.append(0)
orders_df_selected_by_dates['utvm'] = utvm



orders_df_selected_by_dates.to_csv('data/orders_df_selected_by_dates.csv')

utvg_df = orders_df_selected_by_dates.loc[orders_df_selected_by_dates['ПользовСтатус'].isin(['УТВГ'])]


