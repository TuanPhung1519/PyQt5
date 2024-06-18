import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QFontDialog, QColorDialog
from gui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        #Khai bao thanh taskbar
        self.uic.actionFonts.triggered.connect(self.changFonts)
        self.uic.actionColors.triggered.connect(self.changeColors_background)
        self.uic.textEdit.setText('Hello!')
    def changFonts(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.uic.textEdit.setFont(font)

    def changeColors_background(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.uic.textEdit.setStyleSheet("background-color:" + color.name())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ui = MainWindow()
    main_ui.show()
    sys.exit(app.exec_())