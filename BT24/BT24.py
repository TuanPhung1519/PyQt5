import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal, QThread
class MainWindow(QMainWindow):
    def __init__(self, index1=0):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        #self.uic.send_button.clicked.connect(self.senddata)
        self.uic.send_button.clicked.connect(self.receive_thread)

        #2. Truyen data giua tu class support -> class MAinWindow
        self.c = index1
        print("Data 2=",self.c)
        #3. Truyen data tu class(def __init__) sang def trong class do
        self.e = 9

        # 4. Truyen data tu def thuoc class nay sang def thuoc class khac
        self.thread = {}


    '''def senddata(self):
        #1. Truyen data tu def tu tao QMainWiondow -> class
        data = [2,3,4]
        self.thread1 = support(index= data)
        ###############

        # 3. Truyen data tu class(def __init__) sang def trong class do
        f = self.e
        print("Data 4=", f)'''

    def receive_thread(self):
        self.thread[1] = ThreadClass(index=1)
        self.thread[1].signal.connect(self.show_info)
        self.thread[1].start()

    def show_info(self, counter):
        m = counter
        print("Data 4=",m)


        
'''class support():
    def __init__(self, index=0):
        super().__init__()
        # 1. Truyen data tu def tu tao QMainWiondow -> class
        self.a = index
        print("Data 1=",self.a)
        ############################

        # 2. Truyen data giua tu class support -> class MAinWindow
        data_b = [5,6,7]
        self.b = MainWindow(index1=6)
        ##############'''
#4. Truyen data tu def thuoc class nay sang def thuoc class khac
class ThreadClass(QThread):
    signal = pyqtSignal(str)
    def __init__(self, index=0):
        super().__init__()
        self.index = index
    def run(self):
        counter = "Hello!"
        print("Start thread!")
        self.signal.emit(counter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ui = MainWindow()
    main_ui.show()
    sys.exit(app.exec_())