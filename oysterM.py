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

#files for sites are made...now to read them

     
class oyster:
    """This class defines population tolerances for salinity and temperature and population size."""

    def __init__(self, siteName, startSize, saltol, temptol):
        self.siteName= siteName
        self.startSize = startSize
        self.Sal = Sal
        self.Temp = Temp

    def currentSize(self):
        return self.generations[self.generations.count - 1]

#updating population size as conditions change over time
## for loops
    def updatePopSalinity(self, time, salinitylistname, templistname):
        newSize = self.currentSize()[0]        
	if (salinitylistname < self.saltol):
            newSize = newSize * .7
        if (salinitylistname < 1):
            newSize = newSize * .1
        if (templistname > self.temptol):
            newSize = newSize * .6
        if (salinitylistname == 20):
        newSize = newSize * 1.1

#creating method to pull salinity data
    def pullSalinity(self, filename= "", salintylistname=""):
        col_num = 2
        salinitylistname = []
        delimiter = "|"
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
            line = line.split(delimiter)[col_num]
            salinitylistname.append(line)

    def pullTemperature(self, filename= "", templistname=""):
        col_num = 1
        templistname = []
        delimiter = "|"
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
            line = line.split(delimiter)[col_num]
            templistname.append(line)

VB= oyster("Vermillion Bay",50,25)
pullsalinity("VBdata.txt", "VB_salinty")

CR= oyster("Calcaseiu River",50,5,25)
CB= oyster("Calliou Bay",50,15,25)
