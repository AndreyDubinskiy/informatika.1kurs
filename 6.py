import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:\skat_informatics\BTC_data.csv")
Timedurty = list(df['time'])
Close = list(df['close'])
Time = []
TimeNumbers = []

for i in range(len(Timedurty)):
    Time.append(Timedurty[i][8:10] + Timedurty[i][4:8] + Timedurty[i][2:4])

x = np.array(Time)
y = np.array(Close)
for i in range(len(Time)):
    TimeNumbers.append(i+1)
x1 = np.array(TimeNumbers)


plt.figure(figsize=(16,9), dpi=100)
plt.plot(x, y, 'g', label='Price BTC')
plt.xticks(Time[::150])
plt.title('Мечта финансиста', fontdict={'fontname': 'sans-serif', 'fontsize': 20})

coefficients = np.polyfit(x1, y, 3)

p = np.poly1d(coefficients)

x_fit = np.linspace(x1.min(), x1.max(), 1457)

y_fit = p(x_fit)

plt.plot(x_fit, y_fit, label='The approximate price of BTC', color='r')

plt.grid()
plt.legend()
plt.show()