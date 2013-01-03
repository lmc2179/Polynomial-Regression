import math
# This file will compare models, find their error on a data set, and use K-fold cross validation to select the best model for a given dataset.

# Finds the MSE for a given estimator f over a dataset D = x,y; y are the correct values
def meanSquaredError(x,y,f):
	if(len(x) != len(y)):
		raise Exception("Input size different from output size")
	return (1.0/len(y)) * sum([math.pow(math.fabs(y[i] - f(x[i])),2) for i in range (0,len(x))])

# Finds the polynomial with order : {0...maxOrder} with the lowest 2-fold crossValidation Error
def 2FoldOrderChoose(maxOrder,x,y):	

