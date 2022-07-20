# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '2_typegmPhop.ui'
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
        MainWindow.resize(659, 564)
        MainWindow.setMaximumSize(QSize(850, 700))
        MainWindow.setAutoFillBackground(True)
        self.type_z_lin_widget = QWidget(MainWindow)
        self.type_z_lin_widget.setObjectName(u"type_z_lin_widget")
        self.verticalLayout_2 = QVBoxLayout(self.type_z_lin_widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.line_1 = QFrame(self.type_z_lin_widget)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setFrameShape(QFrame.HLine)
        self.line_1.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_1)

        self.name_graph_line = QLineEdit(self.type_z_lin_widget)
        self.name_graph_line.setObjectName(u"name_graph_line")
        self.name_graph_line.setMinimumSize(QSize(0, 60))
        self.name_graph_line.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(12)
        self.name_graph_line.setFont(font)
        self.name_graph_line.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(250, 250, 250);\n"
"}\n"
"\n"
"")
        self.name_graph_line.setEchoMode(QLineEdit.Normal)
        self.name_graph_line.setCursorPosition(0)
        self.name_graph_line.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.name_graph_line)

        self.line_2 = QFrame(self.type_z_lin_widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.main_type_z_lin_widget = QWidget(self.type_z_lin_widget)
        self.main_type_z_lin_widget.setObjectName(u"main_type_z_lin_widget")
        font1 = QFont()
        font1.setPointSize(8)
        self.main_type_z_lin_widget.setFont(font1)
        self.main_type_z_lin_widget.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(self.main_type_z_lin_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(19)
        self.gridLayout.setVerticalSpacing(11)
        self.gridLayout.setContentsMargins(12, 34, 20, 18)
        self.type_label = QLabel(self.main_type_z_lin_widget)
        self.type_label.setObjectName(u"type_label")
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.type_label.setFont(font2)

        self.gridLayout.addWidget(self.type_label, 0, 0, 1, 1)

        self.field_add_a_step = QWidget(self.main_type_z_lin_widget)
        self.field_add_a_step.setObjectName(u"field_add_a_step")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.field_add_a_step.sizePolicy().hasHeightForWidth())
        self.field_add_a_step.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.field_add_a_step)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(24)
        self.gridLayout_2.setContentsMargins(-1, 9, 11, 6)
        self.add_step_pushButton = QPushButton(self.field_add_a_step)
        self.add_step_pushButton.setObjectName(u"add_step_pushButton")
        sizePolicy.setHeightForWidth(self.add_step_pushButton.sizePolicy().hasHeightForWidth())
        self.add_step_pushButton.setSizePolicy(sizePolicy)
        self.add_step_pushButton.setMinimumSize(QSize(0, 36))
        font3 = QFont()
        font3.setFamily(u"Tahoma")
        font3.setPointSize(11)
        self.add_step_pushButton.setFont(font3)

        self.gridLayout_2.addWidget(self.add_step_pushButton, 0, 0, 1, 1)

        self.delete_step_pushButton = QPushButton(self.field_add_a_step)
        self.delete_step_pushButton.setObjectName(u"delete_step_pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.delete_step_pushButton.sizePolicy().hasHeightForWidth())
        self.delete_step_pushButton.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setPointSize(11)
        self.delete_step_pushButton.setFont(font4)

        self.gridLayout_2.addWidget(self.delete_step_pushButton, 0, 1, 1, 1)

        self.indent_Left_add_a_step = QSpacerItem(135, 32, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.indent_Left_add_a_step, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.field_add_a_step, 8, 0, 1, 2)

        self.data_entry_field = QScrollArea(self.main_type_z_lin_widget)
        self.data_entry_field.setObjectName(u"data_entry_field")
        sizePolicy1.setHeightForWidth(self.data_entry_field.sizePolicy().hasHeightForWidth())
        self.data_entry_field.setSizePolicy(sizePolicy1)
        self.data_entry_field.setMinimumSize(QSize(0, 140))
        self.data_entry_field.setStyleSheet(u"")
        self.data_entry_field.setFrameShape(QFrame.NoFrame)
        self.data_entry_field.setWidgetResizable(True)
        self.type_z_data_entry_field = QWidget()
        self.type_z_data_entry_field.setObjectName(u"type_z_data_entry_field")
        self.type_z_data_entry_field.setGeometry(QRect(0, 0, 627, 140))
        self.gridLayout_3 = QGridLayout(self.type_z_data_entry_field)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(18)
        self.gridLayout_3.setVerticalSpacing(7)
        self.input_type_z_lin_label = QLabel(self.type_z_data_entry_field)
        self.input_type_z_lin_label.setObjectName(u"input_type_z_lin_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.input_type_z_lin_label.sizePolicy().hasHeightForWidth())
        self.input_type_z_lin_label.setSizePolicy(sizePolicy2)
        self.input_type_z_lin_label.setFont(font2)
        self.input_type_z_lin_label.setStyleSheet(u" QFrame::NoFrame")

        self.gridLayout_3.addWidget(self.input_type_z_lin_label, 0, 0, 1, 4)

        self.input_type_z_stup_label = QLabel(self.type_z_data_entry_field)
        self.input_type_z_stup_label.setObjectName(u"input_type_z_stup_label")
        sizePolicy2.setHeightForWidth(self.input_type_z_stup_label.sizePolicy().hasHeightForWidth())
        self.input_type_z_stup_label.setSizePolicy(sizePolicy2)
        self.input_type_z_stup_label.setFont(font3)
        self.input_type_z_stup_label.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.gridLayout_3.addWidget(self.input_type_z_stup_label, 1, 0, 1, 4)

        self.dz_label = QLabel(self.type_z_data_entry_field)
        self.dz_label.setObjectName(u"dz_label")
        font5 = QFont()
        font5.setFamily(u"Tahoma")
        font5.setPointSize(10)
        self.dz_label.setFont(font5)

        self.gridLayout_3.addWidget(self.dz_label, 2, 0, 1, 1)

        self.dlin_one_textbox = QLineEdit(self.type_z_data_entry_field)
        self.dlin_one_textbox.setObjectName(u"dlin_one_textbox")
        sizePolicy1.setHeightForWidth(self.dlin_one_textbox.sizePolicy().hasHeightForWidth())
        self.dlin_one_textbox.setSizePolicy(sizePolicy1)
        self.dlin_one_textbox.setMaximumSize(QSize(150, 30))
        self.dlin_one_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.dlin_one_textbox, 2, 3, 1, 1)

        self.dlin_one_label = QLabel(self.type_z_data_entry_field)
        self.dlin_one_label.setObjectName(u"dlin_one_label")
        self.dlin_one_label.setFont(font5)

        self.gridLayout_3.addWidget(self.dlin_one_label, 2, 2, 1, 1)

        self.line = QFrame(self.type_z_data_entry_field)
        self.line.setObjectName(u"line")
        font6 = QFont()
        font6.setPointSize(8)
        font6.setUnderline(False)
        font6.setStrikeOut(False)
        self.line.setFont(font6)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 5, 0, 1, 4)

        self.dz_textbox = QLineEdit(self.type_z_data_entry_field)
        self.dz_textbox.setObjectName(u"dz_textbox")
        sizePolicy1.setHeightForWidth(self.dz_textbox.sizePolicy().hasHeightForWidth())
        self.dz_textbox.setSizePolicy(sizePolicy1)
        self.dz_textbox.setMinimumSize(QSize(30, 30))
        self.dz_textbox.setMaximumSize(QSize(150, 30))
        self.dz_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}")

        self.gridLayout_3.addWidget(self.dz_textbox, 2, 1, 1, 1)

        self.data_entry_field.setWidget(self.type_z_data_entry_field)

        self.gridLayout.addWidget(self.data_entry_field, 3, 0, 5, 3)

        self.save_type_z_lin_pushButton = QPushButton(self.main_type_z_lin_widget)
        self.save_type_z_lin_pushButton.setObjectName(u"save_type_z_lin_pushButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.save_type_z_lin_pushButton.sizePolicy().hasHeightForWidth())
        self.save_type_z_lin_pushButton.setSizePolicy(sizePolicy3)
        self.save_type_z_lin_pushButton.setMinimumSize(QSize(160, 50))
        self.save_type_z_lin_pushButton.setMaximumSize(QSize(100, 30))
        self.save_type_z_lin_pushButton.setFont(font5)
        self.save_type_z_lin_pushButton.setStyleSheet(u"")

        self.gridLayout.addWidget(self.save_type_z_lin_pushButton, 10, 2, 1, 1)

        self.type_widget = QWidget(self.main_type_z_lin_widget)
        self.type_widget.setObjectName(u"type_widget")
        sizePolicy1.setHeightForWidth(self.type_widget.sizePolicy().hasHeightForWidth())
        self.type_widget.setSizePolicy(sizePolicy1)
        self.type_widget.setMinimumSize(QSize(150, 150))
        self.type_widget.setMaximumSize(QSize(400, 200))
        self.type_widget.setStyleSheet(u"border-radius:5px;\n"
"	background-color: rgb(213, 211, 208);\n"
"")
        self.gridLayout_4 = QGridLayout(self.type_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.indent_LeftG = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.indent_LeftG, 1, 0, 1, 1)

        self.indent_BelowG = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.indent_BelowG, 2, 1, 1, 1)

        self.indent_RightG = QSpacerItem(80, 60, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.indent_RightG, 1, 2, 1, 1)

        self.indent_AboveG = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.indent_AboveG, 0, 1, 1, 1)

        self.type_frame = QFrame(self.type_widget)
        self.type_frame.setObjectName(u"type_frame")
        self.type_frame.setStyleSheet(u"background-color: rgb(247, 247, 247);")
        self.type_frame.setFrameShape(QFrame.StyledPanel)
        self.type_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.type_frame, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.type_widget, 0, 1, 1, 2)

        self.indent_Below_add_a_step = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.indent_Below_add_a_step, 9, 0, 2, 1)


        self.verticalLayout_2.addWidget(self.main_type_z_lin_widget)

        MainWindow.setCentralWidget(self.type_z_lin_widget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.name_graph_line.setText("")
        self.name_graph_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0433\u0440\u0430\u0444\u0438\u043a\u0430", u"kuguil"))
        self.type_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434 \u0437\u0430\u0433\u043e\u0442\u043e\u0432\u043a\u0438:", None))
        self.add_step_pushButton.setText(QCoreApplication.translate("MainWindow", u"  + \u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u0442\u0443\u043f\u0435\u043d\u044c  ", None))
        self.delete_step_pushButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.input_type_z_lin_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434 \u0434\u0430\u043d\u043d\u044b\u0445 \u0434\u043b\u044f \u0432\u0441\u0435\u0439 \u0437\u0430\u0433\u043e\u0442\u043e\u0432\u043a\u0438", None))
        self.input_type_z_stup_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434 \u0434\u0430\u043d\u043d\u044b\u0445 \u0434\u043b\u044f \u043f\u0435\u0440\u0432\u043e\u0439 \u0441\u0442\u0443\u043f\u0435\u043d\u0438 \u0437\u0430\u0433\u043e\u0442\u043e\u0432\u043a\u0438", None))
        self.dz_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u0437\u0430\u0433\u043e\u0442\u043e\u0432\u043a\u0438, \u043c\u043c", None))
        self.dlin_one_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430 \u0437\u0430\u0433\u043e\u0442\u043e\u0432\u043a\u0438, \u043c\u043c", None))
        self.save_type_z_lin_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

