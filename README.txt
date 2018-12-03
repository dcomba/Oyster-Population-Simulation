Group members: Adora, Devin, Megan 
BIOL 4800 (Intro to Comp Bio)
Oyster Population Simulation
script name: oysterpopd.py


As climate change continues to reshape our world, it is crucial to understand how biological populations respond to catastrophes. The eastern oyster (C. virginica) is of particular interest as it is a vital part to Louisiana's economy. The Louisiana Department of Wildlife and Fisheries states that, “Louisiana’s commercial oyster industry, which accounts for almost 4,000 jobs, has an economic impact of $317 million annually.” During the months modeled in this script Hurricane Harvey developed in the Gulf of Mexico (GOM) resulting in lower salinities across the Northern GOM due to increased rainfall. C. virginica are osmoconformers and as temperature increases, they have a harder time acclimating to lower salinities. From this phenomenon we can see a synergistic effect of high temperature and low salinity on C. virginica populations.  

Our script simulates C. virginica populations under different salinities and temperatures from three sites across the Northern GOM from early August 2017 through late September 2017. The three sites across south Louisiana have been assigned specific low salinity and high temperature tolerances roughly based on data pulled from the literature (Jones et al in prep). Sites are named as follows: Vermillion Bay (VB), Calcasieu River (CR), and Caillou Bay (CB). The temperature tolerances for all populations were set at 29 degrees Celsius. The low salinity tolerances were 5ppt (VB), 7ppt (CR), and 14ppt (CB). 

The salinity and temperature data for these sites for August-September 2017 were obtained from the USGS Current Conditions webpage which contains a database of environmental conditions collected by buoys along the coast. Data was collected every 0.5 hours meaning there are 48 data points (or "time points") per day and 240 time points for 5 days. Our script pulls the salinity/temperature data from the USGS website and then compares the tolerances set for each population to the data collected. Salinity and temperature effects are combined with a 'zip' function to model population numbers after the two month period during which Hurricane Harvey hit the Gulf coast. Our 'simulatePopulation' function sets thresholds (based on a 'timer' function) for the salinity and temperature data simulating how each population would respond to these changing conditions. The 'timer' within the simulation function requires a certain salinity/temperature threshold to be met for 5 days (240 time points) before you would see a change in the population. The 'timer' resets every day (48 time points) if the threshold condition is not met.

Updated population sizes through all of the time points are stored in 'VBpopulation', 'CRpopulation', and 'CBpopulation' and plotted as basic line plots. Additionally, the raw temperature and salinity data are also plotted as line plots for a visual comparison between the environmental data and population data.



