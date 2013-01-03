import matplotlib.pyplot as mpl

def lineSimple(x,y):
	mpl.plot(x,y)

def lineColor(x,y,color):
	mpl.plot(x,y,color)

def pointsSimple(x,y):
	mpl.plot(x,y,'b.')

def pointsColor(x,y,color): #Ex. bgrcmykw
	mpl.plot(x,y,color+'.')

def plotFunction(f,begin,end,step):
	x = [i for i in range(begin,end,step)]
	y = [f(i) for i in range(begin,end,step)]
	return x,y

def show():
	mpl.show()

