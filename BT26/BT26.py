import sys

import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow

from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QImage
import cv2

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        #Khoi tao 2 nut start, stop
        self.uic.start_button.clicked.connect(self.start_video)
        self.uic.stop_button.clicked.connect(self.stop_video)
        #Set init state for button
        self.uic.start_button.setEnabled(True)
        self.uic.stop_button.setEnabled(False)
        #Khoi tao 1 bien quan ly thread
        self.thread = {}
    def start_video(self):
        self.thread[1] = Thread_runvideo(index=1)
        self.thread[1].signal.connect(self.show_video)
        self.thread[1].start()
        self.uic.start_button.setEnabled(False)
        self.uic.stop_button.setEnabled(True)
    def stop_video(self):
        self.uic.start_button.setEnabled(True)
        self.uic.stop_button.setEnabled(False)
        self.uic.label.clear()
        self.thread[1].stop()
    def show_video(self, image):
        qt_img = self.convert_cv_qt(image)
        self.uic.label.setPixmap(qt_img)
    def convert_cv_qt(self, image):
        image_1 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        convertir_QT = QImage(image_1.data, image_1.shape[1], image_1.shape[0], QImage.Format_RGB888)
        pic = convertir_QT.scaled(741, 500, Qt.KeepAspectRatio)
        return QPixmap.fromImage(pic)







#Tao 1 class co nvu chay thread video
class Thread_runvideo(QThread):
    signal = pyqtSignal(np.ndarray)
    def __init__(self, index=0):
        super().__init__()
        self.index = index
    def putTxt(self, image):
        cv2.putText(image, 'FPS = 23.0', (10, 30), cv2.FONT_HERSHEY_DUPLEX,
                    1, (200, 100, 200), 2, cv2.FONT_HERSHEY_DUPLEX)
        return image

    def run(self):
        self.break_loopvideo = True
        print("Start Thread ", self.index)
        camera = cv2.VideoCapture(0)
        # Read video
        while self.break_loopvideo:
            ret, image = camera.read()
            if ret:
                image = self.putTxt(image)
                self.signal.emit(image)
    def stop(self):
        self.break_loopvideo = False
        print("Stop Thread ", self.index)
        self.quit()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ui = MainWindow()
    main_ui.show()
    sys.exit(app.exec_())