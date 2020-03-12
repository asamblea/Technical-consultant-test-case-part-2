import pandas as pd
import datetime
from decimal import Decimal
import numpy as np

raw_data = pd.read_excel("sales_data_2019_1-3_1.xlsx")
# print(raw_data)

raw_data.columns = ['pos', 'transaction','date', 'amount']
col_n=['transaction','date', 'amount']
intermediate_data = pd.DataFrame(raw_data,columns = col_n)
# print(intermediate_data)
intermediate_data = intermediate_data.sort_values(by=['date'])
# print(intermediate_data['date'])
intermediate_data.reset_index(drop=True, inplace=True)
t = datetime.datetime.strptime(str(intermediate_data['date'][0]), '%Y-%m-%d %H:%M:%S')
year = t.year
month = t.month
day = t.day
hour = t.hour
minute = (t.minute//15)*15
# print(year,month,day,hour,minute, t.second)
standard = datetime.datetime(year=year,month=month,day=day,hour=hour, minute=minute,second=0)
# print(standard.date(), standard.time(), len(intermediate_data['date']))
# print(standard+datetime.timedelta(minutes=15))
# output_t = "{}-{}-{}T{}:{}:00.000000Z".format(year,month,day,hour,minute)
sales = Decimal('0.00')
transactions = 0
result = None
for i in range(0, len(intermediate_data['date'])):
    tmp = intermediate_data.iloc[i]

    if tmp['date'] >= standard and tmp['date'] < standard+datetime.timedelta(minutes=15):
        sales += Decimal(str(tmp['amount']))
        transactions += 1
    else:
        if result is None:
            result = np.array([str(standard.date())+"T"+str(standard.time())+"0000Z", str(sales),transactions])
        else:
            result = np.vstack((result, [str(standard.date())+"T"+str(standard.time())+"0000Z", str(sales),transactions]))
        standard = standard+datetime.timedelta(minutes=15)
        sales = Decimal('0.00')
        transactions = 0
        sales += Decimal(str(tmp['amount']))
        transactions += 1
result = np.vstack((result, [str(standard.date())+"T"+str(standard.time())+"0000Z", str(sales),transactions]))
new_col_n = ['Time','Sales', 'Transactions']
result = pd.DataFrame(result,columns = new_col_n)
# print(result)
result.to_csv("result.csv", index=False)
