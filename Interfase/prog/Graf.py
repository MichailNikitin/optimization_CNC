import sys
import openpyxl
import matplotlib.pyplot as plt
import matplotlib
import pylab

matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import pandas
excel_data_df = pandas.read_excel('datagrafiks2.xlsx', sheet_name='data1')

ddo = excel_data_df['ddo'].tolist()
time_cicle = excel_data_df['time_cicle'].tolist()


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=10, height=8, dpi=400):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.set_xlabel('Время подачи, минуты')
        self.axes.set_ylabel('Подача(фактическая и программная), мм')
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs, ):
        super(MainWindow, self).__init__(*args, **kwargs)

        sc = MplCanvas(self)

        sc.axes.plot(excel_data_df['time_cicle'].tolist(), excel_data_df['tp_ob[z]'].tolist())
        sc.axes.plot(excel_data_df['time_cicle'].tolist(), excel_data_df['tf_ob'].tolist())

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()