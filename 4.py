import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:\skat_informatics\iris_data.csv")
SepalLength = list(df['SepalLengthCm'])
SepalWidth = list(df['SepalWidthCm'])

PetalLength = list(df['PetalLengthCm'])
PetalWidth = list(df['PetalWidthCm'])

x1 = np.array(SepalLength)
y1 = np.array(SepalWidth)

x2 = np.array(PetalLength)
y2 = np.array(PetalWidth)

A1 = np.vstack([x1, np.ones(len(x1))]).T
m1, c1 = np.linalg.lstsq(A1, y1, rcond=None)[0]

fig = plt.figure(figsize=(16, 9))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax1.plot(x1, y1, 'o', label='Данные', markersize=3)
ax1.plot(x1, m1 * x1 + c1, 'r' ,linewidth=3, label='Аппроксимация')
ax1.set_title('Комбинации длин и ширин чашелистников (Sepal)')
ax1.grid()

A2 = np.vstack([x2, np.ones(len(x2))]).T
m2, c2 = np.linalg.lstsq(A2, y2, rcond=None)[0]
ax2.plot(x2, y2, 'o', label='Данные', markersize=3)
ax2.plot(x2, m2 * x2 + c2,'r' , linewidth=3, label='Аппроксимация')
ax2.set_title('Комбинации длин и ширин лепестков (Petal)')
ax2.grid()

fig.show()
plt.show()