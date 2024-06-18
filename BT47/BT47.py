import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        #Khai bao button
        self.uic.show_button.clicked.connect(self.show_edit)
        self.uic.hide_button.clicked.connect(self.hide_edit)

    def show_edit(self):
        self.uic.textEdit.show()
    def hide_edit(self):
        self.uic.textEdit.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ui = MainWindow()
    main_ui.show()
    sys.exit(app.exec_())