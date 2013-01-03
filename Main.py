### This file generates a random third order polynomial, adds Gaussian noise, and finds the Least Squares third order polynomial fit.
### This is a prototype for a more interesting class of regression programs, starting with a simple polynomial example.
import GraphData as Graph
import DataSets as Data
import Regression
import CrossValidation as CV
import pdb

#Generate the data from the basis function
D = Data.genData()

#Graph the points on the base polynomial
Graph.lineColor(D[0],D[1],'red')

#Add Gaussian noise to the data outputs
D[1] = Data.addGaussianNoise(D[1],1.0/2000)

#Graph them as points in blue
Graph.pointsSimple(D[0],D[1])

#Estimate the coefficients of the 3rd order polynomial
fit = Regression.polyTrain(D[0],D[1],3)

#Get the function's estimates for the training x values
z = [fit(i) for i in D[0]]

#Graph the points
Graph.lineColor(D[0],z,'g')

#Show the plot
Graph.show()
