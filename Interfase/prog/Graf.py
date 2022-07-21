import sys
import openpyxl
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs, ):
        super(MainWindow, self).__init__(*args, **kwargs)

        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot(ddo, time_cicle)

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

ddo = [50.3, 50.2959874693863, 50.2872916714614, 50.2750251438493, 50.260236155994, 50.2437186769883, 50.2260348098752,
       50.2075706363046, 50.1885871349996, 50.1692591051679, 50.1497029749659, 50.1299960246567, 50.1101894364898,
       50.0903170599171, 50.0704012606187, 50.0504568075639, 50.0304934494445, 50.016972041566, 50.0075574847718,
       50.0008105162819, 49.9958306136035, 49.9920449757749, 49.9890827845386]
time_cicle = [0, 0.00333333333333333, 0.00666666666666667, 0.01, 0.0133333333333333, 0.0166666666666667, 0.02,
              0.0233333333333333, 0.0266666666666667, 0.03, 0.0333333333333333, 0.0366666666666667, 0.04,
              0.0433333333333333, 0.0466666666666667, 0.05, 0.0533333333333333, 0.0566666666666667, 0.06,
              0.0633333333333333, 0.0666666666666667, 0.07, 0.0733333333333333]

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()