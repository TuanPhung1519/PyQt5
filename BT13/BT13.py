import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI import Ui_MainWindow

#Add libraries for Chart
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

class MainWindow:
    def __init__(self):
        self.main_ui = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_ui)
        #Setup button show chart
        self.uic.pushButton.clicked.connect(self.showdata)

    def showdata(self):
        self.uic.verticalLayout.addChildWidget(MlpCanvas())
    def show(self):
        self.main_ui.show()

class MlpCanvas(FigureCanvasQTAgg):
    def __init__(self):
        fig = Figure(figsize= (5,4), dpi=100)#Cai dat kich thuoc do thi
        self.axes = fig.add_subplot(111)#Tao so o trong khung chua do thi va vi tri do thi
        super().__init__(fig)

        y_axis = [12,30,45,67]
        x_axis = ['a','b','c','d']
        colors = ['red', 'blue', 'green', 'orange', 'black']

        bar1 = self.axes.bar(x_axis, y_axis, label='Men', color=colors)
        self.axes.bar_label(bar1)#Hien thi gia tri tren cot
        fig.suptitle('Men and Women')
        self.axes.set(ylabel='Datas', xlabel='Counts')
        self.axes.legend()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ui = MainWindow()
    main_ui.show()
    sys.exit(app.exec_())


