#!/usr/bin/env python
import numpy
import numpy.random as nr
import matplotlib.pyplot as plt
# oyster fact sheet website: https://www.sms.si.edu/irlspec/Crassostrea_virginica.htm 
#CONDITION THRESHOLDS FROM HOLLIS' MANUSCRIPT
	#Salinity (H 25ppt, M 15ppt, L 7ppt)
	#Temperature (W 35degC, C 20degC)
#LUMCON, Vermillion Bay, Lake Calcaseiu, Grand Isle
	#Vermillion Bay near Cypremort Point 07387040 (4.2 ± 3.1ppt)
    	#Calc River near Cameron 08017118 (11.4 ± 4.1ppt)
    	#Caminada Pass NW of Grand Isle 07380249 ()
    	#Caillou Bay SW of Cocodrie 073813498 ()
#make different files with data from different sites (one data file per site)
	#use data for salinity/temperature for all 4 sites 
	#modeled over 2 month span from August 1, 2017-September 30, 2017 to include Hurricane Harvey
#store output data (population size in an array)

#(several lines on one graph?)(Each condition with 4 lines for each pop?)
	#3 line graphs (salinity, temperature, combined salinity temperature)
	#4 populations on each graph
	#graph: x-axis(generations), y-axis(population-size) 

class oyster:
    """This class defines population tolerances for salinity and temperature and population size."""

    def __init__(self, siteName, startSize, startTime, highSal, lowSal, lowTemp, highTemp):
        self.siteName= siteName
        self.startSize = startSize
        self.startTime = startTime
        self.highSal = highSal
        self.lowSal = lowSal
        self.lowTemp = lowTemp
        self.highTemp = highTemp
        self.generations = [[startSize, startTime]]

    def currentSize(self):
        return self.generations[self.generations.count - 1]

    def updatePopulation(self):
        newSize = self.startSize()[0]
        if (salinity > self.highSal):		# set the 'salinity' and 'temperature' variables
            newSize = newSize * 0.9		# ...with USGS current conditions data 
        if (salinity < self.lowSal):
            newSize = newSize * 0.9
        if (temperature > self.highTemp):
            newSize = newSize * 0.9
       	if (temperature < self.lowTemp):	# will set survival percentage at more specific
            newSize = newSize * 0.9		# ...thresholds later 

VB= oyster(siteName= "Vermillion Bay", startSize=100 , startTime=0 , highSal=7.3, lowSal=1.1 , lowTemp=20, highTemp=35 )
CL= oyster(siteName= "Calcaseiu Lake", startSize=100 , startTime=0 , highSal=15.5, lowSal=7.3 , lowTemp=20, highTemp=35 )
GI= oyster(siteName= "Grand Isle", startSize=100 , startTime=0 , highSal=30, lowSal=16 , lowTemp=20, highTemp=35 )
LM= oyster(siteName= "LUMCON", startSize=100 , startTime=0 , highSal=28, lowSal=14, lowTemp=20, highTemp=35 )
# GI & LM have randomly assigned salinities atm (not in Hollis' manuscript)

LM_file = "LM_data.tsv"
inFile = (LM_file, 'r')
inFile = open(LM_file, 'r')
LM_salinity = []
for salinity in inFile:
    LM_salinity.append(salinity.split(' ')[0])
print(LM_salinity)

#VB_file = "VB_data.tsv"			# make VB_data.tsv file
#inFile = (VB_file, 'r')
#inFile = open(VB_file, 'r')

#CL_file = "CL_data.tsv"			# make CL_data.tsv file
#inFile = (CL_file, 'r')
#inFile = open(CL_file, 'r')

#GI_file = "GI_data.tsv"			# make GI_data.tsv file
#inFile = (GI_file, 'r')
#inFile = open(GI_file, 'r')
