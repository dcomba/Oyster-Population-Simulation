#!/usr/bin/env python

# pull from tsv from usgs current conditions
# time, salinity, and temperature (over how many years?) 
# over 2 months, before during after storm for 4 different sites (LM, VB, CL, GI)

class oyster:
    """This class defines population tolerances for salinity and temperature and population size."""

    def __init__(self, size, highSal, lowSal, highTemp, lowTemp, gen):
        self.size = size
        self.highSal = highSal
        self.lowSal = lowSal
        self.highTemp = highTemp
        self.lowTemp = lowTemp
        self.generations = 

    def updatePop(self):

