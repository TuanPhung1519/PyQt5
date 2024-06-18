import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI_button import Ui_MainWindow
from PyQt5.QtGui import QPixmap

class MainWindow:
    def __init__(self):
        self.main_ui = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_ui)
        #Khoi tao nut nhan pushbutton
        self.uic.pushButton.clicked.connect(self.onoff)

    def onoff(self):
        if (self.uic.pushButton.text() == 'OFF'):
            self.uic.pushButton.setText('ON')
            self.uic.label.setPixmap(QPixmap("data/green.png"))
        else:
            self.uic.pushButton.setText('OFF')
            self.uic.label.setPixmap(QPixmap("data/red.png"))
    def show(self):
        self.main_ui.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_ui = MainWindow()
    main_ui.show()
    sys.exit(app.exec_())