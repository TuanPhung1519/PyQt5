import sys
import time

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from gui import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal, QThread

from random import randint


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        #Khoi tao nut bam
        self.uic.start_button.clicked.connect(self.start_thread)
        self.uic.stop_button.clicked.connect(self.stop_thread)
        #Khoi tao quan ly thread
        self.thread = {}
        #Khi chua dien gia tri khoi tao so thread
        self.numThread = 0

    def start_thread(self):
        self.numThread = int(self.uic.lineEdit.text())
        for i in range(self.numThread):
            self.thread[i] = Thread_Class(index = i)
            self.thread[i].signal.connect(self.receive_data)
            self.thread[i].start()

    def receive_data(self, data):
        self.uic.tableWidget.setRowCount(self.numThread)
        self.uic.tableWidget.setItem(data[2], 0, QTableWidgetItem(str(data[0])))
        self.uic.tableWidget.setItem(data[2], 1, QTableWidgetItem(data[1]))
        self.uic.tableWidget.setItem(data[2], 2, QTableWidgetItem("Thread " + str(data[2])))

    def stop_thread(self):
        self.numThread = int(self.uic.lineEdit.text())
        for i in range(self.numThread):
            self.thread[i].stop()

class Thread_Class(QThread):
    signal = pyqtSignal(object)
    def __init__(self, index=0):
        super().__init__()
        self.index = index
    def run(self):
        print("Start Thread ", self.index)
        #Ta cho random diem bat dau dem khac nhau cua moi thread
        self.random_initcount = randint(0,5)
        #Ta se truyen 1 tap cac data de dien vao table gom: count, status, thread
        self.status = "start"
        for self.i in range(self.random_initcount, 50):
            time.sleep(0.2)
            data = [self.i, self.status, self.index]
            self.signal.emit(data)

        self.status = "stop"
        data = [self.i, self.status, self.index]
        self.signal.emit(data)
    def stop(self):
        print("Stop Thread ", self.index)
        self.status = "stop"
        data = [self.i, self.status, self.index]
        self.signal.emit(data)
        self.terminate()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ui = MainWindow()
    main_ui.show()
    sys.exit(app.exec_())