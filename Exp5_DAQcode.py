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
# The sources cited within this document are utilized under the doctrine of fair use,     *
# in accordance with applicable copyright law.                                            *
#                                                                                         *
# See instructions on Canvas, or the Core Electronics website for set-up information.     *
#                                                                                         *
# CC BY-NC-SA 4.0                                                                         *
# This work is licensed under Attribution-NonCommercial-ShareAlike 4.0 International.     *
# To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/ *
#                               							  *
# This code is designed for Experiment 5: The Operational Amplifier.                      *
# The code uses CH2 and CH3 of the power supply becasue they share a common ground; 	  *
# and querries the voltage, current, and power from the supply;				  *
# and querries voltage from the DMM.	                                                  *
#                                                                                         *
#******************************************************************************************

# Import libraries
import pyvisa
import time
from time import sleep
import os

# Datalogging: create a time-stamped file
dateString = time.strftime("%Y-%m-%d_%H%M")
filepath = "./" + dateString + ".csv"

rm = pyvisa.ResourceManager()
# List all connected resources
print("Resources detected\n{}\n".format(rm.list_resources()))

# Put your device IDs here
supply = rm.open_resource('USB0::0x1AB1::0x0E11::DP8C182001474::INSTR') 
dmm = rm.open_resource('USB0::0x1AB1::0x09C4::DM3R184850533::INSTR')

# Setup Digital MultiMeter in DC Voltage measurement mode
dmm.write(':FUNCtion:VOLTage:DC') 

# Setup the power supply 0V, 200mA
supply.write(':OUTP CH1,OFF')   # start OFF - safe :)
supply.write(':APPL CH1,0,0.2') # apply 0V, 0.2A
supply.write(':OUTP CH2,OFF')   # start OFF - safe :)
supply.write(':APPL CH2,0,0.2') # apply 0V, 0.2A
supply.write(':OUTP CH3,OFF')   # start OFF - safe :)
supply.write(':APPL CH3,0,0.2') # apply 0V, 0.2A

# Turn on the supply CH1 and CH2
supply.write(':OUTP CH1,ON') 
supply.write(':OUTP CH2,ON') 

# Set the supply voltage to power the op-amp using CH2 and CH3
v1 = 15.0
v2 = 15.0
supply.write(':APPL CH1,' + str(v1) + ',0.2')
supply.write(':APPL CH2,' + str(v2) + ',0.2')

# Wait for a short period
sleep(1) 

# Set up the supply voltage for Vi on CH3
v3 = 0 #starting voltage
Visat = 0 #saturation voltage
increment = 0.5 #voltage sweep resolution

# Turn on the supply CH3
supply.write(':OUTP CH3,ON') 

# Run the test
while v3 <= Visat: # sweep voltage up to the saturation voltage Visat
	
    supply.write(':APPL CH3,' + str(v3) + ',0.2') # Change supply voltage to Vi

    sleep(0.5) # Wait for a short period

    # measure voltage
    DMMoutput = dmm.query(':MEASure:VOLTage:DC?') #record the output of the dmm
    Vo = float(DMMoutput)  #exctract the numerical values and store as float
	
    # print results to terminal
    print(" {}{}{}".format('Vout: ',Vo,"\n")) 

    # Write results to a file
    with open(filepath, "a") as file:
        if os.stat(filepath).st_size == 0: #if empty file, write a nice header
            file.write("Vin [V], Vout [V]\n")
        file.write("{:12.2f},{:13.5f}\n".format(v1, Vo)) # log the data
    file.close()
	
    v3 += increment

# Test complete. Turn supply off and zero the setpoints
supply.write(':OUTP CH1,OFF')
supply.write(':APPL CH1,0,0')
supply.write(':OUTP CH2,OFF')
supply.write(':APPL CH2,0,0')
supply.write(':OUTP CH3,OFF')
supply.write(':APPL CH3,0,0')
