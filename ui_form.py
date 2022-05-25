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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
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
        self.age_structure_calculation.setEnabled(True)
        self.tab_SQL_Base_connect = QWidget()
        self.tab_SQL_Base_connect.setObjectName(u"tab_SQL_Base_connect")
        self.label_DB_Name = QLabel(self.tab_SQL_Base_connect)
        self.label_DB_Name.setObjectName(u"label_DB_Name")
        self.label_DB_Name.setGeometry(QRect(10, 130, 131, 51))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_DB_Name.setFont(font)
        self.label_DB_Name.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.label_DB_Name.setMargin(10)
        self.label_SQL_Server_Name = QLabel(self.tab_SQL_Base_connect)
        self.label_SQL_Server_Name.setObjectName(u"label_SQL_Server_Name")
        self.label_SQL_Server_Name.setGeometry(QRect(10, 70, 131, 51))
        self.label_SQL_Server_Name.setFont(font)
        self.label_SQL_Server_Name.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.label_SQL_Server_Name.setMargin(10)
        self.label_SQL_Name = QLabel(self.tab_SQL_Base_connect)
        self.label_SQL_Name.setObjectName(u"label_SQL_Name")
        self.label_SQL_Name.setGeometry(QRect(10, 10, 131, 51))
        self.label_SQL_Name.setFont(font)
        self.label_SQL_Name.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.label_SQL_Name.setMargin(10)
        self.lineEdit_SQL_Name = QLineEdit(self.tab_SQL_Base_connect)
        self.lineEdit_SQL_Name.setObjectName(u"lineEdit_SQL_Name")
        self.lineEdit_SQL_Name.setGeometry(QRect(150, 10, 591, 51))
        self.lineEdit_SQL_Server_Name = QLineEdit(self.tab_SQL_Base_connect)
        self.lineEdit_SQL_Server_Name.setObjectName(u"lineEdit_SQL_Server_Name")
        self.lineEdit_SQL_Server_Name.setGeometry(QRect(150, 70, 591, 51))
        self.lineEdit_DB_Name = QLineEdit(self.tab_SQL_Base_connect)
        self.lineEdit_DB_Name.setObjectName(u"lineEdit_DB_Name")
        self.lineEdit_DB_Name.setGeometry(QRect(150, 130, 591, 51))
        self.verticalLayoutWidget_6 = QWidget(self.tab_SQL_Base_connect)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(20, 240, 381, 61))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.checkBox_tab_sql_bioanalis_table_list = QCheckBox(self.verticalLayoutWidget_6)
        self.checkBox_tab_sql_bioanalis_table_list.setObjectName(u"checkBox_tab_sql_bioanalis_table_list")
        self.checkBox_tab_sql_bioanalis_table_list.setEnabled(False)

        self.verticalLayout_6.addWidget(self.checkBox_tab_sql_bioanalis_table_list)

        self.comboBox_tab_sql_bioanalis_table_list = QComboBox(self.verticalLayoutWidget_6)
        self.comboBox_tab_sql_bioanalis_table_list.setObjectName(u"comboBox_tab_sql_bioanalis_table_list")
        self.comboBox_tab_sql_bioanalis_table_list.setEnabled(False)

        self.verticalLayout_6.addWidget(self.comboBox_tab_sql_bioanalis_table_list)

        self.pushButton_sql_bioanalis_choose_table = QPushButton(self.tab_SQL_Base_connect)
        self.pushButton_sql_bioanalis_choose_table.setObjectName(u"pushButton_sql_bioanalis_choose_table")
        self.pushButton_sql_bioanalis_choose_table.setEnabled(False)
        self.pushButton_sql_bioanalis_choose_table.setGeometry(QRect(490, 290, 379, 28))
        self.checkBox_tab_sql_connect_SQL_DB = QCheckBox(self.tab_SQL_Base_connect)
        self.checkBox_tab_sql_connect_SQL_DB.setObjectName(u"checkBox_tab_sql_connect_SQL_DB")
        self.checkBox_tab_sql_connect_SQL_DB.setEnabled(True)
        self.checkBox_tab_sql_connect_SQL_DB.setGeometry(QRect(150, 190, 150, 30))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_tab_sql_connect_SQL_DB.sizePolicy().hasHeightForWidth())
        self.checkBox_tab_sql_connect_SQL_DB.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        self.checkBox_tab_sql_connect_SQL_DB.setFont(font1)
        self.checkBox_tab_sql_connect_SQL_DB.setChecked(False)
        self.age_structure_calculation.addTab(self.tab_SQL_Base_connect, "")
        self.tab_age_struct = QWidget()
        self.tab_age_struct.setObjectName(u"tab_age_struct")
        self.tab_age_struct.setEnabled(True)
        self.verticalLayoutWidget_3 = QWidget(self.tab_age_struct)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(660, 20, 451, 181))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_export_age_structure_calculation_to_sql = QLabel(self.verticalLayoutWidget_3)
        self.label_export_age_structure_calculation_to_sql.setObjectName(u"label_export_age_structure_calculation_to_sql")

        self.verticalLayout_4.addWidget(self.label_export_age_structure_calculation_to_sql)

        self.comboBox_export_age_structure_calculation_to_sql = QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_export_age_structure_calculation_to_sql.setObjectName(u"comboBox_export_age_structure_calculation_to_sql")
        self.comboBox_export_age_structure_calculation_to_sql.setEnabled(False)

        self.verticalLayout_4.addWidget(self.comboBox_export_age_structure_calculation_to_sql)

        self.label_export_age_structure_persent_calculation_to_sql = QLabel(self.verticalLayoutWidget_3)
        self.label_export_age_structure_persent_calculation_to_sql.setObjectName(u"label_export_age_structure_persent_calculation_to_sql")
        self.label_export_age_structure_persent_calculation_to_sql.setEnabled(True)

        self.verticalLayout_4.addWidget(self.label_export_age_structure_persent_calculation_to_sql)

        self.comboBox_export_age_structure_persent_calculation_to_sql = QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_export_age_structure_persent_calculation_to_sql.setObjectName(u"comboBox_export_age_structure_persent_calculation_to_sql")
        self.comboBox_export_age_structure_persent_calculation_to_sql.setEnabled(False)

        self.verticalLayout_4.addWidget(self.comboBox_export_age_structure_persent_calculation_to_sql)

        self.pushButton_export_age_structure_calculation_to_sql = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_export_age_structure_calculation_to_sql.setObjectName(u"pushButton_export_age_structure_calculation_to_sql")
        self.pushButton_export_age_structure_calculation_to_sql.setEnabled(False)

        self.verticalLayout_4.addWidget(self.pushButton_export_age_structure_calculation_to_sql)

        self.textEdit_age_structure_calculation_for_print_dataframe = QTextEdit(self.tab_age_struct)
        self.textEdit_age_structure_calculation_for_print_dataframe.setObjectName(u"textEdit_age_structure_calculation_for_print_dataframe")
        self.textEdit_age_structure_calculation_for_print_dataframe.setGeometry(QRect(20, 210, 631, 521))
        self.gridLayoutWidget = QWidget(self.tab_age_struct)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 20, 631, 181))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.comboBox_tab_age_struct_area_list = QComboBox(self.gridLayoutWidget)
        self.comboBox_tab_age_struct_area_list.setObjectName(u"comboBox_tab_age_struct_area_list")
        self.comboBox_tab_age_struct_area_list.setEnabled(False)

        self.gridLayout_2.addWidget(self.comboBox_tab_age_struct_area_list, 7, 2, 1, 1)

        self.pushButton_age_struct_choose_column = QPushButton(self.gridLayoutWidget)
        self.pushButton_age_struct_choose_column.setObjectName(u"pushButton_age_struct_choose_column")
        self.pushButton_age_struct_choose_column.setEnabled(False)

        self.gridLayout_2.addWidget(self.pushButton_age_struct_choose_column, 2, 0, 1, 3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_tab_age_struct_type_list_choose_column = QCheckBox(self.gridLayoutWidget)
        self.checkBox_tab_age_struct_type_list_choose_column.setObjectName(u"checkBox_tab_age_struct_type_list_choose_column")
        self.checkBox_tab_age_struct_type_list_choose_column.setEnabled(False)

        self.verticalLayout.addWidget(self.checkBox_tab_age_struct_type_list_choose_column)

        self.comboBox_tab_age_struct_type_list_choose_column = QComboBox(self.gridLayoutWidget)
        self.comboBox_tab_age_struct_type_list_choose_column.setObjectName(u"comboBox_tab_age_struct_type_list_choose_column")
        self.comboBox_tab_age_struct_type_list_choose_column.setEnabled(False)

        self.verticalLayout.addWidget(self.comboBox_tab_age_struct_type_list_choose_column)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_tab_age_struct_area_list_choose_column = QCheckBox(self.gridLayoutWidget)
        self.checkBox_tab_age_struct_area_list_choose_column.setObjectName(u"checkBox_tab_age_struct_area_list_choose_column")
        self.checkBox_tab_age_struct_area_list_choose_column.setEnabled(False)

        self.verticalLayout_3.addWidget(self.checkBox_tab_age_struct_area_list_choose_column)

        self.comboBox_tab_age_struct_area_list_choose_column = QComboBox(self.gridLayoutWidget)
        self.comboBox_tab_age_struct_area_list_choose_column.setObjectName(u"comboBox_tab_age_struct_area_list_choose_column")
        self.comboBox_tab_age_struct_area_list_choose_column.setEnabled(False)

        self.verticalLayout_3.addWidget(self.comboBox_tab_age_struct_area_list_choose_column)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 1, 2, 1, 1)

        self.label_tab_age_struct_type_list = QLabel(self.gridLayoutWidget)
        self.label_tab_age_struct_type_list.setObjectName(u"label_tab_age_struct_type_list")

        self.gridLayout_2.addWidget(self.label_tab_age_struct_type_list, 6, 0, 1, 1)

        self.label_tab_age_struct_year_list = QLabel(self.gridLayoutWidget)
        self.label_tab_age_struct_year_list.setObjectName(u"label_tab_age_struct_year_list")

        self.gridLayout_2.addWidget(self.label_tab_age_struct_year_list, 6, 1, 1, 1)

        self.comboBox_tab_age_struct_year_list = QComboBox(self.gridLayoutWidget)
        self.comboBox_tab_age_struct_year_list.setObjectName(u"comboBox_tab_age_struct_year_list")
        self.comboBox_tab_age_struct_year_list.setEnabled(False)

        self.gridLayout_2.addWidget(self.comboBox_tab_age_struct_year_list, 7, 1, 1, 1)

        self.label_tab_age_struct_area_list = QLabel(self.gridLayoutWidget)
        self.label_tab_age_struct_area_list.setObjectName(u"label_tab_age_struct_area_list")

        self.gridLayout_2.addWidget(self.label_tab_age_struct_area_list, 6, 2, 1, 1)

        self.comboBox_tab_age_struct_type_list = QComboBox(self.gridLayoutWidget)
        self.comboBox_tab_age_struct_type_list.setObjectName(u"comboBox_tab_age_struct_type_list")
        self.comboBox_tab_age_struct_type_list.setEnabled(False)

        self.gridLayout_2.addWidget(self.comboBox_tab_age_struct_type_list, 7, 0, 1, 1)

        self.pushButton_age_struct_choose_values = QPushButton(self.gridLayoutWidget)
        self.pushButton_age_struct_choose_values.setObjectName(u"pushButton_age_struct_choose_values")
        self.pushButton_age_struct_choose_values.setEnabled(False)

        self.gridLayout_2.addWidget(self.pushButton_age_struct_choose_values, 8, 0, 1, 3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.checkBox_tab_age_struct_year_list_choose_column = QCheckBox(self.gridLayoutWidget)
        self.checkBox_tab_age_struct_year_list_choose_column.setObjectName(u"checkBox_tab_age_struct_year_list_choose_column")
        self.checkBox_tab_age_struct_year_list_choose_column.setEnabled(False)

        self.verticalLayout_5.addWidget(self.checkBox_tab_age_struct_year_list_choose_column)

        self.comboBox_tab_age_struct_year_list_choose_column = QComboBox(self.gridLayoutWidget)
        self.comboBox_tab_age_struct_year_list_choose_column.setObjectName(u"comboBox_tab_age_struct_year_list_choose_column")
        self.comboBox_tab_age_struct_year_list_choose_column.setEnabled(False)

        self.verticalLayout_5.addWidget(self.comboBox_tab_age_struct_year_list_choose_column)


        self.gridLayout_2.addLayout(self.verticalLayout_5, 1, 1, 1, 1)

        self.age_structure_calculation.addTab(self.tab_age_struct, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.age_structure_calculation.addTab(self.tab_4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.age_structure_calculation.addTab(self.tab_2, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.age_structure_calculation.addTab(self.tab_5, "")

        self.gridLayout.addWidget(self.age_structure_calculation, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1160, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.age_structure_calculation.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_DB_Name.setText(QCoreApplication.translate("MainWindow", u"DB Name", None))
        self.label_SQL_Server_Name.setText(QCoreApplication.translate("MainWindow", u"Server Name", None))
        self.label_SQL_Name.setText(QCoreApplication.translate("MainWindow", u"SQL Server", None))
        self.checkBox_tab_sql_bioanalis_table_list.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u0431\u0438\u043e\u0430\u043d\u0430\u043b\u0438\u0437\u0430:", None))
        self.pushButton_sql_bioanalis_choose_table.setText(QCoreApplication.translate("MainWindow", u"choose table", None))
        self.checkBox_tab_sql_connect_SQL_DB.setText(QCoreApplication.translate("MainWindow", u"Connected", None))
        self.age_structure_calculation.setTabText(self.age_structure_calculation.indexOf(self.tab_SQL_Base_connect), QCoreApplication.translate("MainWindow", u"SQL DB", None))
        self.label_export_age_structure_calculation_to_sql.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u0443 age_struct \u0434\u043b\u044f \u044d\u043a\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.label_export_age_structure_persent_calculation_to_sql.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u0443 age_struct_persent \u0434\u043b\u044f \u044d\u043a\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.pushButton_export_age_structure_calculation_to_sql.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_age_struct_choose_column.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0441\u0442\u043e\u043b\u0431\u0446\u043e\u0432", None))
        self.checkBox_tab_age_struct_type_list_choose_column.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0441\u0442\u043e\u043b\u0431\u0446\u0430 \u0441 \u0432\u0438\u0434\u043e\u043c", None))
        self.checkBox_tab_age_struct_area_list_choose_column.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0441\u0442\u043e\u043b\u0431\u0446\u0430 \u0441 \u043c\u0435\u0441\u0442\u0430\u043c\u0438 \u043b\u043e\u0432\u0430", None))
        self.label_tab_age_struct_type_list.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434\u044b", None))
        self.label_tab_age_struct_year_list.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434\u0430", None))
        self.label_tab_age_struct_area_list.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u0442\u0430 \u043b\u043e\u0432\u0430", None))
        self.pushButton_age_struct_choose_values.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439", None))
        self.checkBox_tab_age_struct_year_list_choose_column.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0441\u0442\u043e\u043b\u0431\u0446\u0430 \u0441 \u0433\u043e\u0434\u0430\u043c\u0438 \u043b\u043e\u0432\u0430", None))
        self.age_structure_calculation.setTabText(self.age_structure_calculation.indexOf(self.tab_age_struct), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442 \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u043d\u043e\u0439 \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u044b", None))
        self.age_structure_calculation.setTabText(self.age_structure_calculation.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u043c. \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.age_structure_calculation.setTabText(self.age_structure_calculation.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0411\u0438\u043e \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u0438", None))
        self.age_structure_calculation.setTabText(self.age_structure_calculation.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u043c.\u0440\u0430\u0439\u043e\u043d\u044b", None))
    # retranslateUi

