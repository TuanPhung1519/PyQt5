import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from gui import Ui_MainWindow
from subgui import Ui_Form

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        #Khoi tao nut bam
        self.uic.button_main.clicked.connect(self.show_subwin)
        self.uic.textEdit_main.setText('Main')

    def show_subwin(self):
        self.sub1_ui = QMainWindow()
        self.uic1 = Ui_Form()
        self.uic1.setupUi(self.sub1_ui)
        self.uic1.button_sub.clicked.connect(self.close_subwin)
        self.sub1_ui.show()
        data = 'Sub1'
        self.uic1.textEdit_sub.setText(data)

    def close_subwin(self):
        self.sub1_ui.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ui = MainWindow()
    main_ui.show()
    sys.exit(app.exec_())