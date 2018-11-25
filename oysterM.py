#!/usr/bin/env python

#pull USGS data
#CONDITION THRESHOLDS FROM HOLLIS' MANUSCRIPT
	#Salinity (H 25ppt, M 15ppt, L 7ppt)
	#Temperature (W 35degC, C 20degC)
#LUMCON, Vermillion Bay, Lake Calcaseiu, Grand Isle
	#Vermillion Bay near Cypremort Point 07387040 (4.2 ± 3.1ppt)
    	#Calc River near Cameron 08017118 (11.4 ± 4.1ppt)
    	#Caminada Pass NW of Grand Isle 07380249 ()
    	#Caillou Bay SW of Cocodrie 073813498 ()
#make different files with data from different sites (one data file per site)
	#use data for salinity/temperature for all 4 sites 
	#modeled over 2 month span from August 1, 2017-September 30, 2017 to include Hurricane Harvey
#set up each site as a variable with all tolerances set									
						#***SET TOLERANCES (hollis data)***
	#VB= oyster(siteName= "Vermillion Bay", startSize= , startTime= , highSal=7.3, lowSal=1.1 , lowTemp=20, highTemp=35 )
	#CL= oyster(siteName= "Calcaseiu Lake", startSize= , startTime= , highSal=15.5, lowSal=7.3 , lowTemp=20, highTemp=35 )
	#GI= oyster(siteName= "Grand Isle", startSize= , startTime= , highSal=, lowSal= , lowTemp=20, highTemp=35 )
	#LM= oyster(siteName= "LUMCON", startSize= , startTime= , highSal =, lowSal= , lowTemp=20, highTemp=35 )
#read literature for ideas on how to format functions

#store output data (population size in an array)

#(several lines on one graph?)(Each condition with 4 lines for each pop?)
	#3 line graphs (salinity, temperature, combined salinity temperature)
	#4 populations on each graph
	#graph: x-axis(generations), y-axis(population-size) 

class oyster:
    """This class defines population tolerances for salinity and temperature and population size."""

    def __init__(self, siteName, startSize, startTime, highSal, lowSal, lowTemp=20, highTemp=35, generations):
        self.siteName= siteName
        self.startSize = startSize
        self.startTime = startTime
        self.highSal = highSal
        self.lowSal = lowSal
	self.lowTemp = lowTemp
        self.highTemp = highTemp
        self.generations = [[startSize, startTime]]

    def currentSize(self):
        return self.generations[self.generations.count - 1]

    def updatePopulation(self):
        newSize = self.startSize()[0]
        if (salinity > self.highSal):		# set the 'salinity' and 'temperature' variables
            newSize = newSize * 0.9		# ...with USGS current conditions data 
        if (salinity < self.lowSal):
            newSize = newSize * 0.9
        if (temperature > self.Temp):
            newSize = newSize * 0.9
       						# will set survival percentage at more specific
						# ...thresholds later 

VB= oyster(siteName= "Vermillion Bay", startSize= , startTime= , highSal=7.3, lowSal=1.1 , lowTemp=20, highTemp=35 )
CL= oyster(siteName= "Calcaseiu Lake", startSize= , startTime= , highSal=15.5, lowSal=7.3 , lowTemp=20, highTemp=35 )
GI= oyster(siteName= "Grand Isle", startSize= , startTime= , highSal=, lowSal= , lowTemp=20, highTemp=35 )
LM= oyster(siteName= "LUMCON", startSize= , startTime= , highSal =, lowSal= , lowTemp=20, highTemp=35 )

## FUTURE WORK
# add in reproduction rate in addition to survival rate
# pull data from USGS
# one salinty, one temp and one combined affects graph


