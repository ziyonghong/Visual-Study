import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

aapl=pd.read_csv('G:\BaiduNetdiskDownload\python\Data\AAPL.csv')
print(aapl.head())
aapl=aapl[::-1] #reverse
#aapl['Adj Close'].plot()
#aapl['Close'].plot()
#aapl['Adj Close'].plot.bar()
#plt.show()

df=pd.DataFrame(np.random.randint(100,size=(5,2)),columns=['male','female'])
print(df.head())
df.plot.bar()
plt.show()