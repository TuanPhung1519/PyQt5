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
        MainWindow.resize(752, 786)
        MainWindow.setMinimumSize(QtCore.QSize(745, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 731, 751))
        self.stackedWidget.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.textEdit = QtWidgets.QTextEdit(self.page_2)
        self.textEdit.setGeometry(QtCore.QRect(110, 60, 521, 481))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.logout_button = QtWidgets.QPushButton(self.page_2)
        self.logout_button.setGeometry(QtCore.QRect(290, 580, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.logout_button.setFont(font)
        self.logout_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.logout_button.setObjectName("logout_button")
        self.stackedWidget.addWidget(self.page_2)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayoutWidget = QtWidgets.QWidget(self.page)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(170, 120, 421, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.line_id = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.line_id.setFont(font)
        self.line_id.setObjectName("line_id")
        self.gridLayout.addWidget(self.line_id, 1, 0, 1, 1)
        self.line_pass = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.line_pass.setFont(font)
        self.line_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_pass.setObjectName("line_pass")
        self.gridLayout.addWidget(self.line_pass, 2, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.page)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(280, 470, 171, 161))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.login_button = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.login_button.setObjectName("login_button")
        self.gridLayout_3.addWidget(self.login_button, 0, 0, 1, 1)
        self.cancel_button = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cancel_button.setFont(font)
        self.cancel_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout_3.addWidget(self.cancel_button, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logout_button.setText(_translate("MainWindow", "logout"))
        self.line_id.setPlaceholderText(_translate("MainWindow", "ID"))
        self.line_pass.setPlaceholderText(_translate("MainWindow", "Password"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
