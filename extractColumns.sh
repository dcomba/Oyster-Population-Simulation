#!/usr/bin/env bash
# FIRST MAKE SITE FILES NAMED 'VB_data.txt', 'CL_data.txt', 'GI_data.txt', 'LM_data.txt'
# CHANGE FILES BASED ON SITE 


# making VB temperature file
touch VBtemperature.txt
awk '{print $6}' VB_data.txt > VBtemperature.txt
# making VB salinity file  
touch VBsalinity.txt
awk '{print $8}' VB_data.txt > VBsalinity.txt

# making CL temperature file
touch CLtemperature.txt
awk '{print $6}' CL_data.txt > CLtemperature.txt
# making CL salinity file  
touch CLsalinity.txt
awk '{print $8}' CL_data.txt > CLsalinity.txt

# making GI temperature file
touch GItemperature.txt
awk '{print $6}' GI_data.txt > GItemperature.txt
# making GI salinity file  
touch GIsalinity.txt
awk '{print $8}' GI_data.txt > GIsalinity.txt

# making LM temperature file
touch LMtemperature.txt
awk '{print $6}' LM_data.txt > LMtemperature.txt
# making LM salinity file  
touch LMsalinity.txt
awk '{print $8}' LM_data.txt > LMsalinity.txt


