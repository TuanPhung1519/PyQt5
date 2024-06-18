import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow

import threading
import time
import keyboard
class MainWindow():
    def __init__(self):
        self.main_ui = QMainWindow()
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_ui)
        self.uic.start_button.clicked.connect(self.start)



    def start(self):
        global status
        status = True
        self.blink()
    def stop(self):
        global status
        status = False
        self.blink()

    def blink(self):
        def run():
            while status == True:
                print('Blink!')
                time.sleep(0.1)
                if keyboard.is_pressed('q'):
                    self.stop()

        thread1 = threading.Thread(target=run)
        thread1.start()
    def show(self):
        self.main_ui.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ui = MainWindow()
    main_ui.show()
    sys.exit(app.exec_())