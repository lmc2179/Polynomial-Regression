import math
import random
import Regression
import numpy as np
import pdb
import copy
# This file will compare models, find their error on a data set, and use K-fold cross validation to select the best model for a given dataset.

# Finds the MSE for a given estimator f over a dataset D = x,y; y are the correct values
def meanSquaredError(x,y,f):
	if(len(x) != len(y)):
		raise Exception("Input size different from output size")
	return (1.0/len(y)) * sum([math.pow(math.fabs(y[i] - f(x[i])),2) for i in range (0,len(x))])

# Splits that dataset D  = [x,y] into k equal size sets, with any remainder in the last set.
def kSplit(D,k):
	indices = [i for i in range(0,len(D[0]))]
	random.shuffle(indices)
	xS = [D[0][i] for i in indices]
	yS = [D[1][i] for i in indices]
	split = len(xS) / k
	xy = []
	for i in range(0,k-1):
		xy.append([xS[i*split:(i+1)* split],yS[i*split:(i+1)* split]])
	i = k-1
	xy.append([xS[i*split:len(xS)],yS[i*split:len(yS)]])	
	
	return xy

# Wrapper function for the numpy argmin function

def argmin(list):
	a = np.array(list)
	return a.argmin()

# Finds the polynomial with order : {0...maxOrder} with the lowest squared error
def squaredErrorChoose(x,y,maxOrder):
	e = [0 for i in range(0,maxOrder)]
	for order in range(1,maxOrder+1):
		f = Regression.polyTrain(x,y,order)
		e[order-1] = meanSquaredError(x,y,f)
	return min(e[i] for i in range(0,len(e))),(argmin(e)+1)

# Find the polynomial with the smallest k-fold error

def kFoldErrorChoose(x,y,maxOrder,k): #TODO
	e = [0 for i in range(0,maxOrder)]
	d = kSplit([x,y],k)
#	pdb.set_trace()
	for order in range(1,maxOrder+1):
		sumError = 0
		for i in range(0,k): #The current partition to use: the ith partition is used as test data.
			Dcopy = copy.copy(d)
			dtest = Dcopy.pop(i)
			dtrain = Dcopy[0]
			f = Regression.polyTrain(dtrain[0],dtrain[1],order)
			sumError += meanSquaredError(dtest[0],dtest[1],f)
		e[order-1] = sumError/(k * 1.0)
	return min(e[i] for i in range(0,len(e))),(argmin(e)+1)
