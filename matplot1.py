# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:12:50 2018

@author: hp india
"""

from matplotlib import pyplot as plt
x=np.aranimport numpy as np
ge(1,10) 
plt.subplot(2,1,1)
y=2*x+50
plt.plot(x,y,color='g');
plt.show()
plt.subplot(2,1,2)
x=np.arange(0,2*np.pi,0.1)
y=np.sin(x)
plt.plot(x,y,color='lime');
plt.show()
x1=np.arange(0,2*np.pi,0.1)
y1=np.cos(x1)
plt.plot(x1,y1,color='lime');
plt.show()
x2=np.arange(0,2*np.pi,0.1)
y2=np.tan(x2)
plt.plot(x2,y2,color='lime');
plt.show()

x7=[4,9,5]
y7=[5,3,2]
plt.bar(x7,y7,color='r',align='center')
plt.show()