import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from gui import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal, QThread
import time
from random import randint


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        #Khoi tao nut bam
        self.uic.start_button.clicked.connect(self.start_thread)
        self.uic.stop_button.clicked.connect(self.stop_thread)
        #Khoi tao bien luu so luong khi khong co gia tri dien vao lineEdit
        self.number_thread = 0
        #Khoi tao bien quan ly thread
        self.thread = {}
        #Setup do rong cot
        self.uic.tableWidget.setColumnWidth(0, 100)
        self.uic.tableWidget.setColumnWidth(0, 150)
        self.uic.tableWidget.setColumnWidth(0, 170)

    def start_thread(self):
        self.number_thread = int(self.uic.lineEdit.text())
        for i in range(self.number_thread):
            self.thread[i] = Thread_Class(index=i)
            self.thread[i].signal.connect(self.receive_data)
            self.thread[i].signal_indexthread.connect(self.receive_index)
            self.thread[i].start()

    def receive_data(self, data):
        #Thiet lap so luong hang tuy vao thread
        self.uic.tableWidget.setRowCount(self.number_thread)
        self.uic.tableWidget.setItem(data[2], 0, QTableWidgetItem(str(data[0])))
        self.uic.tableWidget.setItem(data[2], 1, QTableWidgetItem(data[1]))
        self.uic.tableWidget.setItem(data[2], 2, QTableWidgetItem("Thread: " + str(data[2])))

    def receive_index(self, index):
        i = index
        self.thread[i] = Thread_Class(index=i)
        self.thread[i].signal.connect(self.receive_data)
        self.thread[i].start()
        self.thread[i].signal_indexthread.connect(self.receive_index)

    def stop_thread(self):
        self.number_thread = int(self.uic.lineEdit.text())
        for i in range(self.number_thread):
            self.thread[i].stop()


class Thread_Class(QThread):
    signal = pyqtSignal(object)
    signal_indexthread = pyqtSignal(object)
    def __init__(self, index=0):
        super().__init__()
        self.index = index
        print("Start Thread ", self.index)
        #Khoi tao bien truyen len bang va truyen khoi tao lai tung thread
        self.data1 = []

    def run(self):
        self.status = "start"
        # Ta can bien moi thread co gia tri dem ban dau khac nhau
        self.init_count = randint(0, 5)
        for self.init_count in range(self.init_count, 10):
            self.data1 = [self.init_count, self.status, self.index]
            self.signal.emit(self.data1)
            time.sleep(1)
        self.status = "stop"
        self.data1 = [self.init_count, self.status, self.index]
        self.signal.emit(self.data1)
        self.signal_indexthread.emit(self.index)

    def stop(self):
        print("Stop Thread ", self.index)
        self.status = "stop"
        self.data1 = [self.init_count, self.status, self.index]
        self.signal.emit(self.data1)
        self.terminate()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ui = MainWindow()
    main_ui.show()
    sys.exit(app.exec_())