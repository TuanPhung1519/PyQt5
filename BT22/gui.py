# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 281)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start1_button = QtWidgets.QPushButton(self.centralwidget)
        self.start1_button.setGeometry(QtCore.QRect(10, 10, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.start1_button.setFont(font)
        self.start1_button.setObjectName("start1_button")
        self.start2_button = QtWidgets.QPushButton(self.centralwidget)
        self.start2_button.setGeometry(QtCore.QRect(10, 120, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.start2_button.setFont(font)
        self.start2_button.setObjectName("start2_button")
        self.stop1_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop1_button.setGeometry(QtCore.QRect(260, 10, 251, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.stop1_button.setFont(font)
        self.stop1_button.setObjectName("stop1_button")
        self.stop2_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop2_button.setGeometry(QtCore.QRect(260, 120, 251, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.stop2_button.setFont(font)
        self.stop2_button.setObjectName("stop2_button")
        self.lcdNumber_1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_1.setGeometry(QtCore.QRect(520, 10, 271, 101))
        self.lcdNumber_1.setObjectName("lcdNumber_1")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(520, 120, 271, 101))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start1_button.setText(_translate("MainWindow", "START 1"))
        self.start2_button.setText(_translate("MainWindow", "START 2"))
        self.stop1_button.setText(_translate("MainWindow", "STOP 1"))
        self.stop2_button.setText(_translate("MainWindow", "STOP 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())