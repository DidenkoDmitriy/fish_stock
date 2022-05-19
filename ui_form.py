# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1160, 861)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.age_structure_calculation = QTabWidget(self.centralwidget)
        self.age_structure_calculation.setObjectName(u"age_structure_calculation")
        self.tab_SQL_Base_connect = QWidget()
        self.tab_SQL_Base_connect.setObjectName(u"tab_SQL_Base_connect")
        self.verticalLayoutWidget_6 = QWidget(self.tab_SQL_Base_connect)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(30, 320, 211, 82))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_tab_sql_bioanalis_table_list = QLabel(self.verticalLayoutWidget_6)
        self.label_tab_sql_bioanalis_table_list.setObjectName(u"label_tab_sql_bioanalis_table_list")
        font = QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label_tab_sql_bioanalis_table_list.setFont(font)

        self.verticalLayout_6.addWidget(self.label_tab_sql_bioanalis_table_list)

        self.comboBox_tab_sql_bioanalis_table_list = QComboBox(self.verticalLayoutWidget_6)
        self.comboBox_tab_sql_bioanalis_table_list.setObjectName(u"comboBox_tab_sql_bioanalis_table_list")
        self.comboBox_tab_sql_bioanalis_table_list.setEnabled(False)

        self.verticalLayout_6.addWidget(self.comboBox_tab_sql_bioanalis_table_list)

        self.pushButton_sql_bioanalis_choose_table = QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_sql_bioanalis_choose_table.setObjectName(u"pushButton_sql_bioanalis_choose_table")
        self.pushButton_sql_bioanalis_choose_table.setEnabled(False)

        self.verticalLayout_6.addWidget(self.pushButton_sql_bioanalis_choose_table)

        self.horizontalLayoutWidget = QWidget(self.tab_SQL_Base_connect)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(150, 220, 371, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_Connect_SQL_DB = QPushButton(self.horizontalLayoutWidget)
        self.btn_Connect_SQL_DB.setObjectName(u"btn_Connect_SQL_DB")

        self.horizontalLayout.addWidget(self.btn_Connect_SQL_DB)

        self.btn_DisConnect_SQL_DB = QPushButton(self.horizontalLayoutWidget)
        self.btn_DisConnect_SQL_DB.setObjectName(u"btn_DisConnect_SQL_DB")
        self.btn_DisConnect_SQL_DB.setEnabled(False)

        self.horizontalLayout.addWidget(self.btn_DisConnect_SQL_DB)

        self.gridLayoutWidget = QWidget(self.tab_SQL_Base_connect)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 20, 811, 161))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_DB_Name = QLabel(self.gridLayoutWidget)
        self.label_DB_Name.setObjectName(u"label_DB_Name")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_DB_Name.setFont(font1)
        self.label_DB_Name.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.label_DB_Name.setMargin(10)

        self.gridLayout_2.addWidget(self.label_DB_Name, 2, 0, 1, 1)

        self.label_SQL_Name = QLabel(self.gridLayoutWidget)
        self.label_SQL_Name.setObjectName(u"label_SQL_Name")
        self.label_SQL_Name.setFont(font1)
        self.label_SQL_Name.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.label_SQL_Name.setMargin(10)

        self.gridLayout_2.addWidget(self.label_SQL_Name, 0, 0, 1, 1)

        self.label_SQL_Server_Name = QLabel(self.gridLayoutWidget)
        self.label_SQL_Server_Name.setObjectName(u"label_SQL_Server_Name")
        self.label_SQL_Server_Name.setFont(font1)
        self.label_SQL_Server_Name.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.label_SQL_Server_Name.setMargin(10)

        self.gridLayout_2.addWidget(self.label_SQL_Server_Name, 1, 0, 1, 1)

        self.lineEdit_SQL_Name = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_SQL_Name.setObjectName(u"lineEdit_SQL_Name")

        self.gridLayout_2.addWidget(self.lineEdit_SQL_Name, 0, 1, 1, 1)

        self.lineEdit_DB_Name = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_DB_Name.setObjectName(u"lineEdit_DB_Name")

        self.gridLayout_2.addWidget(self.lineEdit_DB_Name, 2, 1, 1, 1)

        self.lineEdit_SQL_Server_Name = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_SQL_Server_Name.setObjectName(u"lineEdit_SQL_Server_Name")
        self.lineEdit_SQL_Server_Name.setReadOnly(False)

        self.gridLayout_2.addWidget(self.lineEdit_SQL_Server_Name, 1, 1, 1, 1)

        self.age_structure_calculation.addTab(self.tab_SQL_Base_connect, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayoutWidget_2 = QWidget(self.tab_3)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(720, 30, 160, 80))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_tab_age_struct_area_list = QLabel(self.verticalLayoutWidget_2)
        self.label_tab_age_struct_area_list.setObjectName(u"label_tab_age_struct_area_list")

        self.verticalLayout_3.addWidget(self.label_tab_age_struct_area_list)

        self.comboBox_tab_age_struct_area_list = QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_tab_age_struct_area_list.setObjectName(u"comboBox_tab_age_struct_area_list")
        self.comboBox_tab_age_struct_area_list.setEnabled(False)

        self.verticalLayout_3.addWidget(self.comboBox_tab_age_struct_area_list)

        self.verticalLayoutWidget_3 = QWidget(self.tab_3)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(220, 580, 207, 141))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lbl_export_age_structure_calculation_to_sql = QLabel(self.verticalLayoutWidget_3)
        self.lbl_export_age_structure_calculation_to_sql.setObjectName(u"lbl_export_age_structure_calculation_to_sql")

        self.verticalLayout_4.addWidget(self.lbl_export_age_structure_calculation_to_sql)

        self.comboBox_export_age_structure_calculation_to_sql = QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_export_age_structure_calculation_to_sql.setObjectName(u"comboBox_export_age_structure_calculation_to_sql")

        self.verticalLayout_4.addWidget(self.comboBox_export_age_structure_calculation_to_sql)

        self.textEdit_age_structure_calculation_for_print_dataframe = QTextEdit(self.tab_3)
        self.textEdit_age_structure_calculation_for_print_dataframe.setObjectName(u"textEdit_age_structure_calculation_for_print_dataframe")
        self.textEdit_age_structure_calculation_for_print_dataframe.setGeometry(QRect(460, 170, 631, 461))
        self.button_age_structure_calculation_print_results = QPushButton(self.tab_3)
        self.button_age_structure_calculation_print_results.setObjectName(u"button_age_structure_calculation_print_results")
        self.button_age_structure_calculation_print_results.setGeometry(QRect(460, 630, 631, 51))
        self.button_age_structure_calculation_save_results = QPushButton(self.tab_3)
        self.button_age_structure_calculation_save_results.setObjectName(u"button_age_structure_calculation_save_results")
        self.button_age_structure_calculation_save_results.setGeometry(QRect(460, 680, 631, 51))
        self.verticalLayoutWidget_4 = QWidget(self.tab_3)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(380, 30, 160, 80))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_tab_age_struct_type_list = QLabel(self.verticalLayoutWidget_4)
        self.label_tab_age_struct_type_list.setObjectName(u"label_tab_age_struct_type_list")

        self.verticalLayout.addWidget(self.label_tab_age_struct_type_list)

        self.comboBox_tab_age_struct_type_list = QComboBox(self.verticalLayoutWidget_4)
        self.comboBox_tab_age_struct_type_list.setObjectName(u"comboBox_tab_age_struct_type_list")
        self.comboBox_tab_age_struct_type_list.setEnabled(False)

        self.verticalLayout.addWidget(self.comboBox_tab_age_struct_type_list)

        self.verticalLayoutWidget_5 = QWidget(self.tab_3)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(550, 30, 160, 80))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_tab_age_struct_year_list = QLabel(self.verticalLayoutWidget_5)
        self.label_tab_age_struct_year_list.setObjectName(u"label_tab_age_struct_year_list")

        self.verticalLayout_5.addWidget(self.label_tab_age_struct_year_list)

        self.comboBox_tab_age_struct_year_list = QComboBox(self.verticalLayoutWidget_5)
        self.comboBox_tab_age_struct_year_list.setObjectName(u"comboBox_tab_age_struct_year_list")
        self.comboBox_tab_age_struct_year_list.setEnabled(False)

        self.verticalLayout_5.addWidget(self.comboBox_tab_age_struct_year_list)

        self.verticalLayoutWidget_7 = QWidget(self.tab_3)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(60, 20, 231, 80))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_tab_age_struct_type_list_2 = QLabel(self.verticalLayoutWidget_7)
        self.label_tab_age_struct_type_list_2.setObjectName(u"label_tab_age_struct_type_list_2")

        self.verticalLayout_2.addWidget(self.label_tab_age_struct_type_list_2)

        self.comboBox_tab_age_struct_type_list_2 = QComboBox(self.verticalLayoutWidget_7)
        self.comboBox_tab_age_struct_type_list_2.setObjectName(u"comboBox_tab_age_struct_type_list_2")
        self.comboBox_tab_age_struct_type_list_2.setEnabled(False)

        self.verticalLayout_2.addWidget(self.comboBox_tab_age_struct_type_list_2)

        self.age_structure_calculation.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.age_structure_calculation.addTab(self.tab_4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.age_structure_calculation.addTab(self.tab_2, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.age_structure_calculation.addTab(self.tab_5, "")

        self.gridLayout.addWidget(self.age_structure_calculation, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1160, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.age_structure_calculation.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_tab_sql_bioanalis_table_list.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u0431\u0438\u043e\u0430\u043d\u0430\u043b\u0438\u0437\u0430", None))
        self.pushButton_sql_bioanalis_choose_table.setText(QCoreApplication.translate("MainWindow", u"choose table", None))
        self.btn_Connect_SQL_DB.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.btn_DisConnect_SQL_DB.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.label_DB_Name.setText(QCoreApplication.translate("MainWindow", u"DB Name", None))
        self.label_SQL_Name.setText(QCoreApplication.translate("MainWindow", u"SQL Server", None))
        self.label_SQL_Server_Name.setText(QCoreApplication.translate("MainWindow", u"Server Name", None))
        self.age_structure_calculation.setTabText(self.age_structure_calculation.indexOf(self.tab_SQL_Base_connect), QCoreApplication.translate("MainWindow", u"SQL DB", None))
        self.label_tab_age_struct_area_list.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u0442\u0430 \u043b\u043e\u0432\u0430", None))
        self.lbl_export_age_structure_calculation_to_sql.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u0443 ... \u0434\u043b\u044f \u044d\u043a\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.button_age_structure_calculation_print_results.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0432\u0435\u0441\u0442\u0438 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u0440\u0430\u0441\u0447\u0435\u0442\u043e\u0432", None))
        self.button_age_structure_calculation_save_results.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432 sql", None))
        self.label_tab_age_struct_type_list.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434\u044b", None))
        self.label_tab_age_struct_year_list.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434\u0430", None))
        self.label_tab_age_struct_type_list_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u043f\u043e\u043b\u0435 \u0441 \u0432\u0438\u0434\u043e\u043c \u0412\u0411\u0420", None))
        self.age_structure_calculation.setTabText(self.age_structure_calculation.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442 \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u043d\u043e\u0439 \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u044b", None))
        self.age_structure_calculation.setTabText(self.age_structure_calculation.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u043c. \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.age_structure_calculation.setTabText(self.age_structure_calculation.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0411\u0438\u043e \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u0438", None))
        self.age_structure_calculation.setTabText(self.age_structure_calculation.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u043c.\u0440\u0430\u0439\u043e\u043d\u044b", None))
    # retranslateUi

