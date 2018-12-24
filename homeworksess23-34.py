from matplotlib import pylab as plt
import pandas
from os import path


directory = path.dirname(__file__)

df1 = pandas.read_csv(path.join(directory, "stocks", "AMZN.csv"))
df1['Date'] = pandas.to_datetime(df1.Date)

df2 = pandas.read_csv(path.join(directory, "stocks", "WMT.csv"))
df2['Date'] = pandas.to_datetime(df2.Date)


plt.figure("first")
plt.plot(df1.Date, df1.High, "b-", label="Amazon", linewidth=0.8, ms=0.8)
plt.plot(df2.Date, df2.High, "r-", label="Walmart", linewidth=0.8, ms=0.8)

plt.legend(loc="upper left")

plt.show()
