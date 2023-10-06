import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [0,55.6,77.78,91.7,102,111,117.6,128.7,139]
y = [0,300,420,495,550,600,635,695,750]


plt.figure(figsize=(8,5), dpi=100)
plt.plot(x,y, 'b^-', label='I=U/R')
x2 = np.arange(0,4.5,0.5)



plt.title('График зависимости напряжения U от силы тока I', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.xlabel('I')
plt.ylabel('U')
plt.xticks([0,50,100,150,200])
plt.yticks([0,200,400,600,800])
plt.grid()
plt.legend()
plt.savefig('mygraph.png', dpi=300)
plt.show()
