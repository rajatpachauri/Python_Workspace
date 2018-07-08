from matplotlib import pyplot as plt
from matplotlib import style
from matplotlib._layoutbox import align

# style.use('ggplot')
# style.use('grayscale')

x = [1,4,6,8]
y = [7,3,8,3]

x1 = [2,5,7,9]
y1 = [7,3,5,8]

# plt.plot(x,y)
'''
plt.plot(x,y,'g',linewidth=5, label = 'Line ine')
plt.plot(x1,y1,'c',linewidth=10, label = 'line two')
'''
'''
plt.scatter(x,y,color='g')
plt.scatter(x1,y1,color='c')
'''
plt.bar(x,y,color='g', align='center')
plt.bar(x1,y1,color='c')

plt.title('Rough chart')
plt.ylabel('Y axis')
plt.xlabel('X labels')
# plt.legend()

# plt.grid(True, color='k')

plt.show()