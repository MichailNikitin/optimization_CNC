from PyQt5 import QtWidgets

from main import Ui_MainWindow
from param import Ui_StartWindow

import sys

UI_MAIN_WINDOW = Ui_MainWindow()
UI_START_WINDOW = Ui_StartWindow()

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = UI_MAIN_WINDOW
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())