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
        self.active = False
        self.volt_limit = 0
        self.delay = 0
        self.increment = 0
        self.data = []
        self.radio_setting = "nothing"
        super().__init__()
        self.ui = CircuitProberUI.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.run_button.clicked.disconnect()
        self.ui.run_button.clicked.connect(self.on_run_button_clicked)
        self.ui.copy_button.clicked.connect(self.copy_data)
        self.ui.voltage_sweep_radio.toggled.connect(lambda: self.update_radio_setting(valIn="Voltage Sweep"))
        self.ui.voltage_probe_radio.toggled.connect(lambda: self.update_radio_setting(valIn="Voltage Probe"))
        self.ui.current_sweep_radio.toggled.connect(lambda: self.update_radio_setting(valIn="Current Sweep"))
        self.ui.current_probe_radio.toggled.connect(lambda: self.update_radio_setting(valIn="Current Probe"))
        self.ui.resistance_sweep_radio.toggled.connect(lambda: self.update_radio_setting(valIn="Resistance Sweep"))
        self.ui.resistance_probe_radio.toggled.connect(lambda: self.update_radio_setting(valIn="Resistance Probe"))
        self.ui.nothing_radio.toggled.connect(lambda: self.update_radio_setting(valIn="Panel Test"))
        self.probe = pyvisa.ResourceManager()
        self.send_log('''Welcome to CircuitProber!''')
        self.send_log('UI Developed by Colson Pusley')
        self.send_log('''Adapted from Nikolas Kastor's projects and Michael's work at Core Electronics, Kotara, AU.  Licensed under CC BY-NC-SA 4.0 - http://creativecommons.org/licenses/by-nc-sa/4.0/''')
        self.send_log('')
        try:
            self.send_log(f"Resources available: {self.probe.list_resources()}")
            for resource in self.probe.list_resources():
                if "DP" in resource:
                    self.ui.channel_0.setText(resource)
                if "DM" in resource:
                    self.ui.channel_1.setText(resource)
        except Exception:
            self.send_log("Failed to detect any devices connected.")

    def update_radio_setting(self, valIn):
        self.radio_setting = valIn

    def send_log(self, valIn):
        self.ui.console_out.insertPlainText(valIn)
        self.ui.console_out.insertPlainText("\n")
        scrollbar = self.ui.console_out.verticalScrollBar()
        scrollbar.rangeChanged.connect(lambda min, max: scrollbar.setValue(max))

    def on_run_button_clicked(self):
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
        self.volt_limit = self.ui.volt_limit.value()
        self.volt_limit_2 = self.ui.volt_limit_2.value()
        self.volt_limit_3 = self.ui.volt_limit_3.value()
        self.delay = self.ui.curr_limit.value()
        self.increment = self.ui.increment_setting.value()
        self.send_log(f"Mode: {self.radio_setting}")

        if self.radio_setting == "Voltage Sweep":
            self.run_test('voltage', 'sweep')
        elif self.radio_setting == "Current Sweep":
            self.run_test('current', 'sweep')
        elif self.radio_setting == "Resistance Sweep":
            self.run_test('resistance', 'sweep')
        elif self.radio_setting == "Voltage Probe":
            self.run_test('voltage', 'probe')
        elif self.radio_setting == "Current Probe":
            self.run_test('current', 'probe')
        elif self.radio_setting == "Resistance Probe":
            self.run_test('resistance', 'probe')
        elif self.radio_setting == "Panel Test":
            data_test = [[1, 2, round(random.random(), 2)], [4, 5, 6], ["test", 5]]
            headers_test = ["applied volts", "recorded voltage"]
            self.update_table(headers_test, data_test)


    def run_test(self, setting: str, type: str):
        data_headers = ["applied volts", "recorded " + setting]
        data_collected = []
        rawSetting = ""
        if setting == "voltage":
            rawSetting = "VOLTage"
        elif setting == "current":
            rawSetting = "CURRent"
        elif setting == "resistance":
            rawSetting = "RESistance"
        else:
            self.send_log("Terminating due to internal error")
            return
        if type == 'probe':
            self.increment = 1

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
            supply.write(':APPL CH1,0,0.2')  # apply 0V, 0.2A
            supply.write(':OUTP CH2,OFF')  # start OFF - safe :)
            supply.write(':APPL CH2,0,0.2')  # apply 0V, 0.2A
            supply.write(':OUTP CH3,OFF')  # start OFF - safe :)
            supply.write(':APPL CH3,0,0.2')  # apply 0V, 0.2A
        except Exception:
            self.send_log("Failed to write to DMM")

        # Set the supply voltage to power the op-amp using CH2 and CH3
        supply.write(':APPL CH2,' + str(self.volt_limit_2) + ',0.2')
        supply.write(':APPL CH3,' + str(self.volt_limit_3) + ',0.2')

        # Run the test
        supply.write(':OUTP CH1,ON')
        v = round(self.volt_limit / self.increment, 4)
        while v <= self.volt_limit + 0.0001:  # sweep voltage up to 10V
            self.send_log(f"Testing at {v} volts on CH1")
            supply.write(':APPL CH1,' + str(v) + ',0.2')  # Set the voltage
            time.sleep(self.delay)
            # measure the voltage
            DMMoutput = dmm.query(f':MEASure:{rawSetting}:DC?')  # record the output of the dmm - OMIT :DC for resistance.
            vMeasured = float(DMMoutput)  # exctract the numerical values and store as float
            data_collected.append([DMMoutput, vMeasured])
            v += round(self.volt_limit / self.increment, 4)
        # Test complete. Turn supply off and zero the setpoints
        supply.write(':OUTP CH1,OFF')  # start OFF - safe :)
        supply.write(':APPL CH1,0,0.2')  # apply 0V, 0.2A
        supply.write(':OUTP CH2,OFF')  # start OFF - safe :)
        supply.write(':APPL CH2,0,0.2')  # apply 0V, 0.2A
        supply.write(':OUTP CH3,OFF')  # start OFF - safe :)
        supply.write(':APPL CH3,0,0.2')  # apply 0V, 0.2A
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
