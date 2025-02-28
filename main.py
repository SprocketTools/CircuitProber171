import os, random, pygame, datetime
import pandas as pd
from playsound3 import playsound
import webbrowser
import sys, time, pyvisa, pyvisa_py
#install zeroconf, pyvisa, and pyvisa-py
from asyncio import wait_for

from PyQt6 import QtWidgets, uic, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDockWidget, QFormLayout, QLineEdit, QWidget, QPushButton, QSpinBox, QMessageBox, QToolBar, QMessageBox
from PyQt6.QtCore import QTimer, Qt
import CircuitProberUI
class Dialog(QtWidgets.QDialog):
    def __init__(self):
        try:
            pygame.init()
            if getattr(sys, 'frozen', False):
                # If the app is running as a bundle (frozen executable)
                bundle_dir = sys._MEIPASS
                audio_file = os.path.join(bundle_dir, 'assets/background.mid')
            else:
                # If running from source code (not bundled)
                audio_file = 'assets/background.mid'
            self.mid = pygame.mixer.music.load(audio_file)
        except FileNotFoundError:
            print(f"Error: MIDI file not found at 'background.mid'")
            return
        self.channel_setting = ""
        self.active = False
        self.volt_limit = 0
        self.delay = 0
        self.psuStatus = False
        self.increment = 0
        self.data = []
        self.radio_setting = "nothing"
        super().__init__()
        self.ui = CircuitProberUI.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.run_button.clicked.disconnect()
        self.ui.run_button.clicked.connect(self.on_run_button_clicked)
        self.ui.copy_button.clicked.connect(self.copy_data)

        # Make connections between everything
        self.ui.voltage_radio.toggled.connect(lambda: self.update_radio_setting(valIn="Voltage"))
        self.ui.current_radio.toggled.connect(lambda: self.update_radio_setting(valIn="Current"))
        self.ui.resistance_radio.toggled.connect(lambda: self.update_radio_setting(valIn="Resistance"))
        self.ui.channel_0_radio.toggled.connect(lambda: self.update_radio_setting(valIn="Channel 0"))
        self.ui.channel_1_radio.toggled.connect(lambda: self.update_radio_setting(valIn="Channel 1"))
        self.ui.channel_2_radio.toggled.connect(lambda: self.update_radio_setting(valIn="Channel 2"))
        self.ui.channel_3_radio.toggled.connect(lambda: self.update_radio_setting(valIn="Channel 3"))

        self.probe = pyvisa.ResourceManager()
        self.send_log('''Welcome to CircuitProber!''')
        self.send_log('UI Developed by Colson Pusley')
        self.send_log('''Adapted from Nikolas Kastor's projects and Michael's work at Core Electronics, Kotara, AU.  Licensed under CC BY-NC-SA 4.0 - http://creativecommons.org/licenses/by-nc-sa/4.0/''')
        self.send_log('')
        self.send_log(f"Resources available: {self.probe.list_resources()}")
        self.send_log('')
        self.send_log("Note: don't worry if CircuitProber freezes when you run it, let it finish and then it will unfreeze.")  # debugging logs
        self.send_log(" ")
        try:
            for resource in self.probe.list_resources():
                if "DP" in resource:
                    self.ui.channel_0.setText(resource)
                if "DM" in resource:
                    self.ui.channel_1.setText(resource)
        except Exception:
            self.send_log("Failed to detect any devices connected.")

    def update_radio_setting(self, valIn):
        if "Channel" in valIn:
            self.channel_setting = valIn
        else:
            self.radio_setting = valIn

    def send_log(self, valIn):
        self.ui.console_out.insertPlainText(valIn)
        self.ui.console_out.insertPlainText("\n")
        scrollbar = self.ui.console_out.verticalScrollBar()
        scrollbar.rangeChanged.connect(lambda min, max: scrollbar.setValue(max))

    def on_run_button_clicked(self):
        if random.random() < 0.1:
            self.send_log("Frying electronics now.  Stand back...")
            self.send_log("   ")
        else:
            self.send_log(f"Beginning testing.")  # debugging logs

        #choose if music is played or not
        d = datetime.datetime.now()
        odds = 1
        if d.month == 10 and d.day > 25:
            odds = 30
        if d.month == 4 and d.day < 8:
            odds = 50
        if random.random() < 0.002*odds:
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                # check if playback has finished
                print("hi")
                clock = pygame.time.Clock()
                clock.tick(30)
        print("Hi")

        #recheck variables
        self.psuStatus = self.ui.psuRecord.isChecked()
        self.volt_limit = self.ui.volt_limit.value()
        self.volt_limit_2 = self.ui.volt_limit_2.value()
        self.volt_limit_3 = self.ui.volt_limit_3.value()
        self.delay = self.ui.curr_limit.value()
        self.increment = self.ui.increment_setting.value()

        if self.radio_setting == "Panel Test":
            data_test = [[1, 2, round(random.random(), 2)], [4, 5, 6], ["test", 5]]
            headers_test = ["applied volts", "recorded voltage"]
            self.update_table(headers_test, data_test)
        else:
            self.run_test()


    def run_test(self): #, setting: str, type: str
        setting = self.radio_setting
        data_collected = []
        rawSetting = ""
        rawChannel = ""
        if setting == "Voltage":
            rawSetting = "VOLTage"
        elif setting == "Current":
            rawSetting = "CURRent"
        elif setting == "Resistance":
            rawSetting = "RESistance"
        else:
            self.send_log("Terminating due to internal error")
            return
        if self.channel_setting == 'Channel 0':
            self.increment = 1
            rawChannel = "CH1"
        else:
            rawChannel = "CH" + str(self.channel_setting).split(" ")[1]

        #print(str(self.ui.channel_0.text()))
        try:
            supply = self.probe.open_resource(self.ui.channel_0.toPlainText())  # Put your device IDs here
        except Exception:
            self.send_log(" Failed to connect PSU")
            return

        try:
            dmm = self.probe.open_resource(self.ui.channel_1.toPlainText())
        except Exception:
            self.send_log("Failed to connect DMM")
            return

        # Setup Digital MultiMeter in DC Voltage mode
        try:
            dmm.write(f':FUNCtion:{rawSetting}:DC')
        except Exception:
            self.send_log("Failed to write to DMM")

        # Setup the power supply 0V, 200mA
        try:
            supply.write(':OUTP CH1,OFF')  # start OFF - safe :)
            supply.write(':OUTP CH2,OFF')  # start OFF - safe :)
            supply.write(':OUTP CH3,OFF')  # start OFF - safe :)
            supply.write(':APPL CH1,0,0.2')  # apply 0V, 0.2A
            supply.write(':APPL CH2,0,0.2')  # apply 0V, 0.2A
            supply.write(':APPL CH3,0,0.2')  # apply 0V, 0.2A
        except Exception:
            self.send_log("Failed to write to DMM")

        if self.channel_setting != "Channel 1":
            supply.write(':APPL CH1,' + str(self.volt_limit) + ',0.2')
        if self.channel_setting != "Channel 2":
            supply.write(':APPL CH2,' + str(self.volt_limit_2) + ',0.2')
        if self.channel_setting != "Channel 3":
            supply.write(':APPL CH3,' + str(self.volt_limit_3) + ',0.2')

        supply.write(':OUTP CH1,ON')
        supply.write(':OUTP CH2,ON')
        supply.write(':OUTP CH3,ON')



        if rawChannel == "CH1":
            sweep_limit = self.volt_limit
        elif rawChannel == "CH2":
            sweep_limit = self.volt_limit_2
        elif rawChannel == "CH3":
            sweep_limit = self.volt_limit_3

        # Run the sweep test.  This will run regardless of whether the software is set to probe, and simply just sets the value again in this case.
        v = round(sweep_limit / self.increment, 4) # set the starting increment
        while v <= sweep_limit + 0.0001:  # sweep voltage up to 10V
            self.send_log(f"Testing at {v} volts on {rawChannel}") # debugging logs
            print(f':APPL {rawChannel},' + str(v) + ',0.2')
            supply.write(f':APPL {rawChannel},' + str(v) + ',0.2')  # Set the voltage
            print("aft")
            time.sleep(self.delay) #let the data stabilize
            if rawSetting == 'RESistance':
                DMMoutput = dmm.query(f':MEASure:{rawSetting}?')  # record the output of the dmm - OMIT :DC for resistance.
            else:
                DMMoutput = dmm.query(f':MEASure:{rawSetting}:DC?') # measure the voltage or current
            vMeasured = float(DMMoutput)  # exctract the numerical values and store as float
            
            #if set to record PSU data, include it here
            if self.psuStatus:
                supplyData = supply.query(':MEAS:ALL? CH1')
                data_headers = ["applied voltage", f"recorded {setting}", "PSU voltage", "PSU current", "PSU watts"]
                psudata = supplyData.replace("\n", "").split(",")
                data_collected.append([v, vMeasured, psudata[0], psudata[1], psudata[2]])
            else:
                data_headers = ["applied voltage", f"recorded {setting}"]
                data_collected.append([v, vMeasured]) #add the data to the table
            v += round(sweep_limit / self.increment, 4) # increment the data and continue

        # Test complete. Turn supply off and zero the setpoints
        supply.write(':OUTP CH1,OFF')  # start OFF - safe :)
        supply.write(':APPL CH1,0,0.2')  # apply 0V, 0.2A
        supply.write(':OUTP CH2,OFF')  # start OFF - safe :)
        supply.write(':APPL CH2,0,0.2')  # apply 0V, 0.2A
        supply.write(':OUTP CH3,OFF')  # start OFF - safe :)
        supply.write(':APPL CH3,0,0.2')  # apply 0V, 0.2A

        #update the table
        self.update_table(data_headers, data_collected)

    def update_table(self, headers_in, data_in):
        self.ui.tableWidget.clear()
        self.table = QtWidgets.QTableView()
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setColumnCount(len(headers_in))
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setHorizontalHeaderLabels(headers_in)
        for row in data_in:
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)
            self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount())
            i = 0
            for item in row:
                self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, i, QTableWidgetItem(str(item)))
                i+=1

        df = pd.DataFrame(data_in)
        df.columns = headers_in
        df.to_clipboard()
        self.data = data_in
        self.send_log("Table updated and pasted to clipboard.")

    def copy_data(self):
        df = pd.DataFrame(self.data)
        df.to_clipboard()
        self.send_log("Table pasted to clipboard.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec())
