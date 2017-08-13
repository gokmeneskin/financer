import datetime as dt
import pickle
import pandas as pd 
import pandas_datareader as web
import talib as ta

with open('tickers.pickle', 'rb') as handle:
    tickers = pickle.load(handle)
hisseler = [ticker.replace(u'\u200b', '') for ticker in tickers]

end = dt.date.today()
start = end - dt.timedelta(days=60)

for hisse in hisseler:
    if hisse == 'IST:BOYP':
        pass
    try:
        df = web.DataReader(hisse, "google", start, end)
        df['RSI'] = ta.RSI(df['Close'].values, timeperiod=14)
        fastk, df['StochRSI'] = ta.STOCHRSI(df['Close'].values, timeperiod=14, fastk_period=14, fastd_period=3, fastd_matype=0)
        df['PDI'] = ta.PLUS_DI(df['High'].values, df['Low'].values, df['Close'].values, timeperiod=14)
        close = df['Close'].values[-1]
        rsi = df['RSI'].values[-1]
        stoch_rsi = df['StochRSI'].values[-1]
        pdi = df['PDI'].values[-1]
        date = end
        if rsi < 30 and stoch_rsi < 2 and pdi < 15:
            print(f'{hisse:10} {date} tarihinde {close} kapanışıyla RSI: {rsi:.2f}, StochRSI: {stoch_rsi:.2f}, PDI: {pdi:.2f} değerleri ile al sinyali verdi')
    except:
        print(f'{hisse} hesaplanırken hata oluştu!')
        pass


