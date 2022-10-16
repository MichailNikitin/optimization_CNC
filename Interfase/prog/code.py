from PyQt5 import QtWidgets
import PyQt5.QtCore as QtCore

import main, param, type

import sys


class mywindow(QtWidgets.QMainWindow, main.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.create_new_graph.clicked.connect(self.__click_button)
        self.import_2.clicked.connect(self.__click_break)

    def __click_button(self):
        print("click")

    def __click_break(self):
        print("click2")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = mywindow()
    application.show()
    app.exec_()