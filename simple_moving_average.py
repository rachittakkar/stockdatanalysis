#simple_moving_average of a stock

import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

api_key = "F0XNOB34LYS3PXKX"

ts = TimeSeries(key=api_key, output_format="pandas")
data_ts, meta_data_ts = ts.get_intraday(symbol = "APLE", interval = "1min", outputsize="full")

period = 60
ti = TechIndicators(key=api_key, output_format="pandas")
data_ti, meta_data_ti = ti.get_sma(symbol = "APLE", interval = "1min", time_period = period, series_type="close")

df1 = data_ti
df2 = data_ts['4. close'].iloc[period-1::]
df3 = data_ts.iloc[period-1::]

excel_df = pd.concat([df1,df3], axis=1)
total_df = pd.concat([df1, df2], axis=1)
print(total_df)

excel_df.to_excel("apple_sma_output.xlsx")

total_df.plot()
plt.show()
