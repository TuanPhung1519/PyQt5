import sys
import time

from PyQt5.QtWidgets import QMainWindow, QApplication
from gui import Ui_MainWindow

from PyQt5.QtCore import pyqtSignal, QThread
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        #Khai bao cac nut
        self.uic.start1_button.clicked.connect(self.start1_work)
        self.uic.stop1_button.clicked.connect(self.stop1_work)
        self.uic.start2_button.clicked.connect(self.start2_work)
        self.uic.stop2_button.clicked.connect(self.stop2_work)
        #Khai bao bien quan ly cac thread
        self.thread = {}
    def start1_work(self):
        self.thread[1] = ThreadClass_1(index=1)
        self.thread[1].signal_1.connect(self.function_1)
        self.thread[1].start()
        self.uic.start1_button.setEnabled(False)
        self.uic.stop1_button.setEnabled(True)
    def start2_work(self):
        self.thread[2] = ThreadClass_2(index=2)
        self.thread[2].signal_2.connect(self.function_2)
        self.thread[2].start()
        self.uic.start2_button.setEnabled(False)
        self.uic.stop2_button.setEnabled(True)

    def stop1_work(self):
        self.uic.start1_button.setEnabled(True)
        self.uic.stop1_button.setEnabled(False)
        self.uic.lcdNumber.display(0)
        self.thread[1].stop()
    def stop2_work(self):
        self.uic.start2_button.setEnabled(True)
        self.uic.stop2_button.setEnabled(False)
        self.uic.lcdNumber_2.display(0)
        self.thread[2].stop()
    def function_1(self, counter_1):
        m = counter_1
        self.uic.lcdNumber.display(m)
    def function_2(self, counter_2):
        m = counter_2
        self.uic.lcdNumber_2.display(m)


class ThreadClass_1(QThread):
    signal_1 = pyqtSignal(int)
    def __init__(self, index=0):
        super().__init__()
        self.index = index
    def run(self):
        counter_1 = 0
        print("Start Thread ", self.index)
        while True:
            counter_1 += 1
            time.sleep(0.1)
            self.signal_1.emit(counter_1)
            if counter_1 == 10:
                counter_1 = 0
    def stop(self):
        print("Stop Thread ", self.index)
        self.terminate()

class ThreadClass_2(QThread):
    signal_2 = pyqtSignal(int)
    def __init__(self, index=0):
        super().__init__()
        self.index = index
    def run(self):
        counter_2 = 0
        print("Start Thread ", self.index)
        while True:
            counter_2 += 1
            time.sleep(0.01)
            self.signal_2.emit(counter_2)
            if counter_2 == 100:
                counter_2 = 0

    def stop(self):
        print("Stop Thread ", self.index)
        self.terminate()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ui = MainWindow()
    main_ui.show()
    sys.exit(app.exec_())
