import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Qtui import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_ui = QMainWindow()
        self.main_uic = Ui_MainWindow()
        self.main_uic.setupUi(self.main_ui)
        #Khoi tao cac nut action
        self.main_uic.actionAction1.triggered.connect(self.show1)
        self.main_uic.actionAction2.triggered.connect(self.show2)
        self.main_uic.actionAction3.triggered.connect(self.show3)
        self.main_uic.actionShow.triggered.connect(self.show_copy)

    def show1(self):
        self.main_uic.tabWidget.setCurrentWidget(self.main_uic.tab)
    def show2(self):
        self.main_uic.tabWidget.setCurrentWidget(self.main_uic.tab_2)
    def show3(self):
        self.main_uic.tabWidget.setCurrentWidget(self.main_uic.tab_3)

    def show_copy(self):
        self.main_uic.textBrowser.setText('Hello!')
    def show(self):
        self.main_ui.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())