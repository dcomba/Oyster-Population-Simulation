#!/usr/bin/env python
#this program simulates oyster populations in locations affected by salinity and temperature
#the goal is to visually represent the effects of freshwater events during the summer on oyster populations


#import matplotlib as plot
#import numpy as np


#defining the oyster population with attention to tolerances and sizes
class oysterpopulation:
    """This is a class to define oyster populations"""

    def __init__(self, site, startSize, saltol, temptol):
        self.saltol = saltol
        self.temptol = temptol
        self.size = startSize
        self.site = site

    #pulling salinity data from USGS site files
    #make a list of salinities from a file
    def pullsalinity(self, fileName):
        col_num = 2 #in the files containing salinity data, salinity values are in column 2
        salinities = [] #salinity values will be placed into a list
        delimiter = "|" #making the "pipe" character split a string
        with open(fileName) as file: #opening the fileName corresponding to the buoy site
            lines = file.readlines() #reading all the lines in the given buoy site file
            for line in lines: #in going line by line in the given file
                line = line.split(delimiter)[col_num] #in each line, column number 1 (temperature values) is split by the "pipe" character which is serving as the delimiter
                salinities.append(float(line)) #appending the newly delimited lines to a file as integers/list of numbers
        return salinities

    #pulling temperature data from USGS site files
    #make a list of temperatures from a file
    def pulltemperature(self, fileName):
        col_num = 1 #in the files containing temperature data, temperature values are in column 1
        temperatures = []
        delimiter = "|"
        with open(fileName) as file:
            lines = file.readlines()
            for line in lines:
                line = line.split(delimiter)[col_num]
                temperatures.append(float(line))
        return temperatures


    #updating population size as conditions change over time
    #need to make a list of population changes...how to do this?
    #maybe make this two methods? 
    #also need to include else conditions, otherwise it wont do anything
    def updatePopulation(self, salinities, temperatures):
        newSize = self.size
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
        self.size = newSize

#next step is to make our list of lists (salinites, temperatures, populations)

#delete size
#self.size will be defined as a list

VB = oysterpopulation("Vermillion Bay", 50, 2, 25)
VBsalinities = VB.pullsalinity("experimentalvb.txt")
VBtemperatures = VB.pulltemperature("experimentalvb.txt")
VB.updatePopulation(VBsalinities, VBtemperatures)

CR = oysterpopulation("Calcasieu River", 50, 5, 25)
CRsalinities = CR.pullsalinity("CalcRiv.txt")
CRtemperatures = CR.pulltemperature("CalcRiv.txt")
CR.updatePopulation(CRsalinities, CRtemperatures)

CB = oysterpopulation("Caillou Bay", 50, 15, 25)
CBsalinities = CB.pullsalinity("Caillou.txt")
CBtemperatures = CB.pulltemperature("Caillou.txt")
CB.updatePopulation(CBsalinities, CBtemperatures)

#pyplot ignore nan