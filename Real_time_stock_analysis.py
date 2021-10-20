#Real_time_stock_analysis

import pandas as pd
from alpha_vantage.timeseries import TimeSeries 
import time as t

api_key = "F0XNOB34LYS3PXKX"

ts = TimeSeries(key=api_key , output_format = "pandas")
data, meta_data = ts.get_intraday(symbol='AMZN', interval = "1min", outputsize = "full")
#print(data)

#while True:
  #  data, meta_data = ts.get_intraday(symbol='AAPL', interval = "1min", outputsize = "full")
   # data.to_excel("stocks_apple.xlsx")
    #t.sleep(60)

closing_data = data["4. close"]
percent_change = closing_data.pct_change()

print("last change: " + str(percent_change[-1]))

if abs(percent_change[-1]) > 0.0003:
    print ("Amazon volatility alert: " + str(percent_change[-1]))
