


import quandl
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import date, timedelta
API_KEY = 'sChmti2_VkZUQJtVPpbx'

# def get_date(pyear,pdays):
#     cur_date = datetime.datetime(pyear, 1, 1  )  # date.today()
#     t_date, f_date = str(cur_date), str(cur_date + timedelta(days=pdays))
#     return t_date,f_date

params = {'api_key': API_KEY}
response = requests.get('https://www.quandl.com/api/v3/datasets/FSE/BDT_X',params=params)
rows = response.json()['dataset']['data']

f_date = response.json()['dataset']['oldest_available_date']
t_date = response.json()['dataset']['newest_available_date']
f_year = pd.to_datetime(response.json()['dataset']['oldest_available_date']).year
t_year = pd.to_datetime(response.json()['dataset']['newest_available_date']).year

a7_data = quandl.get("FSE/BDT_X",api_key= API_KEY,\
                    start_date= f_date,end_date= t_date, collapse="weekly")

a30_data = quandl.get("FSE/BDT_X",api_key= API_KEY,\
                  start_date= f_date,end_date= t_date, collapse="monthly")

a90_data = quandl.get("FSE/BDT_X",api_key= API_KEY,\
                  start_date= f_date,end_date= t_date, collapse="quarterly")

ax = a7_data['Traded Volume'].plot(label='7 days')
a30_data['Traded Volume'].plot(ax=ax,label='30 days')
a90_data['Traded Volume'].plot(ax=ax,label='90 days')

a7_data['month'] = pd.to_datetime(a7_data.index.values).month
a7_data['year'] = pd.to_datetime(a7_data.index.values).year
df_by_month = a7_data.groupby(['year', 'month'], as_index=True, dropna=False).mean()
#df_by_month['Date'] = df_by_month['month'].map(str)+ '/' +df_by_month['year'].map(str)
ax=df_by_month.plot(label='Months')

leg = ax.legend()
plt.show()


import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np
stock =  pd.read_csv("data.csv")

d=5
stock["Marker"] = np.where(stock["Open"]<stock["Close"], stock["High"]+d, stock["Low"]-d)
stock["Symbol"] = np.where(stock["Open"]<stock["Close"], "triangle-up", "triangle-down")
stock["Color"] = np.where(stock["Open"]<stock["Close"], "green", "red")

Candle = go.Candlestick(x=stock.Date,
                       open=stock.Open,
                       high=stock.High,
                       low=stock.Low,
                       close=stock.Close
                       )

Trace = go.Scatter(x=stock.Date,
                   y=stock.Marker,
                   mode='markers',
                   name ='markers',
                   marker=go.Marker(size=20,
                                    symbol=stock["Symbol"],
                                    color=stock["Color"])
                   )
py.plot([Candle, Trace])


# df = pd.read_csv('data.csv',parse_dates=True)

#df = pd.DataFrame.from_dict(rows, orient='columns')
#df.columns = list(response.json()['dataset']['column_names'])
#df.to_csv('data.csv',index=False)

# df['Date'] = pd.to_datetime(df['Date'])
# df['month'] = pd.to_datetime(df['Date']).dt.month
# df['year'] = pd.to_datetime(df['Date']).dt.year
# df.sort_values('Date')
#df = df.set_index('Date')
#df['Traded Volume'].plot(figsize=(10,6))
#df.plot(x ='Date', y='Traded Volume', kind = 'bar',color='blue')

#df_90_days = df.loc['2015-01-01':'2018-12-31']
#df_90_days['Traded Volume'].plot(figsize=(15,8))
#df_90_days['moving_avg'] = df_90_days['Traded Volume'].rolling(window=30).mean().plot()
#plt.show()

#df_by_month = df.groupby(['year', 'month'], as_index=False, dropna=False).mean()
#df_by_month['Date'] = df_by_month['month'].map(str)+ '/' +df_by_month['year'].map(str)
#df_by_month.plot(x ='Date', y='Traded Volume', kind = 'bar',color='blue')




# mask = (df['Date'] > '2015-01-01') & (df['Date'] <= '2015-01-31')
# #df = df.set_index('Date')
# df_90_days = df.loc[mask]
# #df_90_days = df_90_days.set_index('Date')
# df_90_days.plot(x ='Date', y='Traded Volume', kind = 'bar',color='blue')
# df_90_days['Traded Volume'].rolling(window=30).mean().plot()
# plt.show()
# print(df)


