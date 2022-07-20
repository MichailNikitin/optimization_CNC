# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '3_paramDisCkD.ui'
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
        MainWindow.resize(1209, 801)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.l_grafs = QFrame(self.centralwidget)
        self.l_grafs.setObjectName(u"l_grafs")
        self.l_grafs.setFrameShape(QFrame.HLine)
        self.l_grafs.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.l_grafs)

        self.MainTabWidget = QTabWidget(self.centralwidget)
        self.MainTabWidget.setObjectName(u"MainTabWidget")
        self.MainTabWidget.setEnabled(True)
        font = QFont()
        font.setPointSize(10)
        self.MainTabWidget.setFont(font)
        self.MainTabWidget.setLayoutDirection(Qt.LeftToRight)
        self.MainTabWidget.setTabPosition(QTabWidget.North)
        self.MainTabWidget.setTabShape(QTabWidget.Rounded)
        self.MainTabWidget.setIconSize(QSize(16, 16))
        self.MainTabWidget.setElideMode(Qt.ElideNone)
        self.results = QWidget()
        self.results.setObjectName(u"results")
        self.gridLayout_12 = QGridLayout(self.results)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.MainTabWidget.addTab(self.results, "")
        self.input_par = QWidget()
        self.input_par.setObjectName(u"input_par")
        self.verticalLayout_5 = QVBoxLayout(self.input_par)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.GrafsTabWidget = QTabWidget(self.input_par)
        self.GrafsTabWidget.setObjectName(u"GrafsTabWidget")
        self.GrafsTabWidget.setFont(font)
        self.GrafsTabWidget.setToolTipDuration(-1)
        self.GrafsTabWidget.setIconSize(QSize(20, 20))
        self.GrafsTabWidget.setUsesScrollButtons(True)
        self.GrafsTabWidget.setDocumentMode(True)
        self.GrafsTabWidget.setTabsClosable(True)
        self.GrafsTabWidget.setMovable(True)
        self.GrafsTabWidget.setTabBarAutoHide(False)
        self.graf_1 = QWidget()
        self.graf_1.setObjectName(u"graf_1")
        self.verticalLayout = QVBoxLayout(self.graf_1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.data_entry_area = QWidget(self.graf_1)
        self.data_entry_area.setObjectName(u"data_entry_area")
        self.gridLayout_2 = QGridLayout(self.data_entry_area)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(20, 19, 20, 6)
        self.area_actions_widget = QWidget(self.data_entry_area)
        self.area_actions_widget.setObjectName(u"area_actions_widget")
        sizePolicy.setHeightForWidth(self.area_actions_widget.sizePolicy().hasHeightForWidth())
        self.area_actions_widget.setSizePolicy(sizePolicy)
        self.area_actions_widget.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_3 = QGridLayout(self.area_actions_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.actions = QWidget(self.area_actions_widget)
        self.actions.setObjectName(u"actions")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.actions.sizePolicy().hasHeightForWidth())
        self.actions.setSizePolicy(sizePolicy1)
        self.actions.setMaximumSize(QSize(500, 500))
        self.verticalLayout_4 = QVBoxLayout(self.actions)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.save_export_import_verticalLayout = QVBoxLayout()
        self.save_export_import_verticalLayout.setObjectName(u"save_export_import_verticalLayout")
        self.save_param_pushButton = QPushButton(self.actions)
        self.save_param_pushButton.setObjectName(u"save_param_pushButton")
        sizePolicy.setHeightForWidth(self.save_param_pushButton.sizePolicy().hasHeightForWidth())
        self.save_param_pushButton.setSizePolicy(sizePolicy)
        self.save_param_pushButton.setMinimumSize(QSize(0, 51))
        self.save_param_pushButton.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.save_param_pushButton.setFont(font1)
        self.save_param_pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 9px;\n"
"	background-color: rgb(187, 218, 255);\n"
"}")

        self.save_export_import_verticalLayout.addWidget(self.save_param_pushButton)

        self.create_new_pushButton = QPushButton(self.actions)
        self.create_new_pushButton.setObjectName(u"create_new_pushButton")
        self.create_new_pushButton.setMinimumSize(QSize(0, 51))
        self.create_new_pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 9px;\n"
"	background-color: rgb(187, 218, 255);\n"
"}")

        self.save_export_import_verticalLayout.addWidget(self.create_new_pushButton)

        self._export_import_horizontalLayout = QHBoxLayout()
        self._export_import_horizontalLayout.setObjectName(u"_export_import_horizontalLayout")
        self.export_pushButton = QPushButton(self.actions)
        self.export_pushButton.setObjectName(u"export_pushButton")
        sizePolicy.setHeightForWidth(self.export_pushButton.sizePolicy().hasHeightForWidth())
        self.export_pushButton.setSizePolicy(sizePolicy)
        self.export_pushButton.setMinimumSize(QSize(0, 50))
        self.export_pushButton.setMaximumSize(QSize(16777215, 16777215))
        self.export_pushButton.setFont(font)
        self.export_pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 7px;\n"
