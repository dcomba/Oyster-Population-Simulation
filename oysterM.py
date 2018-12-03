#!/usr/bin/env python
import numpy as np
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
                    newSize = newSize * .9
            else:
                salinityTimer = salinityTimer + 48
            if (salinity < 1):
                salinityTimer = salinityTimer - 48
                if (salinityTimer <= 0):
                    newSize = newSize * .6
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


VB = oysterpopulation("Vermillion Bay", 10000, 5, 29)
VBsalinities = VB.pullsalinity("VBAugSep.txt")
VBtemperatures = VB.pulltemperature("VBAugSep.txt")
VBpopulation = VB.simulatePopulation(VBsalinities, VBtemperatures)

CR = oysterpopulation("Calcasieu River", 10000, 7, 29)
CRsalinities = CR.pullsalinity("CRAugSep.txt")
CRtemperatures = CR.pulltemperature("CRAugSep.txt")
CRpopulation = CR.simulatePopulation(CRsalinities, CRtemperatures)

CB = oysterpopulation("Caillou Bay", 10000, 14, 29)
CBsalinities = CB.pullsalinity("CBAugSep.txt")
CBtemperatures = CB.pulltemperature("CBAugSep.txt")
CBpopulation = CB.simulatePopulation(CBsalinities, CBtemperatures)


# Plotting results
# setting time points (*******arange based on number of lines of data in Devin's files*****)
timeS = np.arange(2177) # generates consecutive numbers starting at zero (to act as time points on x axis)
timeT = np.arange(2177)
timeP = np.arange(2177)

#blue VB
#orange CR
#green CB

salinitiesPlot= plt.plot(timeS, VBsalinities) + plt.plot(timeS, CRsalinities) + plt.plot(timeS, CBsalinities)
plt.xlabel("time points") ; plt.ylabel("salinity(ppt)") ; plt.title("Salinity variation over two month span in Northern GOM")
plt.show(salinitiesPlot)
#plt.savefig("salinityPlot.png")

temperaturePlot= plt.plot(timeT, VBtemperatures) + plt.plot(timeT, CRtemperatures) + plt.plot(timeT, CBtemperatures)
plt.xlabel("time points") ; plt.ylabel("temperature(Celcius)") ; plt.title("Temperature variation over two month span in Northern GOM")
plt.show(temperaturePlot)
#plt.savefig("temperaturePlot.png")

populationPlot= plt.plot(timeP, VBpopulation) + plt.plot(timeP, CRpopulation) + plt.plot(timeP, CBpopulation)
plt.xlabel("time points") ; plt.ylabel("population size") ; plt.title("Population of Oysters over time")
plt.show(populationPlot)
#plt.savefig("temperaturePlot.png")
