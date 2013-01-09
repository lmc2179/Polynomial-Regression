#This file allows the user to generate some basic functions for testing regression.
import random
import math
import Regression as R


# Generates a sample of points along a random polynomial.
def genData(order):
	x = [i for i in range(-100,100)]
	w = [random.randint(0,3) for i in range(0,order+1)]
	poly = R.weightedSum(w,R.polyList(order))
	y = [(poly (i)) for i in x]

	return [x,y]

# Generates a sine wave with amplitude 2000. Useful for testing cross-validation, as this function is prone to being overfit by polynomials when not properly handled.
def genNonPoly():
	x = [i for i in range(-100,100)]
	y = [2000*math.sin(i) for i in x]
	return [x,y]

#Adds Gaussian noise to a sent of entries, where B is the precision.
def addGaussianNoise(x,B):
	return [random.gauss(i,1.0/B) for i in x]
