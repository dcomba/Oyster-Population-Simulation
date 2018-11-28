#!/usr/bin/env bash
## CHANGE FILES BASED ON SITE ##


# for LM temperature 
touch LMtemperature.txt
awk '{print $8}' LM_data.txt > LMtemperature.txt

# for LM salinity 
touch LMsalinity.txt
awk '{print $6}' LM_data.txt > LMsalinity.txt



