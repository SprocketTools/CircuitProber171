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
        Dialog.resize(800, 550)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        Dialog.setFont(font)
        Dialog.setStyleSheet("\n"
"font: 10pt \"Tahoma\"")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(230, 20, 551, 66))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.verticalLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.channel_0 = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget)
        self.channel_0.setMaximumSize(QtCore.QSize(16777215, 29))
        self.channel_0.setObjectName("channel_0")
        self.gridLayout.addWidget(self.channel_0, 0, 1, 1, 1)
        self.channel_1 = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget)
        self.channel_1.setMaximumSize(QtCore.QSize(16777215, 29))
        self.channel_1.setObjectName("channel_1")
        self.gridLayout.addWidget(self.channel_1, 3, 1, 1, 1)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(529, 109, 251, 421))
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
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 20, 193, 474))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.volt_limit = QtWidgets.QDoubleSpinBox(parent=self.verticalLayoutWidget_3)
        self.volt_limit.setDecimals(2)
        self.volt_limit.setMaximum(30.0)
        self.volt_limit.setProperty("value", 12.0)
        self.volt_limit.setObjectName("volt_limit")
        self.verticalLayout_3.addWidget(self.volt_limit)
        self.label_8 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.volt_limit_2 = QtWidgets.QDoubleSpinBox(parent=self.verticalLayoutWidget_3)
        self.volt_limit_2.setDecimals(2)
        self.volt_limit_2.setMaximum(30.0)
        self.volt_limit_2.setProperty("value", 12.0)
        self.volt_limit_2.setObjectName("volt_limit_2")
        self.verticalLayout_3.addWidget(self.volt_limit_2)
        self.label_9 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.volt_limit_3 = QtWidgets.QDoubleSpinBox(parent=self.verticalLayoutWidget_3)
        self.volt_limit_3.setDecimals(2)
        self.volt_limit_3.setMaximum(5.0)
        self.volt_limit_3.setSingleStep(0.5)
        self.volt_limit_3.setProperty("value", 5.0)
        self.volt_limit_3.setObjectName("volt_limit_3")
        self.verticalLayout_3.addWidget(self.volt_limit_3)
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
        self.channel_group = QtWidgets.QGroupBox(parent=self.verticalLayoutWidget_3)
        self.channel_group.setMinimumSize(QtCore.QSize(0, 115))
        self.channel_group.setBaseSize(QtCore.QSize(0, 300))
        self.channel_group.setObjectName("channel_group")
        self.channel_2_radio = QtWidgets.QRadioButton(parent=self.channel_group)
        self.channel_2_radio.setGeometry(QtCore.QRect(0, 40, 191, 21))
        self.channel_2_radio.setObjectName("channel_2_radio")
        self.channel_1_radio = QtWidgets.QRadioButton(parent=self.channel_group)
        self.channel_1_radio.setGeometry(QtCore.QRect(0, 20, 191, 21))
        self.channel_1_radio.setObjectName("channel_1_radio")
        self.channel_3_radio = QtWidgets.QRadioButton(parent=self.channel_group)
        self.channel_3_radio.setGeometry(QtCore.QRect(0, 60, 191, 21))
        self.channel_3_radio.setObjectName("channel_3_radio")
        self.channel_0_radio = QtWidgets.QRadioButton(parent=self.channel_group)
        self.channel_0_radio.setGeometry(QtCore.QRect(0, 80, 191, 21))
        self.channel_0_radio.setObjectName("channel_0_radio")
        self.verticalLayout_3.addWidget(self.channel_group)
        self.setting_group = QtWidgets.QGroupBox(parent=self.verticalLayoutWidget_3)
        self.setting_group.setMinimumSize(QtCore.QSize(0, 85))
        self.setting_group.setBaseSize(QtCore.QSize(0, 300))
        self.setting_group.setObjectName("setting_group")
        self.voltage_radio = QtWidgets.QRadioButton(parent=self.setting_group)
        self.voltage_radio.setGeometry(QtCore.QRect(0, 20, 191, 21))
        self.voltage_radio.setObjectName("voltage_radio")
        self.current_radio = QtWidgets.QRadioButton(parent=self.setting_group)
        self.current_radio.setGeometry(QtCore.QRect(0, 40, 191, 21))
        self.current_radio.setObjectName("current_radio")
        self.resistance_radio = QtWidgets.QRadioButton(parent=self.setting_group)
        self.resistance_radio.setGeometry(QtCore.QRect(0, 60, 191, 21))
        self.resistance_radio.setObjectName("resistance_radio")
        self.verticalLayout_3.addWidget(self.setting_group)
        self.psuRecord = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_3)
        self.psuRecord.setObjectName("psuRecord")
        self.verticalLayout_3.addWidget(self.psuRecord)
        self.console_out = QtWidgets.QTextBrowser(parent=Dialog)
        self.console_out.setGeometry(QtCore.QRect(230, 110, 271, 421))
        self.console_out.setObjectName("console_out")
        self.run_button = QtWidgets.QPushButton(parent=Dialog)
        self.run_button.setGeometry(QtCore.QRect(20, 510, 91, 24))
        self.run_button.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));\n"
"\n"
"background-color: rgb(255, 240, 240);")
        self.run_button.setObjectName("run_button")
        self.copy_button = QtWidgets.QPushButton(parent=Dialog)
        self.copy_button.setGeometry(QtCore.QRect(120, 510, 91, 24))
        self.copy_button.setObjectName("copy_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CircuitProber"))
        self.label.setText(_translate("Dialog", "Power Supply Address"))
        self.label_2.setText(_translate("Dialog", "Multimeter Address"))
        self.label_5.setText(_translate("Dialog", "PSU voltage (Ch. 1)"))
        self.label_8.setText(_translate("Dialog", "PSU voltage (Ch. 2)"))
        self.label_9.setText(_translate("Dialog", "PSU voltage (Ch. 3)"))
        self.label_6.setText(_translate("Dialog", "Measurement length"))
        self.label_7.setText(_translate("Dialog", "Amount of sweep data points"))
        self.channel_group.setTitle(_translate("Dialog", "Sweep Channel"))
        self.channel_2_radio.setText(_translate("Dialog", "Channel 2"))
        self.channel_1_radio.setText(_translate("Dialog", "Channel 1"))
        self.channel_3_radio.setText(_translate("Dialog", "Channel 3"))
        self.channel_0_radio.setText(_translate("Dialog", "Don\'t sweep any channels"))
        self.setting_group.setTitle(_translate("Dialog", "Operation Mode"))
        self.voltage_radio.setText(_translate("Dialog", "Voltage"))
        self.current_radio.setText(_translate("Dialog", "Current"))
        self.resistance_radio.setText(_translate("Dialog", "Resistance"))
        self.psuRecord.setText(_translate("Dialog", "Record PSU data"))
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
