#!/usr/bin/env python


class oysterpopulation:
    """This is a class to define oyster populations"""

    def __init__(self, startSize, startTime, saltol, temptol):
        self.saltol = saltol
        self.temptol = temptol
        self.generations = [[startSize, startTime]]

    def currentSize(self):
        return self.generations[self.generations.count - 1]

    def updatePopulation(self, time, salinity, temperature):
        newSize = self.currentSize()[0]
        if (salinity > self.saltol):
            newSize = newSize * .9
        if (temperature > self.temptol):
            newSize = newSize * .9

        if (salinity > 20):
            newSize = newSize * 1.1

lowsal = oysterpopulation("time", 50, 10, 24)
highsal = oysterpopulation("time", 50, 35, 24)


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