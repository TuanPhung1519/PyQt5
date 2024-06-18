import sys
import time

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from gui import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal, QThread
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #Khoi tao gia tri ban dau
        self.data = 0
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        #Khoi tao nut bam, vi sd while => se sd thread cho while
        self.uic.pushButton.clicked.connect(self.start_thread)
        #Khoi tao bien quan ly thread
        self.thread = {}
    def start_thread(self):
        self.thread[1] = Thread_Class(index = 1)
        self.thread[1].signal.connect(self.update_show)
        self.thread[1].start()

    def update_show(self, data):
        self.uic.tableWidget.setItem(1,1,QTableWidgetItem(str(data)))
        self.uic.lineEdit.setText(str(data))

class Thread_Class(QThread):
    signal = pyqtSignal(int)
    def __init__(self, index=0):
        super().__init__()
        self.index = index
        print("Start Thread ", self.index)
        self.data = 0
    def run(self):
        self.data = 0
        while True:
            self.data += 1
            self.signal.emit(self.data)
            time.sleep(1)
            if self.data == 5:
                break




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ui = MainWindow()
    main_ui.show()
    sys.exit(app.exec_())