# -*- coding: utf-8 -*-
from PySide6.QtCore import QRect, QCoreApplication, QMetaObject
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QGridLayout, QTabWidget, QLabel, QLineEdit, QVBoxLayout, QCheckBox, QComboBox, \
    QSizePolicy, QTextEdit, QPushButton, QTableWidget, QGraphicsView, QMenuBar, QStatusBar


class UiMainWindow:
    def __init__(self, main_window):
        # Initialize central widget
        self.central_widget = QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        # !!! may be incorrect place
        main_window.setCentralWidget(self.central_widget)
        main_window.setWindowTitle("Fish")

        # Initialize tab SQL base connect
        self.tab_SQL_Base_connect = QWidget()
        self.tab_SQL_Base_connect.setObjectName("tab_SQL_Base_connect")
        self.tab_age_struct = QWidget()
        self.tab_age_struct.setObjectName("tab_age_struct")

        # Initialize tab_widget + tabs adding
        # tab_widget contains tabs (individually)
        # !!!! rename age_structure_calculation to tab_widget
        self.tab_widget = QTabWidget(self.central_widget)
        self.tab_widget.setObjectName("tab_widget")
        self.tab_widget.setEnabled(True)
        self.tab_widget.addTab(self.tab_SQL_Base_connect, "")
        self.tab_widget.addTab(self.tab_age_struct, "")
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_SQL_Base_connect), "SQL DB")
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_age_struct), "Расчет возрастной структуры")

        # add font type
        font = QFont()
        font.setFamilies(["Times New Roman"])
        font.setPointSize(12)
        font.setBold(True)

        font_connect = QFont()
        font_connect.setFamilies(["Times New Roman"])
        font_connect.setPointSize(12)

        # ui for tab sql db

        # credentials sections
        self.label_DB_Name = QLabel(self.tab_SQL_Base_connect)
        self.label_DB_Name.setObjectName("label_DB_Name")
        self.label_DB_Name.setGeometry(QRect(10, 130, 131, 51))
        self.label_DB_Name.setFont(font)
        self.label_DB_Name.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.label_DB_Name.setMargin(10)
        self.label_DB_Name.setText("DB Name")
        self.lineEdit_DB_Name = QLineEdit(self.tab_SQL_Base_connect)
        self.lineEdit_DB_Name.setObjectName("lineEdit_DB_Name")
        self.lineEdit_DB_Name.setGeometry(QRect(150, 130, 671, 51))

        self.label_SQL_Server_Name = QLabel(self.tab_SQL_Base_connect)
        self.label_SQL_Server_Name.setObjectName("label_SQL_Server_Name")
        self.label_SQL_Server_Name.setGeometry(QRect(10, 70, 131, 51))
        self.label_SQL_Server_Name.setFont(font)
        self.label_SQL_Server_Name.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.label_SQL_Server_Name.setMargin(10)
        self.label_SQL_Server_Name.setText("Server Name")
        self.lineEdit_SQL_Server_Name = QLineEdit(self.tab_SQL_Base_connect)
        self.lineEdit_SQL_Server_Name.setObjectName("lineEdit_SQL_Server_Name")
        self.lineEdit_SQL_Server_Name.setGeometry(QRect(150, 70, 671, 51))

        self.label_SQL_Name = QLabel(self.tab_SQL_Base_connect)
        self.label_SQL_Name.setObjectName("label_SQL_Name")
        self.label_SQL_Name.setGeometry(QRect(10, 10, 131, 51))
        self.label_SQL_Name.setFont(font)
        self.label_SQL_Name.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.label_SQL_Name.setMargin(10)
        self.lineEdit_SQL_Name = QLineEdit(self.tab_SQL_Base_connect)
        self.lineEdit_SQL_Name.setObjectName("lineEdit_SQL_Name")
        self.lineEdit_SQL_Name.setGeometry(QRect(150, 10, 671, 51))
        self.label_SQL_Name.setText("SQL Server")

        # vertical layouts sections (tab SQL DB)
        # !!! rename verticalLayoutWidget_6 to sql_db_vertical_layout_widget_1
        # !!! rename verticalLayout_6 to sql_db_vertical_layout_1
        self.sql_db_vertical_layout_widget_1 = QWidget(self.tab_SQL_Base_connect)
        self.sql_db_vertical_layout_widget_1.setObjectName("sql_db_vertical_layout_widget_1")
        self.sql_db_vertical_layout_widget_1.setGeometry(QRect(20, 240, 381, 155))
        self.sql_db_vertical_layout_1 = QVBoxLayout(self.sql_db_vertical_layout_widget_1)
        self.sql_db_vertical_layout_1.setObjectName("sql_db_vertical_layout_1")
        self.sql_db_vertical_layout_1.setContentsMargins(0, 0, 0, 0)

        # !!! rename checkBox_tab_sql_bioanalis_table_list to sql_db_checkBox_choose_table
        self.sql_db_checkBox_choose_table = QCheckBox(self.sql_db_vertical_layout_widget_1)
        self.sql_db_checkBox_choose_table.setObjectName("sql_db_checkBox_choose_table")
        self.sql_db_checkBox_choose_table.setEnabled(False)
        self.sql_db_checkBox_choose_table.setText("Выберите таблицу биоанализа")

        # !!! rename comboBox_tab_sql_bioanalis_table_list to sql_db_checkBox_choose_bioanalis_table
        self.sql_db_checkBox_choose_bioanalis_table = QComboBox(self.sql_db_vertical_layout_widget_1)
        self.sql_db_checkBox_choose_bioanalis_table.setObjectName("sql_db_checkBox_choose_bioanalis_table")
        self.sql_db_checkBox_choose_bioanalis_table.setEnabled(False)

        # !!! rename label_export_age_structure_calculation_to_sql to label_choose_table_age_struct
        self.label_choose_table_age_struct = QLabel(self.sql_db_vertical_layout_widget_1)
        self.label_choose_table_age_struct.setObjectName("label_choose_table_age_struct")
        self.label_choose_table_age_struct.setText("Выберете таблицу age_struct для экспорта")

        # !!! rename comboBox_export_age_structure_calculation_to_sql to comboBox_choose_table_age_struct
        self.comboBox_choose_table_age_struct = QComboBox(self.sql_db_vertical_layout_widget_1)
        self.comboBox_choose_table_age_struct.setObjectName(
            "comboBox_choose_table_age_struct")
        self.comboBox_choose_table_age_struct.setEnabled(False)

        # !!! rename label_export_age_structure_persent_calculation_to_sql to label_choose_table_age_struct_persent
        self.label_choose_table_age_struct_persent = QLabel(self.sql_db_vertical_layout_widget_1)
        self.label_choose_table_age_struct_persent.setObjectName(
            "label_choose_table_age_struct_persent")
        self.label_choose_table_age_struct_persent.setEnabled(True)
        self.label_choose_table_age_struct_persent.setText("Выберете таблицу age_struct_persent для экспорта")

        # !!! rename comboBox_export_age_structure_persent_calculation_to_sql to
        # comboBox_choose_table_age_struct_persent
        self.comboBox_choose_table_age_struct_persent = QComboBox(self.sql_db_vertical_layout_widget_1)
        self.comboBox_choose_table_age_struct_persent.setObjectName(
            "comboBox_choose_table_age_struct_persent")
        self.comboBox_choose_table_age_struct_persent.setEnabled(False)



        # add widgets to vertical layouts
        self.sql_db_vertical_layout_1.addWidget(self.sql_db_checkBox_choose_table)
        self.sql_db_vertical_layout_1.addWidget(self.sql_db_checkBox_choose_bioanalis_table)
        self.sql_db_vertical_layout_1.addWidget(self.label_choose_table_age_struct)
        self.sql_db_vertical_layout_1.addWidget(self.comboBox_choose_table_age_struct)
        self.sql_db_vertical_layout_1.addWidget(self.label_choose_table_age_struct_persent)
        self.sql_db_vertical_layout_1.addWidget(self.comboBox_choose_table_age_struct_persent)

        # rename checkBox_tab_sql_connect_SQL_DB to checkBox_connect_to_SQL_DB
        self.checkBox_connect_to_SQL_DB = QCheckBox(self.tab_SQL_Base_connect)
        self.checkBox_connect_to_SQL_DB.setObjectName("checkBox_connect_to_SQL_DB")
        self.checkBox_connect_to_SQL_DB.setEnabled(True)
        self.checkBox_connect_to_SQL_DB.setGeometry(QRect(150, 190, 150, 30))
        self.checkBox_connect_to_SQL_DB.setFont(font_connect)
        self.checkBox_connect_to_SQL_DB.setText("Connected")




        # !!! start work with right vertical layouts

        # rename verticalLayoutWidget_3 to sql_db_vertical_layout_widget_2
        # rename verticalLayout_7 to sql_db_vertical_layout_2
        self.sql_db_vertical_layout_widget_2 = QWidget(self.tab_SQL_Base_connect)
        self.sql_db_vertical_layout_widget_2.setObjectName("sql_db_vertical_layout_widget_2")
        self.sql_db_vertical_layout_widget_2.setGeometry(QRect(430, 240, 391, 181))
        self.sql_db_vertical_layout_2 = QVBoxLayout(self.sql_db_vertical_layout_widget_2)
        self.sql_db_vertical_layout_2.setObjectName("sql_db_vertical_layout_2")
        self.sql_db_vertical_layout_2.setContentsMargins(0, 0, 0, 0)

        # rename label_choose_catch_history_table to label_choose_table_catch_history
        self.label_choose_table_catch_history = QLabel(self.sql_db_vertical_layout_widget_2)
        self.label_choose_table_catch_history.setObjectName("label_choose_table_catch_history")
        self.label_choose_table_catch_history.setText("Выберете таблицу истории вылова")

        # rename comboBox_catch_history_table_choose to comboBox_choose_table_catch_history
        self.comboBox_choose_table_catch_history = QComboBox(self.sql_db_vertical_layout_widget_2)
        self.comboBox_choose_table_catch_history.setObjectName("comboBox_choose_table_catch_history")
        self.comboBox_choose_table_catch_history.setEnabled(False)

        # rename label_choose_commercial_register_table to label_choose_table_commercial_register
        self.label_choose_table_commercial_register = QLabel(self.sql_db_vertical_layout_widget_2)
        self.label_choose_table_commercial_register.setObjectName("label_choose_table_commercial_register")
        self.label_choose_table_commercial_register.setText("Выберете таблицу регистр промыслового вылова")

        # rename comboBox_catch_history_commercial_register_choose_table to comboBox_choose_table_commercial_register
        self.comboBox_choose_table_commercial_register = QComboBox(self.sql_db_vertical_layout_widget_2)
        self.comboBox_choose_table_commercial_register.setObjectName("comboBox_choose_table_commercial_register")
        self.comboBox_choose_table_commercial_register.setEnabled(False)

        # rename label_choose_privat_register_table to label_choose_table_privat_register
        self.label_choose_table_privat_register = QLabel(self.sql_db_vertical_layout_widget_2)
        self.label_choose_table_privat_register.setObjectName("label_choose_table_privat_register")
        self.label_choose_table_privat_register.setText("Выберете таблицу регистр непромыслового вылова")

        # rename comboBox_catch_history_privat_register_choose_table to comboBox_choose_table_privat_register
        self.comboBox_choose_table_privat_register = QComboBox(self.sql_db_vertical_layout_widget_2)
        self.comboBox_choose_table_privat_register.setObjectName("comboBox_choose_table_privat_register")
        self.comboBox_choose_table_privat_register.setEnabled(False)

        # rename checkBox_catch_history_save_choose_table to checkBox_save_choose_table_catch_history
        self.checkBox_save_choose_table_catch_history = QCheckBox(self.sql_db_vertical_layout_widget_2)
        self.checkBox_save_choose_table_catch_history.setObjectName(u"checkBox_catch_history_save_choose_table")
        self.checkBox_save_choose_table_catch_history.setEnabled(False)
        self.checkBox_save_choose_table_catch_history.setText("Сохранить выбор таблиц")

        self.sql_db_vertical_layout_2.addWidget(self.label_choose_table_catch_history)
        self.sql_db_vertical_layout_2.addWidget(self.comboBox_choose_table_catch_history)
        self.sql_db_vertical_layout_2.addWidget(self.label_choose_table_commercial_register)
        self.sql_db_vertical_layout_2.addWidget(self.comboBox_choose_table_commercial_register)
        self.sql_db_vertical_layout_2.addWidget(self.label_choose_table_privat_register)
        self.sql_db_vertical_layout_2.addWidget(self.comboBox_choose_table_privat_register)
        self.sql_db_vertical_layout_2.addWidget(self.checkBox_save_choose_table_catch_history)

        # ui for tab age struct

        # Initialize grid
        # rename gridLayout_2 to grid_layout_age_struct
        self.grid_layout = QGridLayout(self.central_widget)
        self.grid_layout.setObjectName("grid_layout")
        self.gridLayoutWidget = QWidget(self.tab_age_struct)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 20, 631, 191))
        self.grid_layout_age_struct = QGridLayout(self.gridLayoutWidget)
        self.grid_layout_age_struct.setObjectName("grid_layout_age_struct")
        self.grid_layout_age_struct.setContentsMargins(0, 0, 0, 0)

        # rename textEdit_age_structure_calculation_for_print_dataframe to textEdit_print_dataframe
        # rename comboBox_tab_age_struct_area_list to comboBox_tab_age_struct_area
        self.textEdit_print_dataframe = QTextEdit(self.tab_age_struct)
        self.textEdit_print_dataframe.setObjectName("textEdit_print_dataframe")
        self.textEdit_print_dataframe.setGeometry(QRect(20, 210, 631, 221))
        self.comboBox_tab_age_struct_area = QComboBox(self.gridLayoutWidget)
        self.comboBox_tab_age_struct_area.setObjectName("comboBox_tab_age_struct_area")
        self.comboBox_tab_age_struct_area.setEnabled(False)

        # add widgets to grid layout
        self.grid_layout_age_struct.addWidget(self.comboBox_tab_age_struct_area, 7, 2, 1, 1)

        self.grid_layout.addWidget(self.tab_widget, 0, 0, 1, 1)

        if not main_window.objectName():
            main_window.setObjectName("main_window")
        main_window.resize(874, 558)

    def setup_ui(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName("main_window")
        main_window.resize(874, 558)

        self.centralwidget = QWidget(main_window)
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
        self.lineEdit_SQL_Name.setGeometry(QRect(150, 10, 671, 51))
        self.lineEdit_SQL_Server_Name = QLineEdit(self.tab_SQL_Base_connect)
        self.lineEdit_SQL_Server_Name.setObjectName(u"lineEdit_SQL_Server_Name")
        self.lineEdit_SQL_Server_Name.setGeometry(QRect(150, 70, 671, 51))
        self.lineEdit_DB_Name = QLineEdit(self.tab_SQL_Base_connect)
        self.lineEdit_DB_Name.setObjectName(u"lineEdit_DB_Name")
        self.lineEdit_DB_Name.setGeometry(QRect(150, 130, 671, 51))
        self.verticalLayoutWidget_6 = QWidget(self.tab_SQL_Base_connect)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(20, 240, 381, 155))
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

        self.label_export_age_structure_calculation_to_sql = QLabel(self.verticalLayoutWidget_6)
        self.label_export_age_structure_calculation_to_sql.setObjectName(u"label_export_age_structure_calculation_to_sql")

        self.verticalLayout_6.addWidget(self.label_export_age_structure_calculation_to_sql)

        self.comboBox_export_age_structure_calculation_to_sql = QComboBox(self.verticalLayoutWidget_6)
        self.comboBox_export_age_structure_calculation_to_sql.setObjectName(u"comboBox_export_age_structure_calculation_to_sql")
        self.comboBox_export_age_structure_calculation_to_sql.setEnabled(False)

        self.verticalLayout_6.addWidget(self.comboBox_export_age_structure_calculation_to_sql)

        self.label_export_age_structure_persent_calculation_to_sql = QLabel(self.verticalLayoutWidget_6)
        self.label_export_age_structure_persent_calculation_to_sql.setObjectName(u"label_export_age_structure_persent_calculation_to_sql")
        self.label_export_age_structure_persent_calculation_to_sql.setEnabled(True)

        self.verticalLayout_6.addWidget(self.label_export_age_structure_persent_calculation_to_sql)

        self.comboBox_export_age_structure_persent_calculation_to_sql = QComboBox(self.verticalLayoutWidget_6)
        self.comboBox_export_age_structure_persent_calculation_to_sql.setObjectName(u"comboBox_export_age_structure_persent_calculation_to_sql")
        self.comboBox_export_age_structure_persent_calculation_to_sql.setEnabled(False)

        self.verticalLayout_6.addWidget(self.comboBox_export_age_structure_persent_calculation_to_sql)

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
        self.verticalLayoutWidget_3 = QWidget(self.tab_SQL_Base_connect)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(430, 240, 391, 181))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_choose_catch_history_table = QLabel(self.verticalLayoutWidget_3)
        self.label_choose_catch_history_table.setObjectName(u"label_choose_catch_history_table")

        self.verticalLayout_7.addWidget(self.label_choose_catch_history_table)

        self.comboBox_catch_history_table_choose = QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_catch_history_table_choose.setObjectName(u"comboBox_catch_history_table_choose")
        self.comboBox_catch_history_table_choose.setEnabled(False)

        self.verticalLayout_7.addWidget(self.comboBox_catch_history_table_choose)

        self.label_choose_commercial_register_table = QLabel(self.verticalLayoutWidget_3)
        self.label_choose_commercial_register_table.setObjectName(u"label_choose_commercial_register_table")

        self.verticalLayout_7.addWidget(self.label_choose_commercial_register_table)

        self.comboBox_catch_history_commercial_register_choose_table = QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_catch_history_commercial_register_choose_table.setObjectName(u"comboBox_catch_history_commercial_register_choose_table")
        self.comboBox_catch_history_commercial_register_choose_table.setEnabled(False)

        self.verticalLayout_7.addWidget(self.comboBox_catch_history_commercial_register_choose_table)

        self.label_choose_privat_register_table = QLabel(self.verticalLayoutWidget_3)
        self.label_choose_privat_register_table.setObjectName(u"label_choose_privat_register_table")

        self.verticalLayout_7.addWidget(self.label_choose_privat_register_table)

        self.comboBox_catch_history_privat_register_choose_table = QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_catch_history_privat_register_choose_table.setObjectName(u"comboBox_catch_history_privat_register_choose_table")
        self.comboBox_catch_history_privat_register_choose_table.setEnabled(False)

        self.verticalLayout_7.addWidget(self.comboBox_catch_history_privat_register_choose_table)

        self.checkBox_catch_history_save_choose_table = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_catch_history_save_choose_table.setObjectName(u"checkBox_catch_history_save_choose_table")
        self.checkBox_catch_history_save_choose_table.setEnabled(False)

        self.verticalLayout_7.addWidget(self.checkBox_catch_history_save_choose_table)

        self.age_structure_calculation.addTab(self.tab_SQL_Base_connect, "")
        self.tab_age_struct = QWidget()
        self.tab_age_struct.setObjectName(u"tab_age_struct")
        self.tab_age_struct.setEnabled(True)
        self.textEdit_age_structure_calculation_for_print_dataframe = QTextEdit(self.tab_age_struct)
        self.textEdit_age_structure_calculation_for_print_dataframe.setObjectName(u"textEdit_age_structure_calculation_for_print_dataframe")
        self.textEdit_age_structure_calculation_for_print_dataframe.setGeometry(QRect(20, 210, 631, 221))
        self.gridLayoutWidget = QWidget(self.tab_age_struct)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 20, 631, 191))
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
        self.label_tab_age_struct_type_list = QLabel(self.gridLayoutWidget)
        self.label_tab_age_struct_type_list.setObjectName(u"label_tab_age_struct_type_list")

        self.verticalLayout.addWidget(self.label_tab_age_struct_type_list)

        self.comboBox_tab_age_struct_type_list_choose_column = QComboBox(self.gridLayoutWidget)
        self.comboBox_tab_age_struct_type_list_choose_column.setObjectName(u"comboBox_tab_age_struct_type_list_choose_column")
        self.comboBox_tab_age_struct_type_list_choose_column.setEnabled(False)

        self.verticalLayout.addWidget(self.comboBox_tab_age_struct_type_list_choose_column)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_tab_age_struct_area_list = QLabel(self.gridLayoutWidget)
        self.label_tab_age_struct_area_list.setObjectName(u"label_tab_age_struct_area_list")

        self.verticalLayout_3.addWidget(self.label_tab_age_struct_area_list)

        self.comboBox_tab_age_struct_area_list_choose_column = QComboBox(self.gridLayoutWidget)
        self.comboBox_tab_age_struct_area_list_choose_column.setObjectName(u"comboBox_tab_age_struct_area_list_choose_column")
        self.comboBox_tab_age_struct_area_list_choose_column.setEnabled(False)

        self.verticalLayout_3.addWidget(self.comboBox_tab_age_struct_area_list_choose_column)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 1, 2, 1, 1)

        self.comboBox_tab_age_struct_year_list = QComboBox(self.gridLayoutWidget)
        self.comboBox_tab_age_struct_year_list.setObjectName(u"comboBox_tab_age_struct_year_list")
        self.comboBox_tab_age_struct_year_list.setEnabled(False)

        self.gridLayout_2.addWidget(self.comboBox_tab_age_struct_year_list, 7, 1, 1, 1)

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
        self.label_tab_age_struct_year_list = QLabel(self.gridLayoutWidget)
        self.label_tab_age_struct_year_list.setObjectName(u"label_tab_age_struct_year_list")

        self.verticalLayout_5.addWidget(self.label_tab_age_struct_year_list)

        self.comboBox_tab_age_struct_year_list_choose_column = QComboBox(self.gridLayoutWidget)
        self.comboBox_tab_age_struct_year_list_choose_column.setObjectName(u"comboBox_tab_age_struct_year_list_choose_column")
        self.comboBox_tab_age_struct_year_list_choose_column.setEnabled(False)

        self.verticalLayout_5.addWidget(self.comboBox_tab_age_struct_year_list_choose_column)


        self.gridLayout_2.addLayout(self.verticalLayout_5, 1, 1, 1, 1)

        self.checkBox_tab_age_struct_type_list_choose_column = QCheckBox(self.gridLayoutWidget)
        self.checkBox_tab_age_struct_type_list_choose_column.setObjectName(u"checkBox_tab_age_struct_type_list_choose_column")
        self.checkBox_tab_age_struct_type_list_choose_column.setEnabled(False)

        self.gridLayout_2.addWidget(self.checkBox_tab_age_struct_type_list_choose_column, 6, 0, 1, 1)

        self.checkBox_tab_age_struct_year_list_choose_column = QCheckBox(self.gridLayoutWidget)
        self.checkBox_tab_age_struct_year_list_choose_column.setObjectName(u"checkBox_tab_age_struct_year_list_choose_column")
        self.checkBox_tab_age_struct_year_list_choose_column.setEnabled(False)

        self.gridLayout_2.addWidget(self.checkBox_tab_age_struct_year_list_choose_column, 6, 1, 1, 1)

        self.checkBox_tab_age_struct_area_list_choose_column = QCheckBox(self.gridLayoutWidget)
        self.checkBox_tab_age_struct_area_list_choose_column.setObjectName(u"checkBox_tab_age_struct_area_list_choose_column")
        self.checkBox_tab_age_struct_area_list_choose_column.setEnabled(False)

        self.gridLayout_2.addWidget(self.checkBox_tab_age_struct_area_list_choose_column, 6, 2, 1, 1)

        self.pushButton_export_age_structure_calculation_to_sql = QPushButton(self.tab_age_struct)
        self.pushButton_export_age_structure_calculation_to_sql.setObjectName(u"pushButton_export_age_structure_calculation_to_sql")
        self.pushButton_export_age_structure_calculation_to_sql.setEnabled(False)
        self.pushButton_export_age_structure_calculation_to_sql.setGeometry(QRect(690, 170, 111, 28))
        self.pushButton_load_age_structure_from_sql = QPushButton(self.tab_age_struct)
        self.pushButton_load_age_structure_from_sql.setObjectName(u"pushButton_load_age_structure_from_sql")
        self.pushButton_load_age_structure_from_sql.setEnabled(False)
        self.pushButton_load_age_structure_from_sql.setGeometry(QRect(690, 200, 111, 28))
        self.age_structure_calculation.addTab(self.tab_age_struct, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayoutWidget_2 = QWidget(self.tab_4)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 441, 231))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox_catch_history_choose_type = QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_catch_history_choose_type.setObjectName(u"checkBox_catch_history_choose_type")
        self.checkBox_catch_history_choose_type.setEnabled(False)

        self.verticalLayout_2.addWidget(self.checkBox_catch_history_choose_type)

        self.comboBox_catch_history_choose_type = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_catch_history_choose_type.setObjectName(u"comboBox_catch_history_choose_type")
        self.comboBox_catch_history_choose_type.setEnabled(False)

        self.verticalLayout_2.addWidget(self.comboBox_catch_history_choose_type)

        self.tableWidget_catch_history_table_of_type_by_year = QTableWidget(self.gridLayoutWidget_2)
        self.tableWidget_catch_history_table_of_type_by_year.setObjectName(u"tableWidget_catch_history_table_of_type_by_year")
        self.tableWidget_catch_history_table_of_type_by_year.setEnabled(False)

        self.verticalLayout_2.addWidget(self.tableWidget_catch_history_table_of_type_by_year)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 2)

        self.verticalLayoutWidget_2 = QWidget(self.tab_4)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(460, 10, 381, 231))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.checkBox_catch_history_choose_year = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_catch_history_choose_year.setObjectName(u"checkBox_catch_history_choose_year")
        self.checkBox_catch_history_choose_year.setEnabled(False)

        self.verticalLayout_4.addWidget(self.checkBox_catch_history_choose_year)

        self.comboBox_catch_history_choose_year = QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_catch_history_choose_year.setObjectName(u"comboBox_catch_history_choose_year")
        self.comboBox_catch_history_choose_year.setEnabled(False)

        self.verticalLayout_4.addWidget(self.comboBox_catch_history_choose_year)

        self.tableWidget_catch_history_table_of_type_of_the_year = QTableWidget(self.verticalLayoutWidget_2)
        self.tableWidget_catch_history_table_of_type_of_the_year.setObjectName(u"tableWidget_catch_history_table_of_type_of_the_year")
        self.tableWidget_catch_history_table_of_type_of_the_year.setEnabled(False)

        self.verticalLayout_4.addWidget(self.tableWidget_catch_history_table_of_type_of_the_year)

        self.pushButton_export_catch_history_to_sql = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_export_catch_history_to_sql.setObjectName(u"pushButton_export_catch_history_to_sql")
        self.pushButton_export_catch_history_to_sql.setEnabled(False)

        self.verticalLayout_4.addWidget(self.pushButton_export_catch_history_to_sql)

        self.graphicsView_catch_history_graph_of_type_by_year = QGraphicsView(self.tab_4)
        self.graphicsView_catch_history_graph_of_type_by_year.setObjectName(u"graphicsView_catch_history_graph_of_type_by_year")
        self.graphicsView_catch_history_graph_of_type_by_year.setGeometry(QRect(10, 250, 831, 201))
        self.age_structure_calculation.addTab(self.tab_4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.age_structure_calculation.addTab(self.tab_2, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.age_structure_calculation.addTab(self.tab_5, "")

        self.gridLayout.addWidget(self.age_structure_calculation, 0, 0, 1, 1)

        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 874, 26))
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)

        self.age_structure_calculation.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_DB_Name.setText(QCoreApplication.translate("MainWindow", u"DB Name", None))
        self.label_SQL_Server_Name.setText(QCoreApplication.translate("MainWindow", u"Server Name", None))
        self.label_SQL_Name.setText(QCoreApplication.translate("MainWindow", u"SQL Server", None))
        self.checkBox_tab_sql_bioanalis_table_list.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u0431\u0438\u043e\u0430\u043d\u0430\u043b\u0438\u0437\u0430:", None))
        self.label_export_age_structure_calculation_to_sql.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u0443 age_struct \u0434\u043b\u044f \u044d\u043a\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.label_export_age_structure_persent_calculation_to_sql.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u0443 age_struct_persent \u0434\u043b\u044f \u044d\u043a\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.checkBox_tab_sql_connect_SQL_DB.setText(QCoreApplication.translate("MainWindow", u"Connected", None))
        self.label_choose_catch_history_table.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u0438\u0441\u0442\u043e\u0440\u0438\u0438 \u0432\u044b\u043b\u043e\u0432\u0430", None))
        self.label_choose_commercial_register_table.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u0440\u0435\u0433\u0438\u0441\u0442\u0440 \u043f\u0440\u043e\u043c\u044b\u0441\u043b\u043e\u0432\u043e\u0433\u043e \u0432\u044b\u043b\u043e\u0432\u0430", None))
        self.label_choose_privat_register_table.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u0440\u0435\u0433\u0438\u0441\u0442\u0440 \u043d\u0435\u043f\u0440\u043e\u043c\u044b\u0441\u043b\u043e\u0432\u043e\u0433\u043e \u0432\u044b\u043b\u043e\u0432\u0430", None))
        self.checkBox_catch_history_save_choose_table.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432\u044b\u0431\u043e\u0440 \u0442\u0430\u0431\u043b\u0438\u0446", None))
        self.age_structure_calculation.setTabText(self.age_structure_calculation.indexOf(self.tab_SQL_Base_connect), QCoreApplication.translate("MainWindow", u"SQL DB", None))
        self.pushButton_age_struct_choose_column.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0441\u0442\u043e\u043b\u0431\u0446\u043e\u0432", None))
        self.label_tab_age_struct_type_list.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434\u044b", None))
        self.label_tab_age_struct_area_list.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u0442\u0430 \u043b\u043e\u0432\u0430", None))
        self.pushButton_age_struct_choose_values.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439", None))
        self.label_tab_age_struct_year_list.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434\u0430", None))
        self.checkBox_tab_age_struct_type_list_choose_column.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0441\u0442\u043e\u043b\u0431\u0446\u0430 \u0441 \u0432\u0438\u0434\u043e\u043c", None))
        self.checkBox_tab_age_struct_year_list_choose_column.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0441\u0442\u043e\u043b\u0431\u0446\u0430 \u0441 \u0433\u043e\u0434\u0430\u043c\u0438 \u043b\u043e\u0432\u0430", None))
        self.checkBox_tab_age_struct_area_list_choose_column.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0441\u0442\u043e\u043b\u0431\u0446\u0430 \u0441 \u043c\u0435\u0441\u0442\u0430\u043c\u0438 \u043b\u043e\u0432\u0430", None))
        self.pushButton_export_age_structure_calculation_to_sql.setText(QCoreApplication.translate("MainWindow", u"Save to SQL", None))
        self.pushButton_load_age_structure_from_sql.setText(QCoreApplication.translate("MainWindow", u"Load from SQL", None))
        self.age_structure_calculation.setTabText(self.age_structure_calculation.indexOf(self.tab_age_struct), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442 \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u043d\u043e\u0439 \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u044b", None))
        self.checkBox_catch_history_choose_type.setText(QCoreApplication.translate("MainWindow", u"\u0432\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0432\u0438\u0434", None))
        self.checkBox_catch_history_choose_year.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0433\u043e\u0434\u0430", None))
        self.pushButton_export_catch_history_to_sql.setText(QCoreApplication.translate("MainWindow", u"Save to SQL", None))
        self.age_structure_calculation.setTabText(self.age_structure_calculation.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u043c. \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.age_structure_calculation.setTabText(self.age_structure_calculation.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0411\u0438\u043e \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u0438", None))
        self.age_structure_calculation.setTabText(self.age_structure_calculation.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u043c.\u0440\u0430\u0439\u043e\u043d\u044b", None))
    # retranslateUi