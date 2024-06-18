import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from gui import Ui_MainWindow
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        #Khai bao nut an
        self.uic.cancel_button.clicked.connect(self.close)
        self.uic.login_button.clicked.connect(self.pass_login)
        self.uic.logout_button.clicked.connect(self.logout)

    def pass_login(self):
        ID = self.uic.line_id.text()
        Pass = self.uic.line_pass.text()
        self.uic.textEdit.setText("AAA")
        if ID == 'tuan' and Pass == 'tuan':
            self.uic.stackedWidget.setCurrentWidget(self.uic.page_2)
        elif ID != 'tuan':
            QMessageBox.information(self, 'Error', 'Your ID is wrong!')
        elif Pass != 'tuan':
            QMessageBox.information(self, 'Error', 'Your Pass is wrong!')
        else:
            QMessageBox.information(self, 'Error', 'Your ID or Pass is wrong!')
    #Su dung nut enter de dang nhap => Vi su dung ham event nut bam => can truyen tham so event => khi an enter can kien tra pass, id dung chua?
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.pass_login()

    def logout(self):#Khi an nut logout se quay lai man hinh 1
        self.uic.stackedWidget.setCurrentWidget(self.uic.page)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ui = MainWindow()
    main_ui.show()
    sys.exit(app.exec_())