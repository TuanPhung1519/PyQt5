# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(60, 30, 681, 371))
        self.stackedWidget.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.Panel)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.stackedWidget.setLineWidth(3)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.textEdit = QtWidgets.QTextEdit(self.page_2)
        self.textEdit.setGeometry(QtCore.QRect(40, 60, 191, 101))
        self.textEdit.setObjectName("textEdit")
        self.show_button = QtWidgets.QPushButton(self.page_2)
        self.show_button.setGeometry(QtCore.QRect(410, 90, 75, 23))
        self.show_button.setObjectName("show_button")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label = QtWidgets.QLabel(self.page_3)
        self.label.setGeometry(QtCore.QRect(60, 40, 611, 311))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("data/1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.page_3)
        self.s1 = QtWidgets.QPushButton(self.centralwidget)
        self.s1.setGeometry(QtCore.QRect(60, 430, 121, 61))
        self.s1.setObjectName("s1")
        self.s2 = QtWidgets.QPushButton(self.centralwidget)
        self.s2.setGeometry(QtCore.QRect(340, 430, 121, 61))
        self.s2.setObjectName("s2")
        self.s3 = QtWidgets.QPushButton(self.centralwidget)
        self.s3.setGeometry(QtCore.QRect(620, 430, 121, 61))
        self.s3.setObjectName("s3")
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
        self.show_button.setText(_translate("MainWindow", "show"))
        self.s1.setText(_translate("MainWindow", "1"))
        self.s2.setText(_translate("MainWindow", "2"))
        self.s3.setText(_translate("MainWindow", "3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())