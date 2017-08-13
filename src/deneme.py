import datetime as dt
import pickle
import pandas as pd 
import pandas_datareader as web
import talib as ta

end = dt.date.today()
start = end - dt.timedelta(days=120)

df = web.DataReader("IST:BOYP", "google", start, end)
df['RSI'] = ta.RSI(df['Close'].values, timeperiod=14)
fastk, df['StochRSI'] = ta.STOCHRSI(df['Close'].values, timeperiod=14, fastk_period=14, fastd_period=3, fastd_matype=0)
df['PDI'] = ta.PLUS_DI(df['High'].values, df['Low'].values, df['Close'].values, timeperiod=14)
rsi = df['RSI'].values[-1]
stoch_rsi = df['StochRSI'].values[-1]
pdi = df['PDI'].values[-1]
date = end
print(df.tail())
print(f'BOYP {date} tarihinde RSI: {rsi:.2f}, StochRSI: {stoch_rsi:.2f}, PDI: {pdi:.2f} değerleri ile al sinyali verdi')
    


