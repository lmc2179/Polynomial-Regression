import math
import random
import Regression
import numpy as np
# This file will compare models, find their error on a data set, and use K-fold cross validation to select the best model for a given dataset.

# Finds the MSE for a given estimator f over a dataset D = x,y; y are the correct values
def meanSquaredError(x,y,f):
	if(len(x) != len(y)):
		raise Exception("Input size different from output size")
	return (1.0/len(y)) * sum([math.pow(math.fabs(y[i] - f(x[i])),2) for i in range (0,len(x))])

#Takes a dataset D, D[0] = x, D[1] = y; splits it into D1 and D2 of equal size.
def randomSplit(D):
	indices = [i for i in range(0,len(D[0]))]
	random.shuffle(indices)
	xS = [D[0][i] for i in indices]
	yS = [D[1][i] for i in indices]
	split = len(xS) / 2
	x1 = xS[0:split]
	y1 = yS[0:split]
	x2 = xS[split:len(xS)]
	y2 = yS[split:len(yS)]
	return [x1,y1], [x2,y2]

def argmin(list):
	a = np.array(list)
	return a.argmin()

# Finds the polynomial with order : {0...maxOrder} with the lowest squared error
def squaredErrorChoose(x,y,maxOrder):	#TODO Finish implementing for 2-fold case; get cross error and choose best model, not just min error
	e = [0 for i in range(0,maxOrder)]
	for order in range(1,maxOrder+1):
		f = Regression.polyTrain(x,y,order)
		e[order-1] = meanSquaredError(x,y,f)
	return min(e[i] for i in range(0,len(e))),(argmin(e)+1)