"	background-color: rgb(187, 218, 255);\n"
"}")

        self._export_import_horizontalLayout.addWidget(self.export_pushButton)

        self.import_param_pushButton = QPushButton(self.actions)
        self.import_param_pushButton.setObjectName(u"import_param_pushButton")
        sizePolicy.setHeightForWidth(self.import_param_pushButton.sizePolicy().hasHeightForWidth())
        self.import_param_pushButton.setSizePolicy(sizePolicy)
        self.import_param_pushButton.setMinimumSize(QSize(0, 50))
        self.import_param_pushButton.setMaximumSize(QSize(16777215, 16777215))
        self.import_param_pushButton.setFont(font)
        self.import_param_pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 7px;\n"
"	background-color: rgb(187, 218, 255);\n"
"}")

        self._export_import_horizontalLayout.addWidget(self.import_param_pushButton)


        self.save_export_import_verticalLayout.addLayout(self._export_import_horizontalLayout)


        self.verticalLayout_4.addLayout(self.save_export_import_verticalLayout)


        self.gridLayout_3.addWidget(self.actions, 1, 0, 1, 1)

        self.indent_BelowActions = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.indent_BelowActions, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.area_actions_widget, 7, 2, 1, 1)

        self.input_zag_widget = QWidget(self.data_entry_area)
        self.input_zag_widget.setObjectName(u"input_zag_widget")
        self.input_zag_widget.setMaximumSize(QSize(16777215, 400))
        self.gridLayout_4 = QGridLayout(self.input_zag_widget)
        self.gridLayout_4.setSpacing(11)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.dk_label = QLabel(self.input_zag_widget)
        self.dk_label.setObjectName(u"dk_label")
        font2 = QFont()
        font2.setPointSize(9)
        self.dk_label.setFont(font2)

        self.gridLayout_4.addWidget(self.dk_label, 5, 0, 1, 1)

        self.stzat_textbox = QLineEdit(self.input_zag_widget)
        self.stzat_textbox.setObjectName(u"stzat_textbox")
        self.stzat_textbox.setMinimumSize(QSize(0, 29))
        self.stzat_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}")

        self.gridLayout_4.addWidget(self.stzat_textbox, 4, 1, 1, 1)

        self.indent_BelowZag = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.indent_BelowZag, 7, 0, 1, 1)

        self.coefgg_textbox = QLineEdit(self.input_zag_widget)
        self.coefgg_textbox.setObjectName(u"coefgg_textbox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.coefgg_textbox.sizePolicy().hasHeightForWidth())
        self.coefgg_textbox.setSizePolicy(sizePolicy2)
        self.coefgg_textbox.setMinimumSize(QSize(0, 29))
        self.coefgg_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}")

        self.gridLayout_4.addWidget(self.coefgg_textbox, 6, 1, 1, 1)

        self.hgtc_label = QLabel(self.input_zag_widget)
        self.hgtc_label.setObjectName(u"hgtc_label")
        self.hgtc_label.setFont(font2)

        self.gridLayout_4.addWidget(self.hgtc_label, 4, 0, 1, 1)

        self.dr_pow_label = QLabel(self.input_zag_widget)
        self.dr_pow_label.setObjectName(u"dr_pow_label")
        self.dr_pow_label.setFont(font2)

        self.gridLayout_4.addWidget(self.dr_pow_label, 2, 0, 1, 1)

        self.acw_textbox = QLineEdit(self.input_zag_widget)
        self.acw_textbox.setObjectName(u"acw_textbox")
        self.acw_textbox.setMinimumSize(QSize(0, 29))
        self.acw_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}")

        self.gridLayout_4.addWidget(self.acw_textbox, 0, 1, 1, 1)

        self.coefgg_label = QLabel(self.input_zag_widget)
        self.coefgg_label.setObjectName(u"coefgg_label")
        self.coefgg_label.setFont(font2)

        self.gridLayout_4.addWidget(self.coefgg_label, 6, 0, 1, 1)

        self.sk_label = QLabel(self.input_zag_widget)
        self.sk_label.setObjectName(u"sk_label")
        self.sk_label.setFont(font2)

        self.gridLayout_4.addWidget(self.sk_label, 1, 0, 1, 1)

        self.acw_label = QLabel(self.input_zag_widget)
        self.acw_label.setObjectName(u"acw_label")
        self.acw_label.setFont(font2)

        self.gridLayout_4.addWidget(self.acw_label, 0, 0, 1, 1)

        self.sk_textbox = QLineEdit(self.input_zag_widget)
        self.sk_textbox.setObjectName(u"sk_textbox")
        self.sk_textbox.setMinimumSize(QSize(0, 29))
        self.sk_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}")

        self.gridLayout_4.addWidget(self.sk_textbox, 1, 1, 1, 1)

        self.hgtc_textbox = QLineEdit(self.input_zag_widget)
        self.hgtc_textbox.setObjectName(u"hgtc_textbox")
        self.hgtc_textbox.setMinimumSize(QSize(0, 29))
        self.hgtc_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}")

        self.gridLayout_4.addWidget(self.hgtc_textbox, 5, 1, 1, 1)

        self.dk_textbox = QLineEdit(self.input_zag_widget)
        self.dk_textbox.setObjectName(u"dk_textbox")
        self.dk_textbox.setMinimumSize(QSize(0, 29))
        self.dk_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.dk_textbox, 3, 1, 1, 1)

        self.dr_pow_textbox = QLineEdit(self.input_zag_widget)
        self.dr_pow_textbox.setObjectName(u"dr_pow_textbox")
        self.dr_pow_textbox.setMinimumSize(QSize(0, 29))
        self.dr_pow_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}")

        self.gridLayout_4.addWidget(self.dr_pow_textbox, 2, 1, 1, 1)

        self.stzat_label = QLabel(self.input_zag_widget)
        self.stzat_label.setObjectName(u"stzat_label")
        self.stzat_label.setFont(font2)

        self.gridLayout_4.addWidget(self.stzat_label, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.input_zag_widget, 4, 1, 1, 1)

        self.input_cycle_widget = QWidget(self.data_entry_area)
        self.input_cycle_widget.setObjectName(u"input_cycle_widget")
        self.input_cycle_widget.setEnabled(True)
        self.input_cycle_widget.setMaximumSize(QSize(16777215, 400))
        self.gridLayout_5 = QGridLayout(self.input_cycle_widget)
        self.gridLayout_5.setSpacing(11)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(11, 11, 0, 16)
        self.tp_ob_label = QLabel(self.input_cycle_widget)
        self.tp_ob_label.setObjectName(u"tp_ob_label")
        self.tp_ob_label.setFont(font2)
        self.tp_ob_label.setStyleSheet(u"QLabel {\n"
"	color: rgb(115, 115, 115)\n"
"}")

        self.gridLayout_5.addWidget(self.tp_ob_label, 4, 0, 1, 1)

        self.time_ob_label = QLabel(self.input_cycle_widget)
        self.time_ob_label.setObjectName(u"time_ob_label")
        self.time_ob_label.setFont(font2)
        self.time_ob_label.setStyleSheet(u"QLabel {\n"
"	color: rgb(115, 115, 115)\n"
"}")

        self.gridLayout_5.addWidget(self.time_ob_label, 3, 0, 1, 1)

        self.sp_textbox = QLineEdit(self.input_cycle_widget)
        self.sp_textbox.setObjectName(u"sp_textbox")
        self.sp_textbox.setMinimumSize(QSize(0, 29))
        self.sp_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}")

        self.gridLayout_5.addWidget(self.sp_textbox, 1, 1, 1, 1)

        self.time_ob_textbox = QLineEdit(self.input_cycle_widget)
        self.time_ob_textbox.setObjectName(u"time_ob_textbox")
        self.time_ob_textbox.setEnabled(False)
        self.time_ob_textbox.setMinimumSize(QSize(0, 29))
        self.time_ob_textbox.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.time_ob_textbox, 3, 1, 1, 1)

        self.sp_label = QLabel(self.input_cycle_widget)
        self.sp_label.setObjectName(u"sp_label")
        self.sp_label.setFont(font2)

        self.gridLayout_5.addWidget(self.sp_label, 1, 0, 1, 1)

        self.tp_ob_textbox = QLineEdit(self.input_cycle_widget)
        self.tp_ob_textbox.setObjectName(u"tp_ob_textbox")
        self.tp_ob_textbox.setEnabled(False)
        self.tp_ob_textbox.setMinimumSize(QSize(0, 29))

        self.gridLayout_5.addWidget(self.tp_ob_textbox, 4, 1, 1, 1)

        self.zmax_label = QLabel(self.input_cycle_widget)
        self.zmax_label.setObjectName(u"zmax_label")
        self.zmax_label.setFont(font2)

        self.gridLayout_5.addWidget(self.zmax_label, 0, 0, 1, 1)

        self.kz_textbox = QLineEdit(self.input_cycle_widget)
        self.kz_textbox.setObjectName(u"kz_textbox")
        self.kz_textbox.setMinimumSize(QSize(0, 29))
        self.kz_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}")

        self.gridLayout_5.addWidget(self.kz_textbox, 2, 1, 1, 1)

        self.indent_BelowCycle = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.indent_BelowCycle, 5, 0, 1, 1)

        self.kz_label = QLabel(self.input_cycle_widget)
        self.kz_label.setObjectName(u"kz_label")
        self.kz_label.setFont(font2)

        self.gridLayout_5.addWidget(self.kz_label, 2, 0, 1, 1)

        self.zmax_textbox = QLineEdit(self.input_cycle_widget)
        self.zmax_textbox.setObjectName(u"zmax_textbox")
        self.zmax_textbox.setMinimumSize(QSize(0, 29))
        self.zmax_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}")

        self.gridLayout_5.addWidget(self.zmax_textbox, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.input_cycle_widget, 4, 2, 1, 1)

        self.input_detail_widget = QWidget(self.data_entry_area)
        self.input_detail_widget.setObjectName(u"input_detail_widget")
        self.gridLayout_7 = QGridLayout(self.input_detail_widget)
        self.gridLayout_7.setSpacing(11)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(11, 11, 11, 11)
        self.prsk_label = QLabel(self.input_detail_widget)
        self.prsk_label.setObjectName(u"prsk_label")
        palette = QPalette()
        brush = QBrush(QColor(115, 115, 115, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(227, 227, 227, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(115, 115, 115, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush3 = QBrush(QColor(222, 165, 227, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(115, 115, 115, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        brush5 = QBrush(QColor(247, 247, 247, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(115, 115, 115, 128))
        brush6.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.prsk_label.setPalette(palette)
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setWeight(50)
        font3.setStrikeOut(False)
        self.prsk_label.setFont(font3)
        self.prsk_label.setCursor(QCursor(Qt.ArrowCursor))
        self.prsk_label.setMouseTracking(True)
        self.prsk_label.setFocusPolicy(Qt.WheelFocus)
        self.prsk_label.setAcceptDrops(False)
        self.prsk_label.setAutoFillBackground(False)
        self.prsk_label.setStyleSheet(u"QLabel {\n"
"	color: rgb(115, 115, 115)\n"
"}")
        self.prsk_label.setTextFormat(Qt.AutoText)

        self.gridLayout_7.addWidget(self.prsk_label, 6, 0, 1, 1)

        self.B_textbox = QLineEdit(self.input_detail_widget)
        self.B_textbox.setObjectName(u"B_textbox")
        self.B_textbox.setMinimumSize(QSize(0, 29))
        self.B_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}")

        self.gridLayout_7.addWidget(self.B_textbox, 1, 1, 1, 1)

        self.B_label = QLabel(self.input_detail_widget)
        self.B_label.setObjectName(u"B_label")
        self.B_label.setFont(font2)

        self.gridLayout_7.addWidget(self.B_label, 1, 0, 1, 1)

        self.td_textbox = QLineEdit(self.input_detail_widget)
        self.td_textbox.setObjectName(u"td_textbox")
        self.td_textbox.setMinimumSize(QSize(0, 29))
        self.td_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}")

        self.gridLayout_7.addWidget(self.td_textbox, 2, 1, 1, 1)

        self.indent_BelowDetail = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.indent_BelowDetail, 7, 0, 1, 1)

        self.dd_max_label = QLabel(self.input_detail_widget)
        self.dd_max_label.setObjectName(u"dd_max_label")
        self.dd_max_label.setFont(font2)

        self.gridLayout_7.addWidget(self.dd_max_label, 0, 0, 1, 1)

        self.rgn_dd_label = QLabel(self.input_detail_widget)
        self.rgn_dd_label.setObjectName(u"rgn_dd_label")
        self.rgn_dd_label.setFont(font2)

        self.gridLayout_7.addWidget(self.rgn_dd_label, 3, 0, 1, 1)

        self.rgn_dd_textbox = QLineEdit(self.input_detail_widget)
        self.rgn_dd_textbox.setObjectName(u"rgn_dd_textbox")
        self.rgn_dd_textbox.setMinimumSize(QSize(0, 29))
        self.rgn_dd_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}")

        self.gridLayout_7.addWidget(self.rgn_dd_textbox, 3, 1, 1, 1)

        self.sigma_textbox = QLineEdit(self.input_detail_widget)
        self.sigma_textbox.setObjectName(u"sigma_textbox")
        self.sigma_textbox.setMinimumSize(QSize(0, 29))
        self.sigma_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}")

        self.gridLayout_7.addWidget(self.sigma_textbox, 5, 1, 1, 1)

        self.sigma_label = QLabel(self.input_detail_widget)
        self.sigma_label.setObjectName(u"sigma_label")
        self.sigma_label.setFont(font2)

        self.gridLayout_7.addWidget(self.sigma_label, 5, 0, 1, 1)

        self.b_label = QLabel(self.input_detail_widget)
        self.b_label.setObjectName(u"b_label")
        self.b_label.setFont(font2)

        self.gridLayout_7.addWidget(self.b_label, 4, 0, 1, 1)

        self.dd_max_textbox = QLineEdit(self.input_detail_widget)
        self.dd_max_textbox.setObjectName(u"dd_max_textbox")
        self.dd_max_textbox.setMinimumSize(QSize(0, 29))
        self.dd_max_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}")

        self.gridLayout_7.addWidget(self.dd_max_textbox, 0, 1, 1, 1)

        self.b_textbox = QLineEdit(self.input_detail_widget)
        self.b_textbox.setObjectName(u"b_textbox")
        self.b_textbox.setMinimumSize(QSize(0, 29))
        self.b_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}")

        self.gridLayout_7.addWidget(self.b_textbox, 4, 1, 1, 1)

        self.prsk_textbox = QLineEdit(self.input_detail_widget)
        self.prsk_textbox.setObjectName(u"prsk_textbox")
        self.prsk_textbox.setEnabled(False)
        self.prsk_textbox.setMinimumSize(QSize(0, 29))

        self.gridLayout_7.addWidget(self.prsk_textbox, 6, 1, 1, 1)

        self.td_label = QLabel(self.input_detail_widget)
        self.td_label.setObjectName(u"td_label")
        self.td_label.setFont(font2)

        self.gridLayout_7.addWidget(self.td_label, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.input_detail_widget, 7, 0, 1, 1)

        self.machine_widget = QWidget(self.data_entry_area)
        self.machine_widget.setObjectName(u"machine_widget")
        self.gridLayout_6 = QGridLayout(self.machine_widget)
        self.gridLayout_6.setSpacing(11)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.vkst_textbox = QLineEdit(self.machine_widget)
        self.vkst_textbox.setObjectName(u"vkst_textbox")
        self.vkst_textbox.setMinimumSize(QSize(0, 29))
        self.vkst_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}")

        self.gridLayout_6.addWidget(self.vkst_textbox, 0, 1, 1, 1)

        self.nd_label = QLabel(self.machine_widget)
        self.nd_label.setObjectName(u"nd_label")
        self.nd_label.setFont(font2)

        self.gridLayout_6.addWidget(self.nd_label, 2, 0, 1, 1)

        self.vk_textbox = QLineEdit(self.machine_widget)
        self.vk_textbox.setObjectName(u"vk_textbox")
        self.vk_textbox.setEnabled(False)
        self.vk_textbox.setMinimumSize(QSize(0, 29))

        self.gridLayout_6.addWidget(self.vk_textbox, 1, 1, 1, 1)

        self.indent_BelowMachine = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.indent_BelowMachine, 4, 0, 1, 1)

        self.nd_textbox = QLineEdit(self.machine_widget)
        self.nd_textbox.setObjectName(u"nd_textbox")
        self.nd_textbox.setMinimumSize(QSize(0, 29))
        self.nd_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}")

        self.gridLayout_6.addWidget(self.nd_textbox, 2, 1, 1, 1)

        self.podatl_textbox = QLineEdit(self.machine_widget)
        self.podatl_textbox.setObjectName(u"podatl_textbox")
        self.podatl_textbox.setEnabled(False)
        self.podatl_textbox.setMinimumSize(QSize(0, 29))

        self.gridLayout_6.addWidget(self.podatl_textbox, 3, 1, 1, 1)

        self.vkst_label = QLabel(self.machine_widget)
        self.vkst_label.setObjectName(u"vkst_label")
        self.vkst_label.setFont(font2)

        self.gridLayout_6.addWidget(self.vkst_label, 0, 0, 1, 1)

        self.podatl_label = QLabel(self.machine_widget)
        self.podatl_label.setObjectName(u"podatl_label")
        self.podatl_label.setFont(font2)
        self.podatl_label.setStyleSheet(u"QLabel {\n"
"	color: rgb(115, 115, 115)\n"
"}")

        self.gridLayout_6.addWidget(self.podatl_label, 3, 0, 1, 1)

        self.vk_label = QLabel(self.machine_widget)
        self.vk_label.setObjectName(u"vk_label")
        self.vk_label.setFont(font2)
        self.vk_label.setStyleSheet(u"QLabel {\n"
"	color: rgb(115, 115, 115)\n"
"}")

        self.gridLayout_6.addWidget(self.vk_label, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.machine_widget, 7, 1, 1, 1)

        self.input_grinding_wheel_widget = QWidget(self.data_entry_area)
        self.input_grinding_wheel_widget.setObjectName(u"input_grinding_wheel_widget")
        self.input_grinding_wheel_widget.setMaximumSize(QSize(16777215, 400))
        self.gridLayout = QGridLayout(self.input_grinding_wheel_widget)
        self.gridLayout.setSpacing(11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(11, 11, 0, 11)
        self.indent_BelowGW = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.indent_BelowGW, 5, 0, 1, 1)

        self.E_textbox = QLineEdit(self.input_grinding_wheel_widget)
        self.E_textbox.setObjectName(u"E_textbox")
        self.E_textbox.setMinimumSize(QSize(0, 29))
        self.E_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}")

        self.gridLayout.addWidget(self.E_textbox, 3, 1, 1, 1)

        self.E_label = QLabel(self.input_grinding_wheel_widget)
        self.E_label.setObjectName(u"E_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.E_label.sizePolicy().hasHeightForWidth())
        self.E_label.setSizePolicy(sizePolicy3)
        self.E_label.setFont(font2)

        self.gridLayout.addWidget(self.E_label, 3, 0, 1, 1)

        self.tdz_label = QLabel(self.input_grinding_wheel_widget)
        self.tdz_label.setObjectName(u"tdz_label")
        sizePolicy3.setHeightForWidth(self.tdz_label.sizePolicy().hasHeightForWidth())
        self.tdz_label.setSizePolicy(sizePolicy3)
        self.tdz_label.setFont(font2)

        self.gridLayout.addWidget(self.tdz_label, 1, 0, 1, 1)

        self.dz_max_label = QLabel(self.input_grinding_wheel_widget)
        self.dz_max_label.setObjectName(u"dz_max_label")
        sizePolicy3.setHeightForWidth(self.dz_max_label.sizePolicy().hasHeightForWidth())
        self.dz_max_label.setSizePolicy(sizePolicy3)
        self.dz_max_label.setFont(font2)

        self.gridLayout.addWidget(self.dz_max_label, 0, 0, 1, 1)

        self.sum_flz__label = QLabel(self.input_grinding_wheel_widget)
        self.sum_flz__label.setObjectName(u"sum_flz__label")
        sizePolicy3.setHeightForWidth(self.sum_flz__label.sizePolicy().hasHeightForWidth())
        self.sum_flz__label.setSizePolicy(sizePolicy3)
        self.sum_flz__label.setFont(font2)

        self.gridLayout.addWidget(self.sum_flz__label, 4, 0, 1, 1)

        self.gab_dlin_textbox = QLineEdit(self.input_grinding_wheel_widget)
        self.gab_dlin_textbox.setObjectName(u"gab_dlin_textbox")
        self.gab_dlin_textbox.setMinimumSize(QSize(0, 29))
        self.gab_dlin_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}")

        self.gridLayout.addWidget(self.gab_dlin_textbox, 2, 1, 1, 1)

        self.sum_flz_textbox = QLineEdit(self.input_grinding_wheel_widget)
        self.sum_flz_textbox.setObjectName(u"sum_flz_textbox")
        self.sum_flz_textbox.setMinimumSize(QSize(0, 29))
        self.sum_flz_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}")

        self.gridLayout.addWidget(self.sum_flz_textbox, 4, 1, 1, 1)

        self.dz_max_textbox = QLineEdit(self.input_grinding_wheel_widget)
        self.dz_max_textbox.setObjectName(u"dz_max_textbox")
        self.dz_max_textbox.setEnabled(True)
        self.dz_max_textbox.setMinimumSize(QSize(0, 29))
        self.dz_max_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}")

        self.gridLayout.addWidget(self.dz_max_textbox, 0, 1, 1, 1)

        self.gab_dlin_label = QLabel(self.input_grinding_wheel_widget)
        self.gab_dlin_label.setObjectName(u"gab_dlin_label")
        sizePolicy3.setHeightForWidth(self.gab_dlin_label.sizePolicy().hasHeightForWidth())
        self.gab_dlin_label.setSizePolicy(sizePolicy3)
        self.gab_dlin_label.setFont(font2)

        self.gridLayout.addWidget(self.gab_dlin_label, 2, 0, 1, 1)

        self.tdz_textbox = QLineEdit(self.input_grinding_wheel_widget)
        self.tdz_textbox.setObjectName(u"tdz_textbox")
        self.tdz_textbox.setMinimumSize(QSize(0, 29))
        self.tdz_textbox.setStyleSheet(u"QLineEdit\n"
"{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(206, 224, 255);\n"
"}")

        self.gridLayout.addWidget(self.tdz_textbox, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.input_grinding_wheel_widget, 4, 0, 1, 1)

        self.line_Detail = QFrame(self.data_entry_area)
        self.line_Detail.setObjectName(u"line_Detail")
        self.line_Detail.setMaximumSize(QSize(280, 16777215))
        self.line_Detail.setFrameShadow(QFrame.Raised)
        self.line_Detail.setLineWidth(1)
        self.line_Detail.setMidLineWidth(0)
        self.line_Detail.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line_Detail, 6, 0, 1, 1)

        self.lineDW = QFrame(self.data_entry_area)
        self.lineDW.setObjectName(u"lineDW")
        self.lineDW.setMaximumSize(QSize(360, 16777215))
        self.lineDW.setLineWidth(1)
        self.lineDW.setMidLineWidth(0)
        self.lineDW.setFrameShape(QFrame.HLine)
        self.lineDW.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.lineDW, 2, 0, 1, 1)

        self.data_grinding_wheel_title = QLabel(self.data_entry_area)
        self.data_grinding_wheel_title.setObjectName(u"data_grinding_wheel_title")
        font4 = QFont()
        font4.setFamily(u"MS Shell Dlg 2")
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.data_grinding_wheel_title.setFont(font4)
        self.data_grinding_wheel_title.setIndent(0)

        self.gridLayout_2.addWidget(self.data_grinding_wheel_title, 0, 0, 1, 1)

        self.line_Zag = QFrame(self.data_entry_area)
        self.line_Zag.setObjectName(u"line_Zag")
        self.line_Zag.setMaximumSize(QSize(260, 16777215))
        self.line_Zag.setLineWidth(1)
        self.line_Zag.setMidLineWidth(0)
        self.line_Zag.setFrameShape(QFrame.HLine)
        self.line_Zag.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_Zag, 2, 1, 1, 1)

        self.data_entry_detail_title = QLabel(self.data_entry_area)
        self.data_entry_detail_title.setObjectName(u"data_entry_detail_title")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.data_entry_detail_title.setFont(font5)

        self.gridLayout_2.addWidget(self.data_entry_detail_title, 5, 0, 1, 1)

        self.data_entry_cycle_title = QLabel(self.data_entry_area)
        self.data_entry_cycle_title.setObjectName(u"data_entry_cycle_title")
        self.data_entry_cycle_title.setFont(font5)

        self.gridLayout_2.addWidget(self.data_entry_cycle_title, 0, 2, 1, 1)

        self.line_Cycle = QFrame(self.data_entry_area)
        self.line_Cycle.setObjectName(u"line_Cycle")
        self.line_Cycle.setMaximumSize(QSize(260, 16777215))
        self.line_Cycle.setFrameShadow(QFrame.Raised)
        self.line_Cycle.setLineWidth(1)
        self.line_Cycle.setMidLineWidth(0)
        self.line_Cycle.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line_Cycle, 2, 2, 1, 1)

        self.data_entry_zag_title = QLabel(self.data_entry_area)
        self.data_entry_zag_title.setObjectName(u"data_entry_zag_title")
        self.data_entry_zag_title.setFont(font5)

        self.gridLayout_2.addWidget(self.data_entry_zag_title, 0, 1, 1, 1)

        self.line_Machine = QFrame(self.data_entry_area)
        self.line_Machine.setObjectName(u"line_Machine")
        self.line_Machine.setMaximumSize(QSize(280, 16777215))
        self.line_Machine.setFrameShadow(QFrame.Raised)
        self.line_Machine.setLineWidth(1)
        self.line_Machine.setMidLineWidth(0)
        self.line_Machine.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line_Machine, 6, 1, 1, 1)

        self.data_entry_machine_title = QLabel(self.data_entry_area)
        self.data_entry_machine_title.setObjectName(u"data_entry_machine_title")
        self.data_entry_machine_title.setFont(font5)

        self.gridLayout_2.addWidget(self.data_entry_machine_title, 5, 1, 1, 1)


        self.verticalLayout.addWidget(self.data_entry_area)

        self.GrafsTabWidget.addTab(self.graf_1, "")
        self.graf_2 = QWidget()
        self.graf_2.setObjectName(u"graf_2")
        self.verticalLayout_2 = QVBoxLayout(self.graf_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.param_2 = QWidget(self.graf_2)
        self.param_2.setObjectName(u"param_2")

        self.verticalLayout_2.addWidget(self.param_2)

        self.GrafsTabWidget.addTab(self.graf_2, "")

        self.verticalLayout_5.addWidget(self.GrafsTabWidget)

        self.MainTabWidget.addTab(self.input_par, "")

        self.horizontalLayout_2.addWidget(self.MainTabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.MainTabWidget.setCurrentIndex(1)
        self.GrafsTabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.results), QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
        self.save_param_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.create_new_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 ", None))
        self.export_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.import_param_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442", None))
        self.dk_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u043a\u0440\u0443\u0433\u0430, \u043c\u043c", None))
        self.hgtc_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u043a\u0440\u0443\u0433\u0430, \u043c\u043c ", None))
        self.dr_pow_label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c \u043f\u0440\u0438\u0432\u043e\u0434\u0430 \u043a\u0440\u0443\u0433\u0430, \u043a\u0412\u0442", None))
        self.coefgg_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u0433\u0435\u043e\u043c\u0435\u0442\u0440\u0438\u0438 \u0437\u0435\u0440\u0435\u043d ", None))
        self.sk_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043a\u0440\u0443\u0433\u0430, \u043c/\u0441", None))
        self.acw_label.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442\u0438\u0432\u043d\u0430\u044f \u0448\u0438\u0440\u0438\u043d\u0430 \u043a\u0440\u0443\u0433\u0430, \u043c\u043c", None))
        self.stzat_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0435\u043f\u0435\u043d\u044c \u0437\u0430\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f \u043a\u0440\u0443\u0433\u0430, \u043c\u043c ", None))
        self.tp_ob_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u0430\u044f \u043c\u0438\u043d\u0443\u0442\u043d\u0430\u044f \u043f\u043e\u0434\u0430\u0447\u0430 \n"
"\u043d\u0430 \u043e\u0431\u043e\u0440\u043e\u0442 \u0441\u0442\u0443\u043f\u0435\u043d\u044f\u0445 \u0446\u0438\u043a\u043b\u0430, \u043c\u043c/\u043c\u0438\u043d", None))
        self.time_ob_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043e\u0434\u043d\u043e\u0433\u043e \u043e\u0431\u043e\u0440\u043e\u0442\u0430 \u0437\u0430\u0433\u043e\u0442\u043e\u0432\u043a\u0438, \u043c\u0438\u043d", None))
        self.sp_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u0430\u044f \u043c\u0438\u043d\u0443\u0442\u043d\u0430\u044f \u043f\u043e\u0434\u0430\u0447\u0430 \u043d\u0430 \n"
