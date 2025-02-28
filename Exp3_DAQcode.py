# 
#   __|   \ |   __|  _ \                                              
#   _|   .  |  (_ |    /                                              
#  ___|\_|\\||\___| _|_\__|  __| \ \   / __|   \ |     _ \   \ |  __| 
#   (   | .  |  _|    \__ \  _|   \ \ /  _|   .  |    (   | .  |  _|  
#  \___/ _|\_| ___|   ____/ ___|   \_/  ___| _|\_|   \___/ _|\_| ___|                                                                   
#                                                                                                                        
# *****************************************************************************************
# ******************* Rigol Power Supply and DMM Data Aquisition Code *********************
# *****************************************************************************************
#                                                                                         *
# Nikolas Kastor, PhD.                                                                    *
# Allan Hancock College                                                                   *
# Spring 2024                                                                             *
#                                                                                         *
# Adapted from Michael's work at Core Electronics, Kotara, AU.                            *
# https://core-electronics.com.au/guides/automating-test-equipment-with-python/           *
#                                                                                         *
# See instructions on Canvas, or the Core Electronics website for set-up information.     *
#                                                                                         *
# CC BY-NC-SA 4.0                                                                         *
# This work is licensed under Attribution-NonCommercial-ShareAlike 4.0 International.     *
# To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/ *
#                               							  *
# This code is designed for Experiment 3: Superposition.                                  *
# The code sets the voltage of CH1 and CH2 of the power supply to known values; 	  *
# and querries the voltage, current, and power from the supply;				  *
# and querries the measured value of choice from the DMM.				  *
#                                                                                         *
#******************************************************************************************

# Import libraries
import pyvisa
import time
from time import sleep
import os

rm = pyvisa.ResourceManager()
# List all connected resources
print("Resources detected\n{}\n".format(rm.list_resources()))

# Put your device IDs here

for resource in rm.list_resources():
    if "DP" in resource:
        supply = rm.open_resource(resource)
    if "DM" in resource:
        dmm = rm.open_resource(resource)



# Setup Digital MultiMeter in DC Voltage measurement mode
dmm.write(':FUNCtion:VOLTage:DC')

# Setup the power supply 0V, 200mA
supply.write(':OUTP CH1,OFF')   # start OFF - safe :)
supply.write(':OUTP CH2,OFF')   # start OFF - safe :)
supply.write(':APPL CH1,0,0.2') # apply 0V, 0.2A
supply.write(':APPL CH2,0,0.2') # apply 0V, 0.2A

# Turn on the supply
supply.write(':OUTP CH1,ON') 
supply.write(':OUTP CH2,ON') 

# Set the supply voltage
v1 = 16.0
v2 = 12.0
supply.write(':APPL CH1,' + str(v1) + ',0.2')
supply.write(':APPL CH2,' + str(v2) + ',0.2')
sleep(1) # Wait for a short period

# measure the voltage
DMMoutput = dmm.query(':MEASure:VOLTage:DC?') #record the output of the dmm
measuredValue = float(DMMoutput[11:26])  #exctract the numerical values and store as float

# Query the voltage, current and power measured on the output terminal of the specified channel of the Supply. 
supplyV1 = supply.query(':MEAS:ALL? CH1')
supplyV2 = supply.query(':MEAS:ALL? CH2') 

# Write results to console
print(" {}{}".format('CH1 (V,A,W): ',supplyV1))
print(" {}{}".format('CH2 (V,A,W): ',supplyV2))
print(" {}{}{}".format('Measured_Value: ',measuredValue,"\n"))
sleep(2) # Wait for a short period

# Test complete. Turn supply off and zero the setpoints
supply.write(':OUTP CH1,OFF')
supply.write(':APPL CH1,0,0')
supply.write(':OUTP CH2,OFF')
supply.write(':APPL CH2,0,0')