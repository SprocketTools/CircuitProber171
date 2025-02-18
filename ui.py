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
        font.setBold(False)
        Dialog.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 421, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.channel_0 = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget)
        self.channel_0.setObjectName("channel_0")
        self.verticalLayout.addWidget(self.channel_0)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.channel_1 = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget)
        self.channel_1.setObjectName("channel_1")
        self.verticalLayout.addWidget(self.channel_1)
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.channel_2 = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget)
        self.channel_2.setObjectName("channel_2")
        self.verticalLayout.addWidget(self.channel_2)
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.channel_3 = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget)
        self.channel_3.setObjectName("channel_3")
        self.verticalLayout.addWidget(self.channel_3)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(469, 19, 311, 561))
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
        self.run_button = QtWidgets.QPushButton(parent=Dialog)
        self.run_button.setGeometry(QtCore.QRect(20, 510, 75, 24))
        self.run_button.setObjectName("run_button")
        self.groupBox = QtWidgets.QGroupBox(parent=Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 410, 120, 80))
        self.groupBox.setObjectName("groupBox")
        self.SweepRadio = QtWidgets.QRadioButton(parent=self.groupBox)
        self.SweepRadio.setGeometry(QtCore.QRect(0, 20, 89, 16))
        self.SweepRadio.setObjectName("SweepRadio")
        self.NothingRadio = QtWidgets.QRadioButton(parent=self.groupBox)
        self.NothingRadio.setGeometry(QtCore.QRect(0, 40, 89, 20))
        self.NothingRadio.setObjectName("NothingRadio")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 260, 171, 146))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.volt_limit = QtWidgets.QDoubleSpinBox(parent=self.verticalLayoutWidget_3)
        self.volt_limit.setObjectName("volt_limit")
        self.verticalLayout_3.addWidget(self.volt_limit)
        self.label_6 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.curr_limit = QtWidgets.QDoubleSpinBox(parent=self.verticalLayoutWidget_3)
        self.curr_limit.setObjectName("curr_limit")
        self.verticalLayout_3.addWidget(self.curr_limit)
        self.label_7 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.increment_setting = QtWidgets.QDoubleSpinBox(parent=self.verticalLayoutWidget_3)
        self.increment_setting.setObjectName("increment_setting")
        self.verticalLayout_3.addWidget(self.increment_setting)
        self.console_out = QtWidgets.QTextBrowser(parent=Dialog)
        self.console_out.setGeometry(QtCore.QRect(200, 261, 256, 321))
        self.console_out.setObjectName("console_out")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CircuitProber"))
        self.label.setText(_translate("Dialog", "Channel 0 Address"))
        self.label_2.setText(_translate("Dialog", "Channel 1 Address"))
        self.label_3.setText(_translate("Dialog", "Channel 2 Address"))
        self.label_4.setText(_translate("Dialog", "Channel 3 Address"))
        self.run_button.setText(_translate("Dialog", "Run"))
        self.groupBox.setTitle(_translate("Dialog", "Mode"))
        self.SweepRadio.setText(_translate("Dialog", "Sweep"))
        self.NothingRadio.setText(_translate("Dialog", "Do Nothing"))
        self.label_5.setText(_translate("Dialog", "Voltage Limit"))
        self.label_6.setText(_translate("Dialog", "Delay"))
        self.label_7.setText(_translate("Dialog", "Increments"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
