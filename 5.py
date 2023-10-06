import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv("C:\skat_informatics\BTC_data.csv")
TIME = list(df['time'])
The_last_column = list(df['close'])
Time = []
for i in range(len(TIME)):
    Time.append(TIME[i][8:10] + TIME[i][4:8] + TIME[i][:4])
x = np.array(Time)
y = np.array(The_last_column)


plt.figure(figsize=(16,9),dpi=100)
plt.plot(x,y,'k',label='Price_BTC')
plt.xticks(Time[::150])
plt.title('Price of bitcoin', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.show()