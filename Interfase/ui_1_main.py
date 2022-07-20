# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '1_mainNXtLFH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(865, 517)
        MainWindow.setMinimumSize(QSize(700, 500))
        MainWindow.setIconSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(7)
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.import_2 = QPushButton(self.centralwidget)
        self.import_2.setObjectName(u"import_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_2.sizePolicy().hasHeightForWidth())
        self.import_2.setSizePolicy(sizePolicy)
        self.import_2.setMinimumSize(QSize(300, 80))
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(12)
        self.import_2.setFont(font)
        self.import_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 9px;\n"
"	background-color: rgb(187, 218, 255);\n"
"}")

        self.gridLayout.addWidget(self.import_2, 4, 1, 1, 1)

        self.indent_Above = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.indent_Above, 0, 1, 1, 1)

        self.create_new_graph = QPushButton(self.centralwidget)
        self.create_new_graph.setObjectName(u"create_new_graph")
        sizePolicy.setHeightForWidth(self.create_new_graph.sizePolicy().hasHeightForWidth())
        self.create_new_graph.setSizePolicy(sizePolicy)
        self.create_new_graph.setMinimumSize(QSize(300, 80))
        self.create_new_graph.setFont(font)
        self.create_new_graph.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 9px;\n"
"	background-color: rgb(187, 218, 255);\n"
"}")

        self.gridLayout.addWidget(self.create_new_graph, 3, 1, 1, 1)

        self.indent_Below = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.indent_Below, 5, 1, 1, 1)

        self.indent_Right = QSpacerItem(68, 55, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.indent_Right, 3, 2, 1, 1)

        self.indent_Left = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.indent_Left, 4, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.import_2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.create_new_graph.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
    # retranslateUi

