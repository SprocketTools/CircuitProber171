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
# This code is designed for Experiment 4: Thevenin Equivalent Circuits.                   *
# The code sets the voltage of CH1 of the power supply to a known value; 	          *
# and querries the voltage, current, and power from the supply;				  *
# and querries the measured value of choice (resistance or voltage) from the DMM.	  *
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
supply = rm.open_resource('USB0::0x1AB1::0x0E11::DP8C182001474::INSTR') 
dmm = rm.open_resource('USB0::0x1AB1::0x09C4::DM3R184850533::INSTR')

# Setup the power supply 0V, 200mA
supply.write(':OUTP CH1,OFF')   # start OFF - safe :)
supply.write(':APPL CH1,0,0.2') # apply 0V, 0.2A

# Turn on the supply
supply.write(':OUTP CH1,ON') 

# Set the supply voltage
v1 = 15.0
supply.write(':APPL CH1,' + str(v1) + ',0.2')

# Wait for a short period
sleep(1) 

# Query the voltage, current and power measured on the output terminal of the specified channel of the Supply. 
supplyV1 = supply.query(':MEAS:ALL? CH1')
print(" {}{}".format('CH1 (V,A,W): ',supplyV1)) # print to terminal

# measure resistance
dmm.write(':FUNCtion:RESistance') # Setup Digital MultiMeter in DC Resistance measurement mode
sleep(1) # wait a bit
DMMoutput = dmm.query(':MEASure:RESistance?') #record the output of the dmm
measuredValue = float(DMMoutput)  #exctract the numerical values and store as float
print(" {}{}{}".format('Measured_Resistance: ',measuredValue,"\n"))  # print to terminal

## measure voltage
#dmm.write(':FUNCtion:VOLTage:DC') # Setup Digital MultiMeter in DC Voltage measurement mode
#sleep(1) # wait a bit
#DMMoutput = dmm.query(':MEASure:VOLTage:DC?') #record the output of the dmm
#measuredValue = float(DMMoutput)  #exctract the numerical values and store as float
#print(" {}{}{}".format('Measured_Voltage: ',measuredValue,"\n"))  # print to terminal

# Wait for a short period
sleep(1) 

# Test complete. Turn supply off and zero the setpoints
supply.write(':OUTP CH1,OFF')
supply.write(':APPL CH1,0,0')
