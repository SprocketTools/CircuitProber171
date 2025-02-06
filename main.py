import random
import sys
from PyQt6 import QtWidgets, uic, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDockWidget, QFormLayout, QLineEdit, QWidget, QPushButton, QSpinBox, QMessageBox, QToolBar, QMessageBox
from PyQt6.QtCore import QTimer, Qt
import CircuitProberUI
class Dialog(QtWidgets.QDialog):
    def __init__(self):
        self.i = 0
        super().__init__()
        self.ui = CircuitProberUI.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.run_button.clicked.connect(self.on_run_button_clicked)


    def on_run_button_clicked(self):
        print("Button clicked!")
        print(self.i)
        self.i = self.i + 1
        self.table = QtWidgets.QTableView()
        data = [
            [4, 9, 2],
            [1, 0, 0],
            [3, 5, 0],
            [3, 3, 2],
            [7, 8, 9],
        ]

        self.ui.tableWidget.clear()
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setHorizontalHeaderLabels(["trigger", "voltage", "current"])
        i = 0
        while i < 5:
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)
            self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount())

            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 0, QTableWidgetItem(str(self.ui.tableWidget.rowCount())))
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 1, QTableWidgetItem(str(round(random.random()*500))))
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 2, QTableWidgetItem(str(round(random.random() * 500))))
            i+= 1




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec())
