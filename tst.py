import yfinance as yf
import pandas as pd
import datetime

symbol = input('stock symbol: ')
print()

start_date = input('NOTE THAT THERE\'S PROBLEM INPUTING ONLY dd\nstart date by yyyy-mm-dd or mm-dd: ')
if len(start_date) == 2:
    now = datetime.datetime.now();
    start_date = "{}-{}-{}".format(
            now.year,
            str(now.month) if now.month >= 10 else '0' + str(now.month),
            start_date
        )
elif len(start_date) == 5:
    now = datetime.datetime.now();
    start_date = "{}-{}".format(now.year, start_date)
elif len(start_date) != 10:
    print('date length is not correct')
    exit(1)
# print('end_date = ' + end_date)
print()

end_date = input('NOTE THAT THERE\'S PROBLEM INPUTING ONLY dd\nend date by yyyy-mm-dd or mm-dd: ')
if len(end_date) == 2:
    now = datetime.datetime.now();
    end_date = "{}-{}-{}".format(
            now.year,
            str(now.month) if now.month >= 10 else '0' + str(now.month),
            end_date
        )
elif len(end_date) == 5:
    now = datetime.datetime.now();
    end_date = "{}-{}".format(now.year, end_date)
elif len(end_date) != 10 and len(end_date) != 0:
    print('date length is not correct')
    exit(1)
# print('end_date = ' + end_date)
print()

if end_date != '':
    data = yf.download(symbol, start=start_date, end=end_date, interval='1m')
else:
    data = yf.download(symbol, start=start_date, period='1d', interval='1m')
print(data.head())
data.to_csv(symbol + '.csv')
