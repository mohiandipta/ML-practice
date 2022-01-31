import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#matplotlib version
#print(matplotlib.__version__)

#pyplot
# xpoints = np.array([0,30])
# ypoints = np.array([0,250])

#plotting x and y point
#using 'o' for showing DOT instead of line
#plt.plot(xpoint, ypoint, 'o')

# Multiple points
Apoints = np.array([1,2,6,8,4,6,4,7,3,9])
Bpoints = np.array([3,8,1,10,3,7,5,6,9,3])

# default x-points
Cpoints = np.array([3,8,1,10,5,7])

#set font family
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Graph", fontdict = font2)
plt.plot(Cpoints, 'o:b')
plt.show()

# marker Reference: ('o' = circle), ('*' = star), ('.' = point), (',' = pixel), ('x' = x).....