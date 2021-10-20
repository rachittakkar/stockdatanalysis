#multiple_indicators_plot
#relative strength index

import pandas as pd
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

api_key = "F0XNOB34LYS3PXKX"

period = 60

ti = TechIndicators(key=api_key,output_format="pandas")

data_ti, meta_data_ti = ti.get_rsi(symbol="AAPL",interval="1min",time_period=period,series_type="close")
data_sma, meta_data_sma = ti.get_sma(symbol="AAPL",interval="1min",time_period=period,series_type="close")

df1= data_sma.iloc[1::]
df2= data_ti

df1.index = df2.index

fig, ax1 = plt.subplots()
ax1.plot(df1,"b-")
ax2=ax1.twinx()
ax2.plot(df2,"r.")

plt.title("SMA and RSI graph for Amazon")
plt.show()


