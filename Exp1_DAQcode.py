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

#('USB0::0x1AB1::0x09C4::DM3R183001617::INSTR', 'USB0::0x1AB1::0x0E11::DP8C182001548::INSTR')

supply = rm.open_resource('USB0::0x1AB1::0x0E11::DP8C182001548::INSTR') # Put your device IDs here
dmm = rm.open_resource('USB0::0x1AB1::0x09C4::DM3R183001617::INSTR') #USB0::0x1AB1::0x0E11::DP8C182001548::INSTR

# Setup Digital MultiMeter in DC Voltage mode
dmm.write(':FUNCtion:VOLTage:DC')

# Setup the power supply 0V, 200mA
supply.write(':OUTP CH1,OFF')   # start OFF - safe :)
supply.write(':APPL CH1,0,0.2') # apply 0V, 0.2A
supply.write(':OUTP CH2,OFF')   # start OFF - safe :)
supply.write(':APPL CH2,0,0.2') # apply 0V, 0.2A
supply.write(':OUTP CH3,OFF')   # start OFF - safe :)
supply.write(':APPL CH3,0,0.2') # apply 0V, 0.2A
# Run the test
supply.write(':OUTP CH1,ON')
supply.write(':OUTP CH2,ON')
supply.write(':OUTP CH3,ON')

# apply voltages to the static channels
supply.write(':APPL CH1,' + str(v1) + ',0.2')
supply.write(':APPL CH2,' + str(v2) + ',0.2')

v = 0
while v <= 10.0: # sweep voltage up to 10V
    supply.write(':APPL CH1,' + str(v) + ',0.2')            # Set the voltage
    sleep(0.5)

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

    v += 0.5


# Test complete. Turn supply off and zero the setpoints
supply.write(':OUTP CH1,OFF')
supply.write(':APPL CH1,0,0')