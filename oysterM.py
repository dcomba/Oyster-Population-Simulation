#!/usr/bin/env python
import numpy
import numpy.random as nr
import matplotlib.pyplot as plt
	#Vermillion Bay near Cypremort Point 07387040 (4.2 ± 3.1ppt)
    	#Calc River near Cameron 08017118 (11.4 ± 4.1ppt)
    	#Caillou Bay SW of Cocodrie 073813498 ()
	
     
class oyster:
    """This class defines population tolerances for salinity and temperature and population size."""

    def __init__(self, siteName, startSize, saltol, temptol):
        self.siteName= siteName
        self.startSize = startSize
        self.saltol = saltol
        self.temptol = temptol

#updating population size as conditions change over time
## APPEND NEW SIZE INTO UPDATE POP ARRAY FOR 1) TEMP 2) SIZE******* 
    def updatePopSal(self, time, salinitylistname, templistname):
        newSize = self.startsize[0]        
        if (salinitylistname < self.saltol):
            newSize = newSize * .7
        if (salinitylistname < 1):
            newSize = newSize * .1
    def updatePopTemp(self, time, salinitylistname, templistname):
        if (templistname > self.temptol):
            newSize = newSize * .6
        if (templistname == 20):
            newSize = newSize * 1.1

updatePopSal =
updatePopTemp = #use np.append to make individual site populationSize arrays (to later stack and graph as one master array with 3 arrays in it)


# make a master array from all of the individual 


#creating method to pull salinity data
    def pullSalinity(self,salinitylistname filename= ""):
        col_num = 2
        salinitylistname = []
        delimiter = "|"
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                line = line.split(delimiter)[col_num]
            salinitylistname.append(line)

    def pullTemperature(self, templistname, filename= ""):
        col_num = 1
        templistname = []
        delimiter = "|"
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                line = line.split(delimiter)[col_num]
            templistname.append(line)

VB= oyster("Vermillion Bay",50,2,25)
oyster.pullSalinity(VB_salinity, "Vermillion.txt")
oyster.pullTemperature(VB_temperature, "Vermillion.txt")		## ERROR VB_salinity not defined ****ASK****** lists??

CR= oyster("Calcaseiu River",50,5,25)
CB= oyster("Calliou Bay",50,15,25)

# Plotting results
#graph: x-axis(time points), y-axis(population-size) 
# time points generated using np.arange
# population-size is a master array for 3 different sites (made by np.stack)
# will have two different plots (salinity//temperature) 
	# ...each with 3 lines for our different sites

time = np.arange(17521) # generates consecutive numbers starting at zero (to act as time points on x axis)
salinityPopulation= #stacked array
temperaturePopulation= #stacked array

plt.plot(, growth, color="m")




#>>> np.stack((array1, array2, array3))
#array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])



