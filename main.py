import random
import pandas as pd
import webbrowser
import sys, time, pyvisa #install zeroconf, pyvisa, and pyvisa-py
from asyncio import wait_for

from PyQt6 import QtWidgets, uic, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDockWidget, QFormLayout, QLineEdit, QWidget, QPushButton, QSpinBox, QMessageBox, QToolBar, QMessageBox
from PyQt6.QtCore import QTimer, Qt
import CircuitProberUI
class Dialog(QtWidgets.QDialog):
    def __init__(self):
        self.volt_limit = 0
        self.delay = 0
        self.increment = 0
        self.radio_setting = "nothing"
        super().__init__()
        self.ui = CircuitProberUI.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.run_button.clicked.connect(self.on_run_button_clicked)
        self.ui.sweep_radio.toggled.connect(lambda: self.update_radio_setting(valIn="sweep"))
        self.ui.nothing_radio.toggled.connect(lambda: self.update_radio_setting(valIn="nothing"))
        self.probe = pyvisa.ResourceManager()
        self.send_log(f"Resources available: {self.probe.list_resources()}")
        for resource in self.probe.list_resources():
            if "DP" in resource:
                self.ui.channel_0.setText(resource)
            if "DM" in resource:
                self.ui.channel_1.setText(resource)

    def update_radio_setting(self, valIn):
        self.radio_setting = valIn

    def send_log(self, valIn):
        self.ui.console_out.insertPlainText(valIn)
        self.ui.console_out.insertPlainText("\n")

    def on_run_button_clicked(self):
        print("Hi")
        self.volt_limit = self.ui.volt_limit.value()
        self.delay = self.ui.curr_limit.value()
        self.increment = self.ui.increment_setting.value()
        self.send_log(f"Mode: {self.radio_setting}")

        if self.radio_setting == "sweep":
            self.run_sweep()
        if self.radio_setting == "nothing":
            data_test = [[1, 2, round(random.random(), 2)], [4, 5, 6], ["test", 5]]
            headers_test = ["test", "one", "two"]
            self.update_table(headers_test, data_test)

    def run_sweep(self):
        data_test = [[1, 2, 3], [4, 5, 6], ["test", 5]]
        data_headers = ["one", "two", "three"]
        data_collected = []
        #print(str(self.ui.channel_0.text()))
        try:
            self.send_log("Intended address: USB0::0x1AB1::0x0E11::DP8C182001548::INSTR")
            self.send_log("Connected address: " + self.ui.channel_0.toPlainText())
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
            dmm.write(':FUNCtion:VOLTage:DC')
        except Exception:
            self.send_log("Failed to write to DMM")

        # Setup the power supply 0V, 200mA
        try:
            supply.write(':OUTP CH1,OFF')  # start OFF - safe :)
            supply.write(':APPL CH1,0,0.2')  # apply 0V, 0.2A
        except Exception:
            self.send_log("Failed to write to DMM")

        # Run the test
        supply.write(':OUTP CH1,ON')
        v = 0
        while v <= self.volt_limit + 0.001:  # sweep voltage up to 10V
            supply.write(':APPL CH1,' + str(v) + ',0.2')  # Set the voltage
            time.sleep(2)
            # measure the voltage
            DMMoutput = dmm.query(':MEASure:VOLTage:DC?')  # record the output of the dmm
            vMeasured = float(DMMoutput)  # exctract the numerical values and store as float
            data_collected.append([DMMoutput, vMeasured])
            v += self.volt_limit / self.increment
        # Test complete. Turn supply off and zero the setpoints
        supply.write(':OUTP CH1,OFF')
        supply.write(':APPL CH1,0,0')
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
        self.send_log("Table updated and pasted to clipboard.")




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec())
