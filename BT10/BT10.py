import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from GUI_main import Ui_MainWindow
from sub_GUI import Ui_Form
from PyQt5 import QtWidgets

class MainWindow:
    def __init__(self):
        #Khai bao thuoc tinh de khoi tao window chinh
        self.main_ui = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_ui)
        #Khai bao nut nhan mo cua so moi
        self.uic.showtext_button.clicked.connect(self.subwindow)

    def subwindow(self):
        self.sub_ui = QtWidgets.QMainWindow()
        self.sub_uic = Ui_Form()
        self.sub_uic.setupUi(self.sub_ui)
        self.sub_ui.show()
        #LAy mess tu textedit
        mess = self.uic.textEdit.toPlainText()
        self.sub_uic.textBrowser.setText(mess)

    def show(self):
        self.main_ui.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ui = MainWindow()
    main_ui.show()
    sys.exit(app.exec_())
