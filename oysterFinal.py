#!/usr/bin/env python
# this program simulates oyster populations in locations affected by salinity and temperature
# the goal is to visually represent the effects of freshwater events during the summer on oyster populations

#importing/loading matplotlib.pyplot and numpy
import matplotlib.pyplot as plt
import numpy as np

# defining the oyster population with attention to tolerances and sizes
class oysterpopulation: #creating oysterpopulation class
    """This is a class to define oyster populations"""

    #oysterpopulation constructor, defining class parameters
    def __init__(self, site, startSize, saltol, temptol):
        self.saltol = saltol
        self.temptol = temptol
        self.startSize = startSize
        self.site = site

    #defining function to pull data from oyster buoy site files
    def pulldata(self, fileName, columnIndex):
        data = [] #data values will be placed in a list
        delimiter = "|" #"pipe" character will be used to split string of values within file
        with open(fileName) as file: #opens the file of choice
            for line in file.readlines(): #lines will be read within the file
                line = line.split(delimiter)[columnIndex] #"pipe" delimiter will be placed at the column number indicated
                data.append(float(line)) #the data values will be appended to the data variable as floating/decimal numbers
        return data #returning data values 

    # pulling salinity data from USGS site files using pulldata function
    # make a list of salinities from a file
    def pullsalinity(self, fileName):
        return self.pulldata(fileName, 2)

    # pulling temperature data from USGS site files using pulldata function
    # make a list of temperatures from a file
    def pulltemperature(self, fileName):
        return self.pulldata(fileName, 1)

    #function to simulate population response to different salinity and temperature conditions
    def simulatePopulation(self, salinities, temperatures):
        populationSizes = [] #list of population sizes
        populationSizes.append(self.startSize) #initial population size appended to list of population sizes
        environments = zip(salinities, temperatures) #environment consists of compound effects of salinity and temperature
        salinityTimer = 240 #salinity conditions will persist for 5 days ((5 days)(48 data points per day retrieved from USGS))
        temperatureTimer = 240 #temperature conditions will persist for 5 days ((5 days)(48 data points per day retrieved from USGS))
        for environment in environments:
            salinity = environment[0] #salinity values will make up the 1st column in environments list
            temperature = environment[1] #temperature values will make up the 2nd column in environments list
            newSize = populationSizes[-1] #new population size corresponding to salinity and temperature values will make up 3rd column in environments list
            if (salinity < self.saltol): #if salinity conditions are less than oyster salinity tolerance
                salinityTimer = salinityTimer - 48 #salinity timer is reduced 48 data points (1 day); essentially salinity conditions will persist until the entire 5 days has passed
                if (salinityTimer <= 0): #after the 5 days under the less than ideal salinity conditions
                    newSize = newSize * .90 #90% of the oyster population will remain
            else:
                salinityTimer = salinityTimer + 48 #as time progresses (48 = time points per day)
            if (salinity < 1): #if salinity is less than 1
                salinityTimer = salinityTimer - 48 #as salinity conditions persist for 5 days total
                if (salinityTimer <= 0): #if salinity conditions remain at the end of the 5 days
                    newSize = newSize * .60 #new oyster population size will decrease by 40%
            if (temperature > self.temptol): #if the temperature is greater than oyster temperature tolerance 
                temperatureTimer = temperatureTimer - 48 #(temperature conditions persist for total of 5 days)
                if (temperatureTimer <= 0): #after the 5 days under the temperature conditions
                    newSize = newSize * .99 #99% of the oyster population will remain
            else:
                temperatureTimer = temperatureTimer + 48 #as time progresses (48 = time points per day)
            if (temperature == 20): #if temperature is 20 degrees Celsius
                temperatureTimer = temperatureTimer - 48 #temperature conditions will continue each day for 5 days
                if (temperatureTimer <= 0): #if temperature conditions reach the end of the 5 days
                    newSize = newSize * 1.5 #new population size will increase, oysters will spawn
            else:
                temperatureTimer = temperatureTimer + 48 
            populationSizes.append(newSize) #every 5 days, new oyster population size determined by environment conditions
                                            #will be appended to list of oyster population sizes

            #reseting all the condition timers
            #after 5 days is up, under the temperature conditions and under the salinity conditions, both timers will reset
            if temperatureTimer > 240:  
                temperatureTimer = 240 
            if salinityTimer > 240: 
                salinityTimer = 240 
            if temperatureTimer < 0: 
                temperatureTimer = 0
            if salinityTimer < 0:
                salinityTimer = 0
        return populationSizes[1:] #returns the values of the oyster population sizes


