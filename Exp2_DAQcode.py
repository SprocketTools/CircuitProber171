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

# Run the test
supply.write(':OUTP CH1,ON') # Turn on the supply
v = 0 # Starting voltage
while v <= 10.0: # sweep voltage up to max Voltage
    supply.write(':APPL CH1,' + str(v) + ',0.2') # Set the voltage on supply
    sleep(0.5) # Increment hold time in seconds.

    # measure the voltage
    DMMoutput = dmm.query(':MEASure:VOLTage:DC?') #record the output of the dmm
    vMeasured = float(DMMoutput)  #exctract the numerical values and store as float

    # Write results to console
    print("{}  {}".format(v, vMeasured))

    # Write results to a file
    with open(filepath, "a") as file:
        if os.stat(filepath).st_size == 0: #if empty file, write a nice header
            file.write("Setpoint [V], Measured [V]\n")
        file.write("{:12.2f},{:13.5f}\n".format(v, vMeasured)) # log the data
    file.close()

    v += 0.5 # Add Voltage increment


# Test complete. Turn supply off and zero the setpoints
supply.write(':OUTP CH1,OFF')
supply.write(':APPL CH1,0,0')