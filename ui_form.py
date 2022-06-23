# -*- coding: utf-8 -*-
from PySide6.QtCore import QRect
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget, QGridLayout, QTabWidget, QLabel, QLineEdit, QVBoxLayout, QCheckBox,
    QComboBox, QTextEdit, QPushButton, QTableWidget, QGraphicsView
)


class UiMainWindow:
    def __init__(self, main_window):
        # Initialize central widget
        self.central_widget = QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        # !!! may be incorrect place
        main_window.setCentralWidget(self.central_widget)
        main_window.setWindowTitle("Fish")

        # Initialize tabs
        # rename tab_4 to catch_statistics
        self.tab_SQL_Base_connect = QWidget()
        self.tab_SQL_Base_connect.setObjectName("tab_SQL_Base_connect")
        self.tab_age_struct = QWidget()
        self.tab_age_struct.setObjectName("tab_age_struct")
        self.tab_catch_history = QWidget()
        self.tab_catch_history.setObjectName("catch_statistics")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName("tab_5")

        # Initialize tab_widget + tabs adding
        # tab_widget contains tabs (individually)
        # !!!! rename age_structure_calculation to tab_widget
        self.tab_widget = QTabWidget(self.central_widget)
        self.tab_widget.setObjectName("tab_widget")
        self.tab_widget.setEnabled(True)
        self.tab_widget.addTab(self.tab_SQL_Base_connect, "")
        self.tab_widget.addTab(self.tab_age_struct, "")
        self.tab_widget.addTab(self.tab_catch_history, "")
        self.tab_widget.addTab(self.tab_4, "")
        self.tab_widget.addTab(self.tab_5, "")
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_SQL_Base_connect), "SQL DB")
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_age_struct), "Расчет возрастной структуры")
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_catch_history), "Пром. история")
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_4), "tab 4")
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_5), "tab 5")

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
        # ???
        # sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.checkBox_connect_to_SQL_DB.sizePolicy().hasHeightForWidth())
        # self.checkBox_connect_to_SQL_DB.setSizePolicy(sizePolicy)

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
        self.gridLayoutWidget = QWidget(self.tab_age_struct)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 20, 631, 191))
        self.grid_layout_age_struct = QGridLayout(self.gridLayoutWidget)
        self.grid_layout_age_struct.setObjectName("grid_layout_age_struct")
        self.grid_layout_age_struct.setContentsMargins(0, 0, 0, 0)

        # Initialize widgets

        # vertical layouts section

        # vl types
        # rename label_tab_age_struct_type_list to label_tab_age_struct_type
        # rename comboBox_tab_age_struct_type_list_choose_column to comboBox_tab_age_struct_type_choose_column
        self.label_tab_age_struct_type = QLabel(self.gridLayoutWidget)
        self.label_tab_age_struct_type.setObjectName(
            "label_tab_age_struct_type")
        self.label_tab_age_struct_type.setText("Виды")
        self.comboBox_tab_age_struct_type_choose_column = QComboBox(self.gridLayoutWidget)
        self.comboBox_tab_age_struct_type_choose_column.setObjectName(
            "comboBox_tab_age_struct_type_choose_column")
        self.comboBox_tab_age_struct_type_choose_column.setEnabled(False)

        # rename verticalLayout to verticalLayout_types
        self.verticalLayout_types = QVBoxLayout()
        self.verticalLayout_types.setObjectName("verticalLayout_types")
        self.verticalLayout_types.addWidget(self.label_tab_age_struct_type)
        self.verticalLayout_types.addWidget(self.comboBox_tab_age_struct_type_choose_column)

        # vl years
        # rename label_tab_age_struct_year_list to label_tab_age_struct_year
        # rename comboBox_tab_age_struct_year_list_choose_column to comboBox_tab_age_struct_year_choose_column
        self.label_tab_age_struct_year = QLabel(self.gridLayoutWidget)
        self.label_tab_age_struct_year.setObjectName("label_tab_age_struct_year")
        self.label_tab_age_struct_year.setText("Года")
        self.comboBox_tab_age_struct_year_choose_column = QComboBox(self.gridLayoutWidget)
        self.comboBox_tab_age_struct_year_choose_column.setObjectName(
            "comboBox_tab_age_struct_year_choose_column")
        self.comboBox_tab_age_struct_year_choose_column.setEnabled(False)

        # rename verticalLayout_5 to verticalLayout_years
        self.verticalLayout_years = QVBoxLayout()
        self.verticalLayout_years.setObjectName("verticalLayout_years")
        self.verticalLayout_years.addWidget(self.label_tab_age_struct_year)
        self.verticalLayout_years.addWidget(self.comboBox_tab_age_struct_year_choose_column)

        # vl areas
        # rename label_tab_age_struct_area_list to label_tab_age_struct_area
        # rename comboBox_tab_age_struct_area_list_choose_column to comboBox_tab_age_struct_area_e_column
        self.label_tab_age_struct_area = QLabel(self.gridLayoutWidget)
        self.label_tab_age_struct_area.setObjectName("label_tab_age_struct_area")
        self.label_tab_age_struct_area.setText("Места лова")
        self.comboBox_tab_age_struct_area_choose_column = QComboBox(self.gridLayoutWidget)
        self.comboBox_tab_age_struct_area_choose_column.setObjectName(
            "comboBox_tab_age_struct_area_choose_column")
        self.comboBox_tab_age_struct_area_choose_column.setEnabled(False)

        # rename verticalLayout_3 to verticalLayout_areas
        self.verticalLayout_areas = QVBoxLayout()
        self.verticalLayout_areas.setObjectName("verticalLayout_areas")
        self.verticalLayout_areas.addWidget(self.label_tab_age_struct_area)
        self.verticalLayout_areas.addWidget(self.comboBox_tab_age_struct_area_choose_column)

        # Button choose column
        self.pushButton_age_struct_choose_column = QPushButton(self.gridLayoutWidget)
        self.pushButton_age_struct_choose_column.setObjectName("pushButton_age_struct_choose_column")
        self.pushButton_age_struct_choose_column.setEnabled(False)
        self.pushButton_age_struct_choose_column.setText("Выбор столбцов")

        # checkBox choose column with type
        # rename checkBox_tab_age_struct_type_list_choose_column to checkBox_tab_age_struct_choose_column_type
        self.checkBox_tab_age_struct_choose_column_type = QCheckBox(self.gridLayoutWidget)
        self.checkBox_tab_age_struct_choose_column_type.setObjectName(
            "checkBox_tab_age_struct_choose_column_type")
        self.checkBox_tab_age_struct_choose_column_type.setEnabled(False)
        self.checkBox_tab_age_struct_choose_column_type.setText("Выбор столбца с видом")

        # checkBox choose column with years
        # rename checkBox_tab_age_struct_year_list_choose_column to checkBox_tab_age_struct_choose_column_year
        self.checkBox_tab_age_struct_choose_column_year = QCheckBox(self.gridLayoutWidget)
        self.checkBox_tab_age_struct_choose_column_year.setObjectName(
            "checkBox_tab_age_struct_choose_column_year")
        self.checkBox_tab_age_struct_choose_column_year.setEnabled(False)
        self.checkBox_tab_age_struct_choose_column_year.setText("Выбор столбца с годами лова")

        # checkBox choose column with areas
        # rename checkBox_tab_age_struct_area_list_choose_column to checkBox_tab_age_struct_choose_column_area
        self.checkBox_tab_age_struct_choose_column_area = QCheckBox(self.gridLayoutWidget)
        self.checkBox_tab_age_struct_choose_column_area.setObjectName(
            "checkBox_tab_age_struct_choose_column_area")
        self.checkBox_tab_age_struct_choose_column_area.setEnabled(False)
        self.checkBox_tab_age_struct_choose_column_area.setText("Выбор столбца с местами лова")

        # comboBox choose value - type
        # rename comboBox_tab_age_struct_type_list to comboBox_tab_age_struct_choose_value_type
        self.comboBox_tab_age_struct_choose_value_type = QComboBox(self.gridLayoutWidget)
        self.comboBox_tab_age_struct_choose_value_type.setObjectName(
            "comboBox_tab_age_struct_choose_value_type")
        self.comboBox_tab_age_struct_choose_value_type.setEnabled(False)

        # comboBox choose value - years
        # rename comboBox_tab_age_struct_year_list to comboBox_tab_age_struct_choose_value_year
        self.comboBox_tab_age_struct_choose_value_year = QComboBox(self.gridLayoutWidget)
        self.comboBox_tab_age_struct_choose_value_year.setObjectName(
            "comboBox_tab_age_struct_choose_value_year")
        self.comboBox_tab_age_struct_choose_value_year.setEnabled(False)

        # comboBox choose value - areas
        # rename comboBox_tab_age_struct_area_list to comboBox_tab_age_struct_choose_value_area
        self.comboBox_tab_age_struct_choose_value_area = QComboBox(self.gridLayoutWidget)
        self.comboBox_tab_age_struct_choose_value_area.setObjectName(
            "comboBox_tab_age_struct_choose_value_area")
        self.comboBox_tab_age_struct_choose_value_area.setEnabled(False)

        # Button choose value
        self.pushButton_age_struct_choose_values = QPushButton(self.gridLayoutWidget)
        self.pushButton_age_struct_choose_values.setObjectName(
            "pushButton_age_struct_choose_values")
        self.pushButton_age_struct_choose_values.setEnabled(False)
        self.pushButton_age_struct_choose_values.setText("Выбор значений")

        # textEdit for print dataframe
        # rename textEdit_age_structure_calculation_for_print_dataframe to textEdit_tab_age_struct_for_print_dataframe
        self.textEdit_tab_age_struct_for_print_dataframe = QTextEdit(self.tab_age_struct)
        self.textEdit_tab_age_struct_for_print_dataframe.setObjectName(
            "textEdit_tab_age_struct_for_print_dataframe")
        self.textEdit_tab_age_struct_for_print_dataframe.setGeometry(QRect(20, 210, 631, 221))

        # Button Save to SQL
        self.pushButton_export_age_structure_calculation_to_sql = QPushButton(self.tab_age_struct)
        self.pushButton_export_age_structure_calculation_to_sql.setObjectName(
            "pushButton_export_age_structure_calculation_to_sql")
        self.pushButton_export_age_structure_calculation_to_sql.setEnabled(False)
        self.pushButton_export_age_structure_calculation_to_sql.setText("Save to SQL")
        self.pushButton_export_age_structure_calculation_to_sql.setGeometry(QRect(690, 170, 111, 28))

        # Button Load from sql
        self.pushButton_load_age_structure_from_sql = QPushButton(self.tab_age_struct)
        self.pushButton_load_age_structure_from_sql.setObjectName(u"pushButton_load_age_structure_from_sql")
        self.pushButton_load_age_structure_from_sql.setEnabled(False)
        self.pushButton_load_age_structure_from_sql.setText("Load from SQL")
        self.pushButton_load_age_structure_from_sql.setGeometry(QRect(690, 200, 111, 28))

        # add widgets to grid layout
        self.grid_layout_age_struct.addLayout(self.verticalLayout_types, 1, 0, 1, 1)
        self.grid_layout_age_struct.addLayout(self.verticalLayout_years, 1, 1, 1, 1)
        self.grid_layout_age_struct.addLayout(self.verticalLayout_areas, 1, 2, 1, 1)
        self.grid_layout_age_struct.addWidget(self.pushButton_age_struct_choose_column, 2, 0, 1, 3)
        self.grid_layout_age_struct.addWidget(self.checkBox_tab_age_struct_choose_column_type, 6, 0, 1, 1)
        self.grid_layout_age_struct.addWidget(self.checkBox_tab_age_struct_choose_column_year, 6, 1, 1, 1)
        self.grid_layout_age_struct.addWidget(self.checkBox_tab_age_struct_choose_column_area, 6, 2, 1, 1)
        self.grid_layout_age_struct.addWidget(self.comboBox_tab_age_struct_choose_value_type, 7, 0, 1, 1)
        self.grid_layout_age_struct.addWidget(self.comboBox_tab_age_struct_choose_value_year, 7, 1, 1, 1)
        self.grid_layout_age_struct.addWidget(self.comboBox_tab_age_struct_choose_value_area, 7, 2, 1, 1)
        # self.grid_layout_age_struct.addWidget(self.pushButton_age_struct_choose_values, 8, 0, 1, 3)
        self.grid_layout_age_struct.addWidget(self.pushButton_age_struct_choose_values, 8, 0, 2, 3)

        # ui for tab catch history

        # Initialize grid
        # rename gridLayoutWidget_2 to gridLayoutWidgetCatch
        # rename gridLayout_3 to grid_layout_catch_history
        self.gridLayoutWidgetCatch = QWidget(self.tab_catch_history)
        self.gridLayoutWidgetCatch.setObjectName("gridLayoutWidgetCatch")
        self.gridLayoutWidgetCatch.setGeometry(QRect(10, 10, 441, 231))
        self.grid_layout_catch_history = QGridLayout(self.gridLayoutWidgetCatch)
        self.grid_layout_catch_history.setObjectName("grid_layout_catch_history")
        self.grid_layout_catch_history.setContentsMargins(0, 0, 0, 0)

        # vertical layout choose type
        # rename verticalLayout_2 to verticalLayout_choose_type
        self.verticalLayout_choose_type = QVBoxLayout()
        self.verticalLayout_choose_type.setObjectName("verticalLayout_choose_type")

        # Initialize vl widgets
        self.checkBox_catch_history_choose_type = QCheckBox(self.gridLayoutWidgetCatch)
        self.checkBox_catch_history_choose_type.setObjectName("checkBox_catch_history_choose_type")
        self.checkBox_catch_history_choose_type.setEnabled(False)
        self.checkBox_catch_history_choose_type.setText("Выберете вид")

        self.comboBox_catch_history_choose_type = QComboBox(self.gridLayoutWidgetCatch)
        self.comboBox_catch_history_choose_type.setObjectName(u"comboBox_catch_history_choose_type")
        self.comboBox_catch_history_choose_type.setEnabled(False)

        # left tableWidget
        self.tableWidget_catch_history_table_of_type_by_year = QTableWidget(self.gridLayoutWidgetCatch)
        self.tableWidget_catch_history_table_of_type_by_year.setObjectName(
            u"tableWidget_catch_history_table_of_type_by_year")
        self.tableWidget_catch_history_table_of_type_by_year.setEnabled(False)

        self.verticalLayout_choose_type.addWidget(self.checkBox_catch_history_choose_type)
        self.verticalLayout_choose_type.addWidget(self.comboBox_catch_history_choose_type)
        self.verticalLayout_choose_type.addWidget(self.tableWidget_catch_history_table_of_type_by_year)

        self.grid_layout_catch_history.addLayout(self.verticalLayout_choose_type, 0, 0, 1, 2)

        # vertical layout choose year
        # rename verticalLayoutWidget_2 to verticalLayoutWidgetCatch
        # rename verticalLayout_4 to verticalLayout_choose_year
        self.verticalLayoutWidgetCatch = QWidget(self.tab_catch_history)
        self.verticalLayoutWidgetCatch.setObjectName("verticalLayoutWidgetCatch")
        self.verticalLayoutWidgetCatch.setGeometry(QRect(460, 10, 381, 231))
        self.verticalLayout_choose_year = QVBoxLayout(self.verticalLayoutWidgetCatch)
        self.verticalLayout_choose_year.setObjectName("verticalLayout_choose_year")
        self.verticalLayout_choose_year.setContentsMargins(0, 0, 0, 0)

        # Initialize vl widgets
        self.checkBox_catch_history_choose_year = QCheckBox(self.verticalLayoutWidgetCatch)
        self.checkBox_catch_history_choose_year.setObjectName("checkBox_catch_history_choose_year")
        self.checkBox_catch_history_choose_year.setEnabled(False)
        self.checkBox_catch_history_choose_year.setText("Выбор года")

        self.comboBox_catch_history_choose_year = QComboBox(self.verticalLayoutWidgetCatch)
        self.comboBox_catch_history_choose_year.setObjectName("comboBox_catch_history_choose_year")
        self.comboBox_catch_history_choose_year.setEnabled(False)

        # right table
        self.tableWidget_catch_history_table_of_type_of_the_year = QTableWidget(self.verticalLayoutWidgetCatch)
        self.tableWidget_catch_history_table_of_type_of_the_year.setObjectName(
            "tableWidget_catch_history_table_of_type_of_the_year")
        self.tableWidget_catch_history_table_of_type_of_the_year.setEnabled(False)

        # rename pushButton_export_catch_history_to_sql pushButton_save_to_sql_catch_history
        self.pushButton_save_to_sql_catch_history = QPushButton(self.verticalLayoutWidgetCatch)
        self.pushButton_save_to_sql_catch_history.setObjectName(
            "pushButton_save_to_sql_catch_history")
        self.pushButton_save_to_sql_catch_history.setEnabled(False)

        # add widgets to vertical layout
        self.verticalLayout_choose_year.addWidget(self.checkBox_catch_history_choose_year)
        self.verticalLayout_choose_year.addWidget(self.comboBox_catch_history_choose_year)
        self.verticalLayout_choose_year.addWidget(self.tableWidget_catch_history_table_of_type_of_the_year)
        self.verticalLayout_choose_year.addWidget(self.pushButton_save_to_sql_catch_history)

        self.graphicsView_catch_history_graph_of_type_by_year = QGraphicsView(self.tab_catch_history)
        self.graphicsView_catch_history_graph_of_type_by_year.setObjectName(
            "graphicsView_catch_history_graph_of_type_by_year")
        self.graphicsView_catch_history_graph_of_type_by_year.setGeometry(QRect(10, 250, 831, 201))

        self.grid_layout = QGridLayout(self.central_widget)
        self.grid_layout.setObjectName("grid_layout")
        self.grid_layout.addWidget(self.tab_widget, 0, 0, 1, 1)

        if not main_window.objectName():
            main_window.setObjectName("main_window")
        main_window.resize(874, 558)
