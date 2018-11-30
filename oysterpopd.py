#!/usr/bin/env python
# this program simulates oyster populations in locations affected by salinity and temperature
# the goal is to visually represent the effects of freshwater events during the summer on oyster populations

import matplotlib.pyplot as plt
import numpy as np

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


    def simulatePopulation(self, salinities, temperatures):
        populationSizes = []
        populationSizes.append(self.startSize)
        environments = zip(salinities, temperatures)
        salinityTimer = 240
        temperatureTimer = 240
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
                    newSize = newSize * .99
            else:
                temperatureTimer = temperatureTimer + 48
            if (temperature == 20):
                temperatureTimer = temperatureTimer - 48
                if (temperatureTimer <= 0):
                    newSize = newSize * 1.5
            else:
                temperatureTimer = temperatureTimer + 48
            populationSizes.append(newSize)
            if temperatureTimer > 240:
                temperatureTimer = 240
            if salinityTimer > 240:
                salinityTimer = 240
            if temperatureTimer < 0:
                temperatureTimer = 0
            if salinityTimer < 0:
                salinityTimer = 0
        return populationSizes[1:]


time = np.arange(2177)

#blue
VB = oysterpopulation("Vermillion Bay", 10000, 5, 29)
VBsalinities = VB.pullsalinity("VBAugSep.txt")
VBtemperatures = VB.pulltemperature("VBAugSep.txt")
VBpopulation = VB.simulatePopulation(VBsalinities, VBtemperatures)

#orange
CR = oysterpopulation("Calcasieu River", 10000, 7, 29)
CRsalinities = CR.pullsalinity("CRAugSep.txt")
CRtemperatures = CR.pulltemperature("CRAugSep.txt")
CRpopulation = CR.simulatePopulation(CRsalinities, CRtemperatures)

#green
CB = oysterpopulation("Caillou Bay", 10000, 14, 29)
CBsalinities = CB.pullsalinity("CBAugSep.txt")
CBtemperatures = CB.pulltemperature("CBAugSep.txt")
CBpopulation = CB.simulatePopulation(CBsalinities, CBtemperatures)


populationplot = plt.plot(time, VBpopulation) + plt.plot(time, CRpopulation) + plt.plot(time, CBpopulation)
plt.xlabel("Time point") ; plt.ylabel("Population Count") ; plt.title("Population of oysters over time")

plt.show(populationplot)

plt.savefig("PopulationData")

salinityplot = plt.plot(time, VBsalinities) + plt.plot(time, CRsalinities) + plt.plot(time, CBsalinities)
plt.xlabel("Time point") ; plt.ylabel("Salinity (ppt)") ; plt.title("Salinity over time")

plt.show(salinityplot)

plt.savefig("salinityplot")

temperatureplot = plt.plot(time, VBtemperatures) + plt.plot(time, CRtemperatures) + plt.plot(time, CBtemperatures)
plt.xlabel("Time point") ; plt.ylabel("Temperature (Celcius)") ; plt.title("Temperature over time")

plt.show(temperatureplot)

plt.savefig("temperatureplot")
