import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(16, 9))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
values1 = np.random.normal(0, 100, 200000)
values2 = np.random.normal(0, 100, 100000)
ax1.hist(values1, 100)
ax1.set_title('first graph')
ax1.grid()
ax2.hist(values2, 100)
ax2.set_txttitle('second graph')
ax2.grid()
plt.show()