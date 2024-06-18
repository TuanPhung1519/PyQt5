import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI_main import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_ui = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_ui)
        self.uic.login_button.clicked.connect(self.loging)
    def loging(self):
        if self.uic.lineEdit.text() != '' and self.uic.lineEdit_2.text() != '':
            if self.uic.lineEdit.text() == 'tuan' and self.uic.lineEdit_2.text() == 'tuan':
                self.uic.label_2.setText('Pass!')
            else:
                self.uic.label_2.setText('Error!')
    def show(self):
        self.main_ui.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ui = MainWindow()
    main_ui.show()
    sys.exit(app.exec_())