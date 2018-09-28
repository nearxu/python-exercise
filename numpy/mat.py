import numpy as np

from matplotlib import pyplot as plt 

# x = np.arange(1,11) 
# y =  2  * x +  5 
# plt.title("Matplotlib demo") 
# plt.xlabel("x axis caption") 
# plt.ylabel("y axis caption") 

x= np.arange(0,3*np.pi,0.1)
y = np.sin(x)

plt.plot(x,y) 
# plt.plot(x,y,'ob') 
plt.show()
