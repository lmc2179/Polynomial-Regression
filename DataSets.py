import random
import Regression as R


# Generates a sample of points along the function x^3 + 2x^2 + 3x with uniform noise
def genData():
	x = [i for i in range(-20,20)]
	w = [random.randint(0,5) for i in range(0,4)]
	poly = R.weightedSum(w,R.polyList(3))
	y = [(poly (i)) for i in x]

	return [x,y]

def addGaussianNoise(x,B):
	return [random.gauss(i,1.0/B) for i in x]
