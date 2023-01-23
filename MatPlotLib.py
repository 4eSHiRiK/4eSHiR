# pip install matplotlib

# import matplotlib.pyplot as plt
#
# import matplotlib.pyplot as plt
# year = [1950, 1975, 2000, 2018]
# population = [2.12, 3.681, 5.312, 6.981]
# plt.plot(year, population)
# plt.show()



# import matplotlib.pyplot as plt
# year = [1950, 1975, 2000, 2018]
# population = [2.12, 3.681, 5.312, 6.981]
# plt.scatter(year, population)
# plt.show()
# plt.axis([0,5,0,20])
# plt.title('My first plot')
# plt.plot([1,2,3,4],[1,4,9,16],'ro')
# plt.show()



# import matplotlib.pyplot as plt
# values = [0, 1.2, 1.3, 1.9, 4.3, 2.5, 2.7, 4.3, 1.3, 3.9]
# plt.hist(values, bins = 4)
# plt.show()

#
# import numpy as np
# import matplotlib.pyplot as plt
# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# cos, sin = np.cos(X), np.sin(X)
# plt.plot(X, cos)
# plt.plot(X, sin)
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# cos, sin = np.cos(X), np.sin(X)
# plt.plot(X, cos, color='blue', label = 'cosine')
# plt.plot(X, sin, color='red', label = 'sine')
# plt.legend(loc='upper left',frameon = False)
# plt.show()

#
# import matplotlib.pyplot as plt; plt.rcdefaults()
# import numpy as np
# import matplotlib.pyplot as plt
# names = ('Tom', 'Dick', 'Harry', 'Jill', 'Meredith', 'George')
# y_pos = np.arange(len(names))
# speed = [8, 7, 12, 4, 3, 2]
# plt.bar(y_pos, speed, align='center', alpha=0.5)
# plt.xticks(y_pos, names)
# plt.ylabel('Speed')
# plt.title('Person')
# plt.show()



# import matplotlib.pyplot as plt
# names = 'Tom', 'Dick', 'Harry', 'Jill', 'Meredith', 'George'
# speed = [8, 7, 12, 4, 3, 2]
# colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'blue']
# explode = (0.1, 0, 0, 0, 0, 0)
# plt.pie(speed, explode=explode, labels=names, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
# plt.axis('equal')
# plt.show()

import numpy as np
import numpy.random
import matplotlib.pyplot as plt
temperature = np.random.randn(4096)
anger = np.random.randn(4096)
heatmap, xedges, yedges = np.histogram2d(temperature, anger, bins=(64,64))
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
plt.clf()
plt.ylabel('Anger')
plt.xlabel('Temp')
plt.imshow(heatmap, extent=extent)
plt.show()
