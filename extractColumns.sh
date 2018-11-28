#!/usr/bin/env bash
## CHANGE FILES BASED ON SITE ##


# making LM temperature file
touch LMtemperature.txt
awk '{print $6}' LM_data.txt > LMtemperature.txt

# making LM salinity file  
touch LMsalinity.txt
awk '{print $8}' LM_data.txt > LMsalinity.txt



