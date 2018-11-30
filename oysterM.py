#!/usr/bin/env python
import numpy
import numpy.random as nr
import matplotlib.pyplot as plt
	#Vermillion Bay near Cypremort Point 07387040 (4.2 ± 3.1ppt)
    	#Calc River near Cameron 08017118 (11.4 ± 4.1ppt)
    	#Caillou Bay SW of Cocodrie 073813498 ()
class oysterpopulation:
    """This class defines population tolerances for salinity and temperature and population size."""

    def __init__(self, siteName, startSize=100, saltol, temptol):
        self.siteName= siteName
        self.size = [startSize]
        self.saltol = saltol
        self.temptol = temptol

#pulling salinity data from USGS site files
#make a list of salinities from a file
    def pullsalinity(self, fileName):
        col_num = 2
        salinities = []
        delimiter = "|"
        with open(fileName) as file:
            lines = file.readlines()
            for line in lines:
                line = line.split(delimiter)[col_num]
                salinities.append(float(line))
        return salinities
#pulling temperature data from USGS site files
#make a list of temperatures from a file
    def pulltemperature(self, fileName):
        col_num = 1
        temperatures = []
        delimiter = "|"
        with open(fileName) as file:
            lines = file.readlines()
            for line in lines:
                line = line.split(delimiter)[col_num]
                temperatures.append(float(line))
        return temperatures

#updating population size as conditions change over time
## APPEND NEW SIZE INTO UPDATE POP ARRAY FOR 1) TEMP 2) SIZE******* 
    def updatePopSize(self, salinities):
        newSize = self.size
        for sal in salinities:
            if (sal < self.saltol):
                newSize = newSize * .7
            if (sal < 1):
                newSize = newSize * .1
    def updatePopTemp(self, temperatures):        
        for temp in temperatures:
            if (temp > self.temptol):
                newSize = newSize * .6
            if (temp == 20):
                newSize = newSize * 1.1
        self.size = newSize

VB = oysterpopulation("Vermillion Bay", 50, 2, 25)
VBsalinities = VB.pullsalinity("VBAugSep.txt")
VBtemperatures = VB.pulltemperature("VBAugSep.txt")
VB.updatePopSal(VBsalinities)
VB.updatePopTemp(VBtemperatures)

CR = oysterpopulation("Calcasieu River", 50, 5, 25)
CRsalinities = CR.pullsalinity("CRAugSep.txt")
CRtemperatures = CR.pulltemperature("CRAugSep.txt")
CR.updatePopSal(CRsalinities)
CR.updatePopTemp(CRtemperatures)

CB = oysterpopulation("Caillou Bay", 50, 15, 25)
CBsalinities = CB.pullsalinity("CBAugSep.txt")
CBtemperatures = CB.pulltemperature("CBAugSep.txt")
CB.updatePopSal(CBsalinities)
CB.updatePopTemp(CBtemperatures)

# Plotting results
# graph: x-axis(time points), y-axis(population-size) 
# will have two different plots (salinity//temperature each with 3 lines for our different sites

# setting time points (*******arange based on number of lines of data in Devin's files*****)
time = np.arange(2101) # generates consecutive numbers starting at zero (to act as time points on x axis)

salinityPlot= plt.plot(time, VBsalinities) + plt.plot(time, CRsalinity) + plt.plot(time, CBsalinity)
plt.show(salinityPlot)

temperaturePlot= plt.plot()= plt.plot(time, VBtemperature) + plt.plot(time, CRsalinity) + plt.plot(time, CBsalinity)
plt.show(temperaturePlot)
