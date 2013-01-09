# This includes wrapper functions for a handful of basic matplotlib functions.

import matplotlib.pyplot as mpl


#Graphing lins:
def lineSimple(x,y):
	mpl.plot(x,y)

def lineColor(x,y,color):
	mpl.plot(x,y,color)

#Graphing points
def pointsSimple(x,y):
	mpl.plot(x,y,'b.')

def pointsColor(x,y,color): #Ex. bgrcmykw
	mpl.plot(x,y,color+'.')

#Graphing functions with a particular interval and resolution
def plotFunction(f,begin,end,step):
	x = [i for i in range(begin,end,step)]
	y = [f(i) for i in range(begin,end,step)]
	return x,y

#Shows the plot.
def show():
	mpl.show()

