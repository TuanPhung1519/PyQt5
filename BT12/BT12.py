import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Gui import Ui_MainWindow

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

class MainWindow:
    def __init__(self):
        self.main_ui = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_ui)
        #Khai bao nut nhan
        self.uic.pushButton.clicked.connect(self.show_diagram)
        #sc = MplCanvas(self, width=5, height=4, dpi=100)
        #sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])
        #self.uic.chart.addWidget(self.show_chart)


    def show(self):
        self.main_ui.show()

    def show_diagram(self):
        self.uic.chart.addChildWidget(MplCanvas())


#Tao 1 kieu du lieu hien thi do thi=> kieu du lieu ke thua tu FigureCanvasQTAgg
class MplCanvas(FigureCanvasQTAgg):
    def __init__(self):
        fig = Figure(figsize=(5, 4), dpi=100)
        self.axis = fig.add_subplot(111)
        super().__init__(fig)
        width = 0.35
        y1_axis = [20, 23, 123, 13, 12]
        y2_axis = [21, 26, 12, 13, 12]
        x1_axis = np.arange(len(y1_axis))
        bar1 = self.axis.bar(x1_axis - width/2, y1_axis, width,label='Blue')
        bar2 = self.axis.bar(x1_axis + width/2, y2_axis, width, label='Red')
        self.axis.bar_label(bar1)
        self.axis.bar_label(bar2)
        self.axis.set(ylabel='Datas', xlabel='Counts')
        fig.suptitle('man and women', size= 15)
        self.axis.legend()








if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ui = MainWindow()
    main_ui.show()
    sys.exit(app.exec_())
