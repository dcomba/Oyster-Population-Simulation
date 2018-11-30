#!/usr/bin/env python
import numpy
import numpy.random as nr
import matplotlib.pyplot as plt
	#Vermillion Bay near Cypremort Point 07387040 (4.2 ± 3.1ppt)
    	#Calc River near Cameron 08017118 (11.4 ± 4.1ppt)
    	#Caillou Bay SW of Cocodrie 073813498 ()
class oysterpopulation:
    """This class defines population tolerances for salinity and temperature and population size."""

    def __init__(self, site, startSize, saltol, temptol):
        self.saltol = saltol
        self.temptol = temptol
        self.startSize = startSize
        self.site = site

    def pulldata(self, fileName, columIndex):
        data = []
        delimiter = "|"
        with open(fileName) as file:
            for line in file.readlines():
                line = line.split(delimiter)[columIndex]
                data.append(float(line))
        return data

    # pulling salinity data from USGS site files
    # make a list of salinities from a file
    def pullsalinity(self, fileName):
        return self.pulldata(fileName, 2)

    # pulling temperature data from USGS site files
    # make a list of temperatures from a file
    def pulltemperature(self, fileName):
        return self.pulldata(fileName, 1)

    # updating population size as conditions change over time
    # need to make a list of population changes...how to do this?
    # maybe make this two methods?
    # also need to include else conditions, otherwise it wont do anything
    def updatePopulation(self, salinities, temperatures):
        newSize = self.startSize
        for sal in salinities:
            if (sal < self.saltol):
                newSize = newSize * .7
            if (sal < 1):
                newSize = newSize * .1
        for temp in temperatures:
            if (temp > self.temptol):
                newSize = newSize * .6
            if (temp == 20):
                newSize = newSize * 1.1
        self.startSize = newSize

    def simulatePopulation(self, salinities, temperatures):
        populationSizes = []
        populationSizes.append(self.startSize)
        environments = zip(salinities, temperatures)
        salinityTimer = 10
        temperatureTimer = 10
        for environment in environments:
            salinity = environment[0]
            temperature = environment[1]
            newSize = populationSizes[-1]
            if (salinity < self.saltol):
                salinityTimer = salinityTimer - 1
                if (salinityTimer <= 0):
                    newSize = newSize * .7
            else:
                salinityTimer = salinityTimer + 1
            if (salinity < 1):
                salinityTimer = salinityTimer - 1
                if (salinityTimer <= 0):
                    newSize = newSize * .1
            if (temperature > self.temptol):
                temperatureTimer = temperatureTimer - 1
                if (temperatureTimer <= 0):
                    newSize = newSize * .6
            else:
                temperatureTimer = temperatureTimer + 1
            if (temperature == 20):
                temperatureTimer = temperatureTimer - 1
                if (temperatureTimer <= 0):
                    newSize = newSize * 1.1
            else:
                temperatureTimer = temperatureTimer + 1
            populationSizes.append(newSize)
            if temperatureTimer > 10:
                temperatureTimer = 10
            if salinityTimer > 10:
                salinityTimer = 10
            if temperatureTimer < 0:
                temperatureTimer = 0
            if salinityTimer < 0:
                salinityTimer = 0
        return populationSizes[1:]


VB = oysterpopulation("Vermillion Bay", 50, 2, 25)
VBsalinities = VB.pullsalinity("VBAugSep.txt")
VBtemperatures = VB.pulltemperature("VBAugSep.txt")
# VB.updatePopulation(VBsalinities, VBtemperatures)

CR = oysterpopulation("Calcasieu River", 50, 5, 25)
CRsalinities = CR.pullsalinity("CRAugSep.txt")
CRtemperatures = CR.pulltemperature("CRAugSep.txt")
# CR.updatePopulation(CRsalinities, CRtemperatures)

CB = oysterpopulation("Caillou Bay", 50, 15, 25)
CBsalinities = CB.pullsalinity("CBAugSep.txt")
CBtemperatures = CB.pulltemperature("CBAugSep.txt")
# CB.updatePopulation(CBsalinities, CBtemperatures)

for pop in CR.simulatePopulation(CRsalinities, CRtemperatures):
print(pop)

# Plotting results
# graph: x-axis(time points), y-axis(population-size) 
# will have two different plots (salinity//temperature each with 3 lines for our different sites

# setting time points (*******arange based on number of lines of data in Devin's files*****)
time = np.arange(2101) # generates consecutive numbers starting at zero (to act as time points on x axis)

salinityPlot= plt.plot(time, VBsalinities) + plt.plot(time, CRsalinity) + plt.plot(time, CBsalinity)
plt.show(salinityPlot)

temperaturePlot= plt.plot()= plt.plot(time, VBtemperature) + plt.plot(time, CRsalinity) + plt.plot(time, CBsalinity)
plt.show(temperaturePlot)