"\u0441\u0442\u0443\u043f\u0435\u043d\u044f\u0445 \u0446\u0438\u043a\u043b\u0430, \u043c\u043c/\u043c\u0438\u043d", None))
        self.zmax_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u0443\u043f\u0435\u043d\u0435\u0439 \u0446\u0438\u043a\u043b\u0430 ", None))
        self.kz_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u043f\u0440\u0438\u043f\u0443\u0441\u043a\u0430", None))
        self.prsk_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043f\u0443\u0441\u043a \u043d\u0430 \u0434\u0438\u0430\u043c\u0435\u0442\u0440 \u0434\u0435\u0442\u0430\u043b\u0438, \u043c\u043c", None))
        self.B_label.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u0438\u043d\u0430 \u0448\u043b\u0438\u0444\u043e\u0432\u0430\u043d\u0438\u044f \u0434\u0435\u0442\u0430\u043b\u0438, \u043c\u043c", None))
        self.dd_max_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u0434\u0435\u0442\u0430\u043b\u0438, \u043c\u043c", None))
        self.rgn_dd_label.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0435\u0440\u043e\u0445\u043e\u0432\u0430\u0442\u043e\u0441\u0442\u044c \u0434\u0438\u0430\u043c\u0435\u0442\u0440\u0430 \u0434\u0435\u0442\u0430\u043b\u0438, \u043c\u043a\u043c ", None))
        self.sigma_label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0442\u0435\u043d\u0441\u0438\u0432\u043d\u043e\u0441\u0442\u044c \u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0439, \u043a\u0433/\u043c\u043c^2", None))
        self.b_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430 \u0448\u043b\u0438\u0444\u0443\u0435\u043c\u043e\u0439 \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u0438\n"
