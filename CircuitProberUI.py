# Form implementation generated from reading ui file 'CircuitProber.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        Dialog.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 491, 114))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.channel_0 = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget)
        self.channel_0.setMaximumSize(QtCore.QSize(16777215, 29))
        self.channel_0.setObjectName("channel_0")
        self.verticalLayout.addWidget(self.channel_0)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.channel_1 = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget)
        self.channel_1.setMaximumSize(QtCore.QSize(16777215, 29))
        self.channel_1.setObjectName("channel_1")
        self.verticalLayout.addWidget(self.channel_1)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(529, 19, 251, 561))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.verticalLayoutWidget_2)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(50, 165, 201, 271))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.volt_limit = QtWidgets.QDoubleSpinBox(parent=self.verticalLayoutWidget_3)
        self.volt_limit.setDecimals(3)
        self.volt_limit.setProperty("value", 12.0)
        self.volt_limit.setObjectName("volt_limit")
        self.verticalLayout_3.addWidget(self.volt_limit)
        self.label_6 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.curr_limit = QtWidgets.QDoubleSpinBox(parent=self.verticalLayoutWidget_3)
        self.curr_limit.setDecimals(1)
        self.curr_limit.setProperty("value", 2.0)
        self.curr_limit.setObjectName("curr_limit")
        self.verticalLayout_3.addWidget(self.curr_limit)
        self.label_7 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.increment_setting = QtWidgets.QDoubleSpinBox(parent=self.verticalLayoutWidget_3)
        self.increment_setting.setDecimals(0)
        self.increment_setting.setMaximum(250.0)
        self.increment_setting.setProperty("value", 12.0)
        self.increment_setting.setObjectName("increment_setting")
        self.verticalLayout_3.addWidget(self.increment_setting)
        self.setting_group = QtWidgets.QGroupBox(parent=self.verticalLayoutWidget_3)
        self.setting_group.setMinimumSize(QtCore.QSize(0, 100))
        self.setting_group.setBaseSize(QtCore.QSize(0, 300))
        self.setting_group.setObjectName("setting_group")
        self.voltage_radio = QtWidgets.QRadioButton(parent=self.setting_group)
        self.voltage_radio.setGeometry(QtCore.QRect(0, 20, 111, 21))
        self.voltage_radio.setObjectName("voltage_radio")
        self.nothing_radio = QtWidgets.QRadioButton(parent=self.setting_group)
        self.nothing_radio.setGeometry(QtCore.QRect(0, 60, 111, 21))
        self.nothing_radio.setObjectName("nothing_radio")
        self.current_radio = QtWidgets.QRadioButton(parent=self.setting_group)
        self.current_radio.setGeometry(QtCore.QRect(0, 40, 111, 21))
        self.current_radio.setObjectName("current_radio")
        self.verticalLayout_3.addWidget(self.setting_group)
        self.console_out = QtWidgets.QTextBrowser(parent=Dialog)
        self.console_out.setGeometry(QtCore.QRect(280, 160, 221, 421))
        self.console_out.setObjectName("console_out")
        self.run_button = QtWidgets.QPushButton(parent=Dialog)
        self.run_button.setGeometry(QtCore.QRect(100, 460, 91, 24))
        self.run_button.setObjectName("run_button")
        self.copy_button = QtWidgets.QPushButton(parent=Dialog)
        self.copy_button.setGeometry(QtCore.QRect(100, 490, 91, 24))
        self.copy_button.setObjectName("copy_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CircuitProber"))
        self.label.setText(_translate("Dialog", "Power Supply Address"))
        self.label_2.setText(_translate("Dialog", "Multimeter Address"))
        self.label_5.setText(_translate("Dialog", "Final voltage"))
        self.label_6.setText(_translate("Dialog", "Delay between measurements"))
        self.label_7.setText(_translate("Dialog", "Amount of data points"))
        self.setting_group.setTitle(_translate("Dialog", "Mode"))
        self.voltage_radio.setText(_translate("Dialog", "Voltage Sweep"))
        self.nothing_radio.setText(_translate("Dialog", "Panel Test"))
        self.current_radio.setText(_translate("Dialog", "Current Sweep"))
        self.run_button.setText(_translate("Dialog", "Run"))
        self.copy_button.setText(_translate("Dialog", "Copy Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
