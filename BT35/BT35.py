import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from gui import Ui_MainWindow
from subgui import Ui_Form

class subMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.uic_sub = Ui_Form()
        self.uic_sub.setupUi(self)
        #Khai bao button
        self.uic_sub.ok_button.clicked.connect(self.ok_subui)

    def ok_subui(self):
        #2. Send data through index
        data = 'AAA'
        a = MainWindow()
        a.receidata(index=data)
        self.close()

    def closeEvent(self, event):
        print('Not send value!')





#Class for Main UI
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        #Khoi tao nut bam vao sub win
        self.uic.sub_button.clicked.connect(self.senddatamain)
    def senddatamain(self):
        self.subui = subMainWindow()
        #1. Truyen data hien thi tu main->sub sd settext van duoc
        datamain = self.uic.textEdit_main.toPlainText()
        self.subui.uic_sub.textEdit_sub.setText(datamain)
        self.subui.show()

    def receidata(self, index=0):
        datarecei = index
        print(datarecei)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ui = MainWindow()
    main_ui.show()
    sys.exit(app.exec_())