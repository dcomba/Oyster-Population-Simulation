#!/usr/bin/env python
#this program simulates oyster populations in locations affected by salinity and temperature
#the goal is to visually represent the effects of freshwater events during the summer on oyster populations


#import matplotlib as plot

#files for sites are made...now to read them
#TEST FROM GOOGLE
col_num = 1
col_data = []
delimiter = "|"
with open("CalcRiv.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.split(delimiter)[col_num]
        print(line)
        col_data.append(line)

#defining the oyster population with attention to tolerances and sizes
class oysterpopulation:
    """This is a class to define oyster populations"""

    def __init__(self, site, startSize, saltol, temptol):
        self.saltol = saltol
        self.temptol = temptol
        self.startSize = startSize
        self.site = site

    def currentSize(self):
        return self.generations[self.generations.count - 1]

    #updating population size as conditions change over time
    def updatePopulation(self, time, salinity, temperature):
        newSize = self.currentSize()[0]
        if (salinity < self.saltol):
            newSize = newSize * .7
        if (salinity < 1):
            newSize = newSize * .1
        if (temperature > self.temptol):
            newSize = newSize * .6

        if (salinity == 20):
            newSize = newSize * 1.1

VB = oysterpopulation("Vermillion Bay", 50, 2, 25)
CR = oysterpopulation("Calcasieu River", 50, 5, 25)
CB = oysterpopulation("Caillou Bay", 50, 15, 25)


data = [
    [23,34],
    [23,34],
    [23,34],
    [23,34],
    [23,34],
    [23,34],
]

for timePeriod in data:
    lowsal.updatePopulation("time", timePeriod[0], timePeriod[1])