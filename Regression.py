import numpy
import pdb
import math

###############
#Basis function generators
###############

#Returns a monomial of the form ax^b

def monomial(a,b):
	return lambda x : a * math.pow(x,b)

#Returns a list of monomials forming a polynomial of the desired order

def polyList(order):
	return [monomial(1,i) for i in range(0,order+1)]

#Returns the sum of functions for a given input

def evaluate(functionList, x):
	return sum([f(x) for f in functionList])

#Returns the weighted sum, ie w0f0 + w1f1 +...

def weightedSum(w,F):
	if(len(w) != len(F)):
		raise Exception("Function/weight size mismatch")
	else:
		return lambda x:sum([w[i]*F[i](x) for i in range(0,len(w))])


###############
#Simple case: We fit the third order polynomial that works with the data using least squares.
###############

def polyTrain(x,y,order): 
	#Initialize the weight vector and design matrix
	w = [1 for i in range(0,order)]
	F = polyList(order)
	design = [[f(i) for f in F] for i in x]
	#Convert them to numpy arrays
	w = numpy.asarray(w)
	design = numpy.asarray(design)
	#We solve Ax=b, [x values x 3][coefficients]T = [yvalues]
	pinv = numpy.linalg.pinv(design)
	t = numpy.asarray(y).T
	#We know that the ML estimates for w are w* = pinv(design)y.T
	w = numpy.dot(pinv,t)
	return weightedSum(w,F)