time = np.arange(2177) #time points will consist of range of 2177 values

#defining parameters for each oyster population location

#site = Vermillion Bay, starting population size = 10000, salinity tolerance = 5, temperature tolerance = 29
#blue
VB = oysterpopulation("Vermillion Bay", 10000, 5, 29) 
VBsalinities = VB.pullsalinity("VBAugSep.txt") #salinity data modified/pulled from VBAugSept.txt file
VBtemperatures = VB.pulltemperature("VBAugSep.txt") #temperature data modified/pulled from VBAugSept.txt file
VBpopulation = VB.simulatePopulation(VBsalinities, VBtemperatures) #oyster population simulation for location

#site = Calcasieu River, starting population size = 10000, salinity tolerance = 7, temperature tolerance = 29
#orange
CR = oysterpopulation("Calcasieu River", 10000, 7, 29)
CRsalinities = CR.pullsalinity("CRAugSep.txt") #salinity data modified/pulled from CRAugSep.txt file
CRtemperatures = CR.pulltemperature("CRAugSep.txt") #temperature data modified/pulled from CRAugSep.txt file
CRpopulation = CR.simulatePopulation(CRsalinities, CRtemperatures) #oyster population simulation for location

#site = Caillou Bay, starting population size = 10000, salinity tolerance = 14, temperature tolerance = 29
#green
CB = oysterpopulation("Caillou Bay", 10000, 14, 29)
CBsalinities = CB.pullsalinity("CBAugSep.txt") #salinity data modified/pulled from CBAugSep.txt file
CBtemperatures = CB.pulltemperature("CBAugSep.txt") #temperature data modified/pulled from CBAugSep.txt file
CBpopulation = CB.simulatePopulation(CBsalinities, CBtemperatures) #oyster population simulation for location

#plotting oyster population data with time on x-axis and population data for each site on y-axis
populationplot = plt.plot(time, VBpopulation) + plt.plot(time, CRpopulation) + plt.plot(time, CBpopulation)
plt.xlabel("Time point") ; plt.ylabel("Population Count") ; plt.title("Population of oysters over time") #setting axes titles and figure title

plt.show(populationplot) #display resulting figure

plt.savefig("PopulationData.png") #save resulting figure in a file PopulationData.png

#plotting salinity changes over time for each location with time on x-axis and site salinities on y-axis
salinityplot = plt.plot(time, VBsalinities) + plt.plot(time, CRsalinities) + plt.plot(time, CBsalinities)
plt.xlabel("Time point") ; plt.ylabel("Salinity (ppt)") ; plt.title("Salinity over time") #setting axes titles and figure title

plt.show(salinityplot) #display resulting salinity figure

plt.savefig("salinityplot.png") #save resulting figure in a file salinityplot.png

#plotting temperature changes over time for each location with time on x-axis and site temperatures on y-axis
temperatureplot = plt.plot(time, VBtemperatures) + plt.plot(time, CRtemperatures) + plt.plot(time, CBtemperatures)
plt.xlabel("Time point") ; plt.ylabel("Temperature (Celcius)") ; plt.title("Temperature over time") #setting axes titles and figure title

plt.show(temperatureplot) #display resulting temperature figure

plt.savefig("temperatureplot.png") #save resulting figure in a file temperatureplot.png