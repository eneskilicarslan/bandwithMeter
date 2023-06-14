import threading

from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import time


class Ui_Frame(object):
    def __init__(self):
        self.process = None
        self.thread = None

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(804, 272)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setObjectName("formLayout")
        self.timeRadio = QtWidgets.QRadioButton(Frame)
        self.timeRadio.setChecked(True)
        self.timeRadio.setObjectName("timeRadio")
        self.buttonGroup = QtWidgets.QButtonGroup(Frame)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.timeRadio)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.timeRadio)
        self.time = QtWidgets.QSpinBox(Frame)
        self.time.setMaximumSize(QtCore.QSize(90, 16777215))
        self.time.setMaximum(999999)
        self.time.setProperty("value", 10)
        self.time.setObjectName("time")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.time)
        self.dataRadio = QtWidgets.QRadioButton(Frame)
        self.dataRadio.setObjectName("dataRadio")
        self.buttonGroup.addButton(self.dataRadio)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.dataRadio)
        self.data = QtWidgets.QSpinBox(Frame)
        self.data.setMaximumSize(QtCore.QSize(90, 16777215))
        self.data.setObjectName("data")
        self.data.setMaximum(999999999)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.data)
        self.clientRadio = QtWidgets.QRadioButton(Frame)
        self.clientRadio.setChecked(True)
        self.clientRadio.setObjectName("clientRadio")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(Frame)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.clientRadio)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.clientRadio)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.senderIpText = QtWidgets.QLineEdit(Frame)
        self.senderIpText.setMaximumSize(QtCore.QSize(120, 16777215))
        self.senderIpText.setObjectName("senderIpText")
        self.horizontalLayout_2.addWidget(self.senderIpText)
        self.senderPortText = QtWidgets.QLineEdit(Frame)
        self.senderPortText.setMaximumSize(QtCore.QSize(50, 16777215))
        self.senderPortText.setObjectName("senderPortText")
        self.horizontalLayout_2.addWidget(self.senderPortText)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.serverRadio = QtWidgets.QRadioButton(Frame)
        self.serverRadio.setObjectName("serverRadio")
        self.buttonGroup_2.addButton(self.serverRadio)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.serverRadio)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.rcvrPortText = QtWidgets.QLineEdit(Frame)
        self.rcvrPortText.setMaximumSize(QtCore.QSize(50, 16777215))
        self.rcvrPortText.setObjectName("rcvrPortText")
        self.horizontalLayout_4.addWidget(self.rcvrPortText)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.tcpConf = QtWidgets.QRadioButton(Frame)
        self.tcpConf.setChecked(True)
        self.tcpConf.setObjectName("tcpConf")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(Frame)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.tcpConf)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.tcpConf)
        self.udpConf = QtWidgets.QRadioButton(Frame)
        self.udpConf.setObjectName("udpConf")
        self.buttonGroup_3.addButton(self.udpConf)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.udpConf)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.udpBandwith = QtWidgets.QSpinBox(Frame)
        self.udpBandwith.setMaximumSize(QtCore.QSize(90, 16777215))
        self.udpBandwith.setMaximum(999999)
        self.udpBandwith.setObjectName("udpBandwith")
        self.horizontalLayout_5.addWidget(self.udpBandwith)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.horizontalLayout_3.addLayout(self.formLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.startButton = QtWidgets.QPushButton(Frame)
        self.startButton.setMinimumSize(QtCore.QSize(120, 30))
        self.startButton.setMaximumSize(QtCore.QSize(168777, 16777215))
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)
        self.stopButton = QtWidgets.QPushButton(Frame)
        self.stopButton.setMinimumSize(QtCore.QSize(120, 30))
        self.stopButton.setMaximumSize(QtCore.QSize(168777, 16777215))
        self.stopButton.setObjectName("stopButton")
        self.verticalLayout.addWidget(self.stopButton)
        self.resultText = QtWidgets.QTextEdit(Frame)
        self.resultText.setObjectName("resultText")
        self.verticalLayout.addWidget(self.resultText)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)

    def start(self):
        if self.timeRadio.isChecked():
            transmit = " -t "
            transmitData = self.time.text()
        else:
            transmit = " -n "
            transmitData = self.data.text()

        if self.clientRadio.isChecked():
            if self.tcpConf.isChecked():
                command = "iperf.exe -c " + self.senderIpText.text() + " -P 1 -i 1 -p " + self.senderPortText.text() + " -f m" + transmit + transmitData
            else:
                command = "iperf.exe -c " + self.senderIpText.text() + " -u -P 1 -i 1 -p " + self.senderPortText.text() + " -b " + self.udpBandwith.text() + ".0M -f m " + transmit + transmitData + " -T 1"
        else:
            if self.tcpConf.isChecked():
                command = "iperf.exe -s -P 0 -i 1 -p " + self.rcvrPortText.text() + " -f m"
            else:
                command = "iperf.exe -s -u -P 0 -i 1 -p " + self.rcvrPortText.text() + " -f m"
        # command = "ping google.com"
        self.thread = threading.Thread(target=self.run_command, args=(command,))
        self.thread.start()

    def stop(self):
        if self.process:
            self.process.kill()
            self.process = None
            self.thread.join()
            self.resultText.append("Process killed")
        else:
            self.resultText.append("No process to be killed")

    def run_command(self, command):
        try:
            print(command)
            self.process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            while True:
                output = self.process.stdout.readline()

                if not output:
                    break
                else:
                    self.resultText.append(output.rstrip().decode("windows-1254"))

                time.sleep(0.1)

            self.resultText.append("Done forcing the band: " + str(self.process.returncode))
        except Exception as e:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            msgBox.setText("Error: " + str(e))
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            msgBox.setDefaultButton(QtWidgets.QMessageBox.Ok)

            returnValue = msgBox.exec()

            print("Error: ", e)
            return

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Ağ Band Genişliği Test Aracı"))
        self.timeRadio.setText(_translate("Frame", "Süre (Saniye)"))
        self.dataRadio.setText(_translate("Frame", "Veri (Bytes)"))
        self.clientRadio.setText(_translate("Frame", "İstemci"))
        self.senderIpText.setPlaceholderText(_translate("Frame", "IP"))
        self.senderPortText.setPlaceholderText(_translate("Frame", "port"))
        self.serverRadio.setText(_translate("Frame", "Sunucu"))
        self.rcvrPortText.setPlaceholderText(_translate("Frame", "port"))
        self.tcpConf.setText(_translate("Frame", "TCP"))
        self.udpConf.setText(_translate("Frame", "UDP"))
        self.label.setText(_translate("Frame", "UDP Bandwith(MBits/sec)"))
        self.startButton.setText(_translate("Frame", "START"))
        self.stopButton.setText(_translate("Frame", "STOP"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
