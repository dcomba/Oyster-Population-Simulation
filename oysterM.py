#!/usr/bin/env python

# pull from tsv from usgs current conditions during Gulf storm events 
# time, salinity, and temperature (over how many years?) 
# over one week, before during after storm for 4 different sites (LUMCON, Vermillion Bay, Calcaseiu Lake, Grand Isle)

class oyster:
    """This class defines population tolerances for salinity and temperature and population size."""

    def __init__(self, startSize, startTime, highSal, lowSal, highTemp, lowTemp, generations):
        self.startSize = startSize
        self.startTime = startTime
        self.highSal = highSal
        self.lowSal = lowSal
        self.highTemp = highTemp
        self.lowTemp = lowTemp
        self.generations = [[startSize, startTime]]

    def currentSize(self):
        return self.generations[self.generations.count - 1]

    def updatePopulation(self):
        newSize = self.startSize()[0]
        if (salinity > self.highSal):		# set the 'salinity' and 'temperature' variables
            newSize = newSize * 0.9		# ...with USGS current conditions data 
        if (salinity < self.lowSal):
            newSize = newSize * 0.9
        if (temperature > self.highTemp):
            newSize = newSize * 0.9
        if (temperature < self.lowTemp):
            newSize = newSize * 0.9		# will set survival percentage at more specific
						# ...thresholds later 
## FUTURE WORK
# add in reproduction rate in addition to survival rate
# pull data from USGS

