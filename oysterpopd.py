#!/usr/bin/env python
# this program simulates oyster populations in locations affected by salinity and temperature
# the goal is to visually represent the effects of freshwater events during the summer on oyster populations

import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt
import numpy as np
#time = np.arange(2100)


# defining the oyster population with attention to tolerances and sizes
class oysterpopulation:
    """This is a class to define oyster populations"""

    def __init__(self, site, startSize, saltol, temptol):
        self.saltol = saltol
        self.temptol = temptol
        self.startSize = startSize
        self.site = site

    def pulldata(self, fileName, columnIndex):
        data = []
        delimiter = "|"
        with open(fileName) as file:
            for line in file.readlines():
                line = line.split(delimiter)[columnIndex]
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
    #def updatePopulation(self, salinities, temperatures):
        #newSize = self.startSize
        #for sal in salinities:
            #if (sal < self.saltol):
                #newSize = newSize * .7
            #if (sal < 1):
                #newSize = newSize * .1
        #for temp in temperatures:
            #if (temp > self.temptol):
                #newSize = newSize * .6
            #if (temp == 20):
                #newSize = newSize * 1.1
        #self.startSize = newSize

    def simulatePopulation(self, salinities, temperatures):
        populationSizes = []
        populationSizes.append(self.startSize)
        environments = zip(salinities, temperatures)
        salinityTimer = 336
        temperatureTimer = 336
        for environment in environments:
            salinity = environment[0]
            temperature = environment[1]
            newSize = populationSizes[-1]
            if (salinity < self.saltol):
                salinityTimer = salinityTimer - 48
                if (salinityTimer <= 0):
                    newSize = newSize * .90
            else:
                salinityTimer = salinityTimer + 48
            if (salinity < 1):
                salinityTimer = salinityTimer - 48
                if (salinityTimer <= 0):
                    newSize = newSize * .60
            if (temperature > self.temptol):
                temperatureTimer = temperatureTimer - 48
                if (temperatureTimer <= 0):
                    newSize = newSize * .95
            else:
                temperatureTimer = temperatureTimer + 48
            if (temperature == 20):
                temperatureTimer = temperatureTimer - 48
                if (temperatureTimer <= 0):
                    newSize = newSize * 1.5
            else:
                temperatureTimer = temperatureTimer + 48
            populationSizes.append(newSize)
            if temperatureTimer > 336:
                temperatureTimer = 336
            if salinityTimer > 336:
                salinityTimer = 336
            if temperatureTimer < 0:
                temperatureTimer = 0
            if salinityTimer < 0:
                salinityTimer = 0
        return populationSizes[1:]


# next step is to make our list of lists (salinites, temperatures, populations)

#class timesdata:
    
    #def pulltimes(self, fileName, columnIndex):
        #data = []
        #delimiter = "|"
        #with open(fileName) as file:
            #for line in file.readlines():
                #line = line.split(delimiter)[columnIndex]
                #data.append(line)
        #return data

time = np.arange(2177)

#times = timesdata()
#timesforplot = times.pulltimes("CRAugSep.txt", 0)

VB = oysterpopulation("Vermillion Bay", 10000, 2, 25)
VBsalinities = VB.pullsalinity("VBAugSep.txt")
VBtemperatures = VB.pulltemperature("VBAugSep.txt")
VBpopulation = VB.simulatePopulation(VBsalinities, VBtemperatures)

CR = oysterpopulation("Calcasieu River", 10000, 5, 25)
CRsalinities = CR.pullsalinity("CRAugSep.txt")
CRtemperatures = CR.pulltemperature("CRAugSep.txt")
CRpopulation = CR.simulatePopulation(CRsalinities, CRtemperatures)

CB = oysterpopulation("Caillou Bay", 10000, 15, 25)
CBsalinities = CB.pullsalinity("CBAugSep.txt")
CBtemperatures = CB.pulltemperature("CBAugSep.txt")
CBpopulation = CB.simulatePopulation(CBsalinities, CBtemperatures)



#for pop in CR.simulatePopulation(CRsalinities, CRtemperatures):
    #print(pop)

populationplot = plt.plot(time, VBpopulation) + plt.plot(time, CRpopulation) + plt.plot(time, CBpopulation)
plt.xlabel("time points") ; plt.ylabel("population count") ; plt.title("Population of oysters over time")

plt.show(populationplot)



