import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI_main import Ui_MainWindow
from subGUI import Ui_Form
from PyQt5 import QtWidgets

class MainWindow:
    def __init__(self):
        self.main_ui = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_ui)
        #Khoi tao nut nhan settings
        self.uic.setting_button.clicked.connect(self.show_subGUI)

    def show(self):
        self.main_ui.show()

    def show_subGUI(self):
        #Vi sd Widget => sd QtWidget de open subGUI
        #Sau do khoi tao giong het GUI main
        self.second_ui = QtWidgets.QMainWindow()
        self.second_uic = Ui_Form()
        self.second_uic.setupUi(self.second_ui)
        #Vi main win co ham show nen can ham show de hien thi trong sub win
        self.second_ui.show()
        #Khoi tao nut nhan show text trong subgui
        self.second_uic.show_button.clicked.connect(self.show_text)
    def show_text(self):
        self.second_uic.textBrowser.setText('Hello!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