"\u0434\u0435\u0442\u0430\u043b\u0438, \u043c\u043c ", None))
        self.td_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u0443\u0441\u043a \u0434\u0438\u0430\u043c\u0435\u0442\u0440\u0430 \u0434\u0435\u0442\u0430\u043b\u0438, \u043c\u043c", None))
        self.nd_label.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430 \u0432\u0440\u0430\u0449\u0435\u043d\u0438\u044f \u0434\u0435\u0442\u0430\u043b\u0438, \u043e\u0431/\u043c\u0438\u043d", None))
        self.vkst_label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u0440\u0443\u0436\u043d\u0430\u044f \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u0432\u0440\u0430\u0449\u0435\u043d\u0438\u044f\n"
"\u043a\u0440\u0443\u0433\u0430, \u043c/\u0441", None))
        self.podatl_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0434\u0430\u0442\u043b\u0438\u0432\u043e\u0441\u0442\u044c \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \n"
"\u0441\u0438\u0441\u0442\u0435\u043c\u044b, \u043c\u043c/\u043a\u0433 ", None))
        self.vk_label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u0440\u0443\u0436\u043d\u0430\u044f \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u0432\u0440\u0430\u0449\u0435\u043d\u0438\u044f\n"
"\u043a\u0440\u0443\u0433\u0430, \u043c\u043c/\u043c\u0438\u043d", None))
        self.E_label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u0443\u043f\u0440\u0443\u0433\u043e\u0441\u0442\u0438 \u0437\u0430\u0433\u043e\u0442\u043e\u0432\u043a\u0438, \u043c\u043c ", None))
        self.tdz_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u0443\u0441\u043a \u0434\u0438\u0430\u043c\u0435\u0442\u0440\u0430 \u0437\u0430\u0433\u043e\u0442\u043e\u0432\u043a\u0438, \u043c\u043c ", None))
        self.dz_max_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u0437\u0430\u0433\u043e\u0442\u043e\u0432\u043a\u0438, \u043c\u043c ", None))
        self.sum_flz__label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0433\u043c\u0430 \u0442\u0435\u043a\u0443\u0447\u0435\u0441\u0442\u0438 \u0437\u0430\u0433\u043e\u0442\u043e\u0432\u043a\u0438, \u041d/\u043c^2", None))
        self.gab_dlin_label.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0430\u0431\u0430\u0440\u0438\u0442\u043d\u0430\u044f \u0434\u043b\u0438\u043d\u0430 \u0437\u0430\u0433\u043e\u0442\u043e\u0432\u043a\u0438, \u043c\u043c", None))
        self.data_grinding_wheel_title.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434 \u0434\u0430\u043d\u043d\u044b\u0445 \u043f\u043e \u0448\u043b\u0438\u0444\u043e\u0432\u0430\u043b\u044c\u043d\u043e\u043c\u0443 \u043a\u0440\u0443\u0433\u0443", None))
        self.data_entry_detail_title.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434 \u0434\u0430\u043d\u043d\u044b\u0445 \u043f\u043e \u0434\u0435\u0442\u0430\u043b\u0438", None))
        self.data_entry_cycle_title.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434 \u0434\u0430\u043d\u043d\u044b\u0445 \u043f\u043e \u0446\u0438\u043a\u043b\u0443", None))
        self.data_entry_zag_title.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434 \u0434\u0430\u043d\u043d\u044b\u0445 \u043f\u043e \u0437\u0430\u0433\u043e\u0442\u043e\u0432\u043a\u0435", None))
        self.data_entry_machine_title.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434 \u0434\u0430\u043d\u043d\u044b\u0445 \u043f\u043e \u0441\u0442\u0430\u043d\u043a\u0443", None))
        self.GrafsTabWidget.setTabText(self.GrafsTabWidget.indexOf(self.graf_1), QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a 1", None))
        self.GrafsTabWidget.setTabText(self.GrafsTabWidget.indexOf(self.graf_2), QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a 2", None))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.input_par), QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432", None))
    # retranslateUi

