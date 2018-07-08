from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

x,y = np.loadtxt('exampleFile.txt',
                 unpack = True,
                 delimiter = ',')

plt.plot(x,y)

plt.title('Rough chart')
plt.ylabel('Y axis')
plt.xlabel('X labels')

plt.show()

