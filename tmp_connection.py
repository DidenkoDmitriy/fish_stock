import sys
import SQL_Lib as sql_lib
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from ui_form import Ui_MainWindow


class MainWindow(QMainWindow):

    # Step 0. Initialization application window
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.df_age_struct = dict
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connection()

        # Connecting checkbox events to function in code
        self.ui.checkBox_tab_sql_connect_SQL_DB.stateChanged.connect(self.connection_checkbox_changed)
        self.ui.pushButton_export_age_structure_calculation_to_sql.clicked.connect(
            self.age_struct_calculation_export_to_sql
        )
        self.ui.pushButton_age_struct_choose_values.clicked.connect(self.button_age_struct_choose_values_pushed)
        self.ui.checkBox_tab_age_struct_area_list_choose_column.stateChanged.connect(self.area_checkbox_changed)
        self.ui.checkBox_tab_age_struct_year_list_choose_column.stateChanged.connect(self.year_checkbox_changed)
        self.ui.checkBox_tab_age_struct_type_list_choose_column.stateChanged.connect(self.type_checkbox_changed)
        self.ui.pushButton_age_struct_choose_column.clicked.connect(self.button_age_struct_choose_columns)
        self.ui.checkBox_tab_sql_bioanalis_table_list.stateChanged.connect(self.push_button_age_struct_choose_table)
        self.ui.checkBox_catch_history_save_choose_table.stateChanged.connect(
            self.push_button_catch_history_choose_table)
        self.ui.checkBox_catch_history_choose_type.stateChanged.connect(self.choose_type_check_box)
        self.ui.checkBox_catch_history_choose_year.stateChanged.connect(self.choose_year_check_box)
        # self.ui.pushButton_sql_bioanalis_choose_table.clicked.connect(self.push_button_age_struct_choose_table)

    def connection_checkbox_changed(self):
        if self.ui.checkBox_tab_sql_connect_SQL_DB.checkState():
            self.pushing_connecting_button()
        else:
            self.pushing_disconnecting_button()

    # Sets start sql parameters
    def connection(self):
        self.ui.lineEdit_SQL_Name.setText('SQL Server')
        self.ui.lineEdit_SQL_Server_Name.setText('LAPTOP-E5Q4G2L1')
        self.ui.lineEdit_DB_Name.setText('FISH_WORK')

    # Return to Step 0.
    def pushing_disconnecting_button(self):
        # Enabled/Disabled elements set
        self.ui.lineEdit_SQL_Name.setEnabled(True)
        self.ui.lineEdit_SQL_Server_Name.setEnabled(True)
        self.ui.lineEdit_DB_Name.setEnabled(True)
        self.ui.comboBox_tab_sql_bioanalis_table_list.setEnabled(False)
        self.ui.comboBox_tab_sql_bioanalis_table_list.clear()
        self.ui.comboBox_tab_age_struct_type_list_choose_column.setEnabled(False)
        self.ui.comboBox_tab_age_struct_year_list_choose_column.setEnabled(False)
        self.ui.comboBox_tab_age_struct_area_list_choose_column.setEnabled(False)
        self.ui.pushButton_age_struct_choose_column.setEnabled(False)

        self.ui.checkBox_tab_sql_bioanalis_table_list.setChecked(False)
        self.ui.checkBox_tab_sql_bioanalis_table_list.setEnabled(False)

        self.ui.comboBox_export_age_structure_calculation_to_sql.setEnabled(False)
        self.ui.comboBox_export_age_structure_persent_calculation_to_sql.setEnabled(False)
        self.ui.comboBox_export_age_structure_calculation_to_sql.clear()
        self.ui.comboBox_export_age_structure_persent_calculation_to_sql.clear()

        self.ui.comboBox_catch_history_table_choose.clear()
        self.ui.comboBox_catch_history_commercial_register_choose_table.clear()
        self.ui.comboBox_catch_history_privat_register_choose_table.clear()
        self.ui.comboBox_catch_history_table_choose.setEnabled(False)
        self.ui.comboBox_catch_history_commercial_register_choose_table.setEnabled(False)
        self.ui.comboBox_catch_history_privat_register_choose_table.setEnabled(False)

        self.ui.comboBox_tab_age_struct_type_list.clear()
        self.ui.comboBox_tab_age_struct_year_list.clear()
        self.ui.comboBox_tab_age_struct_area_list.clear()
        self.ui.comboBox_tab_age_struct_type_list.setEnabled(False)
        self.ui.comboBox_tab_age_struct_area_list.setEnabled(False)
        self.ui.comboBox_tab_age_struct_year_list.setEnabled(False)
        self.ui.comboBox_tab_age_struct_type_list_choose_column.setEnabled(False)
        self.ui.checkBox_tab_age_struct_year_list_choose_column.setEnabled(False)
        self.ui.checkBox_tab_age_struct_area_list_choose_column.setEnabled(False)
        self.ui.pushButton_age_struct_choose_column.setEnabled(False)
        self.ui.pushButton_age_struct_choose_values.setEnabled(False)

        self.ui.checkBox_tab_age_struct_type_list_choose_column.setChecked(False)
        self.ui.checkBox_tab_age_struct_year_list_choose_column.setChecked(False)
        self.ui.checkBox_tab_age_struct_area_list_choose_column.setChecked(False)
        self.ui.checkBox_tab_age_struct_type_list_choose_column.setEnabled(False)
        self.ui.checkBox_tab_age_struct_year_list_choose_column.setEnabled(False)
        self.ui.checkBox_tab_age_struct_area_list_choose_column.setEnabled(False)

        self.ui.checkBox_catch_history_save_choose_table.setChecked(False)
        self.ui.checkBox_catch_history_save_choose_table.setEnabled(False)
    # Step 1. Function to set SQL parameters and dynamic interface working
    def pushing_connecting_button(self):
        # Set SQL parameters
        self.dict_sql_settings['current_sql_server'] = self.ui.lineEdit_SQL_Name.text()
        self.dict_sql_settings['current_sql_server_name'] = self.ui.lineEdit_SQL_Server_Name.text()
        self.dict_sql_settings['current_data_base_name'] = self.ui.lineEdit_DB_Name.text()

        # Dynamic interface

        # Enabled/Disabled elements set
        self.ui.lineEdit_SQL_Name.setEnabled(False)
        self.ui.lineEdit_SQL_Server_Name.setEnabled(False)
        self.ui.lineEdit_DB_Name.setEnabled(False)
        self.ui.comboBox_tab_sql_bioanalis_table_list.setEnabled(False)
        self.ui.comboBox_tab_sql_bioanalis_table_list.setEnabled(True)
        self.ui.checkBox_tab_sql_bioanalis_table_list.setEnabled(True)
        self.ui.comboBox_export_age_structure_calculation_to_sql.setEnabled(True)
        self.ui.comboBox_export_age_structure_persent_calculation_to_sql.setEnabled(True)
        self.ui.comboBox_catch_history_table_choose.setEnabled(True)
        self.ui.comboBox_catch_history_privat_register_choose_table.setEnabled(True)
        self.ui.comboBox_catch_history_commercial_register_choose_table.setEnabled(True)

        # Completion comboBox data from SQL
        self.ui.comboBox_tab_sql_bioanalis_table_list.clear()
        var_sql_tbl_list = \
            sql_lib.get_list_from_sql(self.dict_sql_settings,
                                      "SELECT [name] FROM sys.objects WHERE type in (N'U')"
                                      )
        self.ui.comboBox_tab_sql_bioanalis_table_list.addItems(var_sql_tbl_list)
        self.ui.comboBox_export_age_structure_calculation_to_sql.addItems(var_sql_tbl_list)
        self.ui.comboBox_export_age_structure_persent_calculation_to_sql.addItems(var_sql_tbl_list)
        self.ui.comboBox_catch_history_table_choose.addItems(var_sql_tbl_list)
        self.ui.comboBox_catch_history_privat_register_choose_table.addItems(var_sql_tbl_list)
        self.ui.comboBox_catch_history_commercial_register_choose_table.addItems(var_sql_tbl_list)


        # Sets init values in comboboxes
        if var_sql_tbl_list.count('bioanalis$') != 0:
            self.ui.comboBox_tab_sql_bioanalis_table_list. \
                setCurrentIndex(var_sql_tbl_list.index('bioanalis$'))
        if var_sql_tbl_list.count('age_struct') != 0:
            self.ui.comboBox_export_age_structure_calculation_to_sql. \
                setCurrentIndex(var_sql_tbl_list.index('age_struct'))
        if var_sql_tbl_list.count('age_percent_table') != 0:
            self.ui.comboBox_export_age_structure_persent_calculation_to_sql. \
                setCurrentIndex(var_sql_tbl_list.index('age_percent_table'))

        if var_sql_tbl_list.count('cath_history') != 0:
            self.ui.comboBox_catch_history_table_choose.\
                setCurrentIndex(var_sql_tbl_list.index('cath_history'))
        if var_sql_tbl_list.count('Register$') != 0:
            self.ui.comboBox_catch_history_privat_register_choose_table.\
                setCurrentIndex(var_sql_tbl_list.index('Register$'))
        if var_sql_tbl_list.count('catch_without_permits$') != 0:
            self.ui.comboBox_catch_history_commercial_register_choose_table.\
                setCurrentIndex(var_sql_tbl_list.index('catch_without_permits$'))

        self.ui.checkBox_catch_history_save_choose_table.setEnabled(True)

        self.save_dict_file()

    # Step 2. SQL connected and bioanalyse Table chosen.
    def push_button_age_struct_choose_table(self):
        if self.ui.checkBox_tab_sql_bioanalis_table_list.checkState():
            self.dict_sql_settings[
                'current_bioanalis_table'] = self.ui.comboBox_tab_sql_bioanalis_table_list.currentText()
            # self.save_dict_file()

            # Enabled/Disabled interface elements set
            self.ui.comboBox_tab_age_struct_type_list_choose_column.setEnabled(True)
            self.ui.comboBox_tab_age_struct_year_list_choose_column.setEnabled(True)
            self.ui.comboBox_tab_age_struct_area_list_choose_column.setEnabled(True)
            self.ui.pushButton_age_struct_choose_column.setEnabled(True)

            # Clearing choose-column-combobox
            self.ui.comboBox_tab_age_struct_type_list_choose_column.clear()
            self.ui.comboBox_tab_age_struct_year_list_choose_column.clear()
            self.ui.comboBox_tab_age_struct_area_list_choose_column.clear()

            # Set data from SQL to choose-column-combobox
            tmp_list_of_columns = sql_lib.get_list_from_sql(self.dict_sql_settings,
                                                            '''
                                                            SELECT COLUMN_NAME
                                                            FROM INFORMATION_SCHEMA.COLUMNS
                                                            ''' + "WHERE TABLE_NAME = '" +
                                                            str(self.dict_sql_settings[
                                                                    'current_bioanalis_table']) + str(
                                                                "'")
                                                            )

            self.ui.comboBox_tab_age_struct_type_list_choose_column.addItems(tmp_list_of_columns)
            self.ui.comboBox_tab_age_struct_year_list_choose_column.addItems(tmp_list_of_columns)
            self.ui.comboBox_tab_age_struct_area_list_choose_column.addItems(tmp_list_of_columns)

            # Sets init values in comboboxes
            if tmp_list_of_columns.count('type') != 0:
                self.ui.comboBox_tab_age_struct_type_list_choose_column. \
                    setCurrentIndex(tmp_list_of_columns.index('type'))
            if tmp_list_of_columns.count('year') != 0:
                self.ui.comboBox_tab_age_struct_year_list_choose_column. \
                    setCurrentIndex(tmp_list_of_columns.index('year'))
            if tmp_list_of_columns.count('major water body') != 0:
                self.ui.comboBox_tab_age_struct_area_list_choose_column. \
                    setCurrentIndex(tmp_list_of_columns.index('major water body'))

        else:
            self.bioanalis_checkbox_undo()

    def bioanalis_checkbox_undo(self):
        # Clearing select columns interface
        self.ui.comboBox_tab_age_struct_type_list_choose_column.clear()
        self.ui.comboBox_tab_age_struct_year_list_choose_column.clear()
        self.ui.comboBox_tab_age_struct_area_list_choose_column.clear()
        self.ui.comboBox_tab_age_struct_type_list_choose_column.setEnabled(False)
        self.ui.comboBox_tab_age_struct_year_list_choose_column.setEnabled(False)
        self.ui.comboBox_tab_age_struct_area_list_choose_column.setEnabled(False)
        self.ui.pushButton_age_struct_choose_column.setEnabled(False)

        self.ui.checkBox_tab_age_struct_type_list_choose_column.setChecked(False)
        self.ui.checkBox_tab_age_struct_type_list_choose_column.setEnabled(False)

        # Clearing select values interface
        self.ui.comboBox_tab_age_struct_type_list.clear()
        self.ui.comboBox_tab_age_struct_type_list.setEnabled(False)

        self.clear_type()
        self.clear_area()
        self.clear_year()

    def clear_type(self):

        self.ui.checkBox_tab_age_struct_year_list_choose_column.setChecked(False)
        self.ui.checkBox_tab_age_struct_year_list_choose_column.setEnabled(False)
        self.ui.comboBox_tab_age_struct_year_list.clear()

    def clear_year(self):

        self.ui.checkBox_tab_age_struct_area_list_choose_column.setChecked(False)
        self.ui.checkBox_tab_age_struct_area_list_choose_column.setEnabled(False)
        self.ui.comboBox_tab_age_struct_area_list.clear()

    def clear_area(self):

        self.ui.pushButton_age_struct_choose_values.setEnabled(False)

    # Step 3. Setting area, year, type
    def button_age_struct_choose_columns(self):

        # Getting data from chose-column-combobox to settings dict
        #
        self.dict_sql_settings[
            'current_age_struct_type_column'] = self.ui.comboBox_tab_age_struct_type_list_choose_column.currentText()
        self.ui.comboBox_tab_age_struct_type_list.setEnabled(True)
        self.ui.checkBox_tab_age_struct_type_list_choose_column.setEnabled(True)
        self.ui.comboBox_tab_age_struct_type_list.clear()
        # import data from SQL to combobox
        self.ui.comboBox_tab_age_struct_type_list.addItems(
            sql_lib.get_list_from_sql(self.dict_sql_settings,
                                      f'SELECT DISTINCT '
                                      f'[{self.ui.comboBox_tab_age_struct_type_list_choose_column.currentText()}] '
                                      f'FROM [{self.ui.comboBox_tab_sql_bioanalis_table_list.currentText()}]'
                                      ))

        self.ui.checkBox_tab_age_struct_type_list_choose_column.setChecked(False)

        self.ui.checkBox_tab_age_struct_year_list_choose_column.setChecked(False)
        self.ui.checkBox_tab_age_struct_year_list_choose_column.setEnabled(False)
        self.ui.comboBox_tab_age_struct_year_list.clear()
        self.ui.comboBox_tab_age_struct_year_list.setEnabled(False)

        self.ui.checkBox_tab_age_struct_area_list_choose_column.setChecked(False)
        self.ui.checkBox_tab_age_struct_area_list_choose_column.setEnabled(False)
        self.ui.comboBox_tab_age_struct_area_list.clear()
        self.ui.comboBox_tab_age_struct_area_list.setEnabled(False)

        self.ui.pushButton_age_struct_choose_values.setEnabled(False)

    def type_checkbox_changed(self):

        if self.ui.checkBox_tab_age_struct_type_list_choose_column.checkState():

            self.ui.comboBox_tab_age_struct_type_list.setEnabled(False)
            self.dict_sql_settings['current_age_struct_year_column'] = \
                self.ui.comboBox_tab_age_struct_year_list_choose_column.currentText()
            self.ui.comboBox_tab_age_struct_year_list.setEnabled(True)
            self.ui.checkBox_tab_age_struct_year_list_choose_column.setEnabled(True)
            self.ui.comboBox_tab_age_struct_year_list.clear()
            self.ui.comboBox_tab_age_struct_year_list.addItems(
                sql_lib.get_list_from_sql(
                    self.dict_sql_settings,
                    f'SELECT DISTINCT '
                    f'[{self.ui.comboBox_tab_age_struct_year_list_choose_column.currentText()}] '
                    f'FROM [{self.ui.comboBox_tab_sql_bioanalis_table_list.currentText()}]'
                    f'WHERE [{self.ui.comboBox_tab_age_struct_type_list_choose_column.currentText()}]'
                    f"LIKE '{self.ui.comboBox_tab_age_struct_type_list.currentText()}'"
                ))
        else:
            self.ui.comboBox_tab_age_struct_type_list.setEnabled(True)
            self.clear_type()
            self.clear_area()
            self.clear_year()

    def year_checkbox_changed(self):
        if self.ui.checkBox_tab_age_struct_year_list_choose_column.checkState():
            self.ui.comboBox_tab_age_struct_year_list.setEnabled(False)
            self.dict_sql_settings[
                'current_age_struct_area_column'] = \
                self.ui.comboBox_tab_age_struct_area_list_choose_column.currentText()
            self.ui.comboBox_tab_age_struct_area_list.setEnabled(True)
            self.ui.checkBox_tab_age_struct_area_list_choose_column.setEnabled(True)
            self.ui.comboBox_tab_age_struct_area_list.clear()

            self.ui.comboBox_tab_age_struct_area_list.addItems(
                sql_lib.get_list_from_sql(
                    self.dict_sql_settings,
                    f'SELECT DISTINCT '
                    f'[{self.ui.comboBox_tab_age_struct_area_list_choose_column.currentText()}] '
                    f'FROM [{self.ui.comboBox_tab_sql_bioanalis_table_list.currentText()}]'
                    f'WHERE [{self.ui.comboBox_tab_age_struct_area_list_choose_column.currentText()}]'
                    f'IS NOT NULL '
                    f'AND [{self.ui.comboBox_tab_age_struct_type_list_choose_column.currentText()}] '
                    f"LIKE '{self.ui.comboBox_tab_age_struct_type_list.currentText()}'"
                ))

            # self.combobox_age_struct_list()
            self.save_dict_file()

        else:

            self.ui.comboBox_tab_age_struct_year_list.setEnabled(True)

            self.clear_year()
            self.clear_area()

    def area_checkbox_changed(self):
        if self.ui.checkBox_tab_age_struct_area_list_choose_column.checkState():
            self.ui.pushButton_age_struct_choose_values.setEnabled(True)
            self.ui.comboBox_tab_age_struct_area_list.setEnabled(False)
        else:
            self.ui.comboBox_tab_age_struct_area_list.setEnabled(True)
            self.clear_area()

    def button_age_struct_choose_values_pushed(self):

        # export data (type, year, place) from combobox to dict
        self.dict_sql_settings["current_age_struct_type_current"] = \
            self.ui.comboBox_tab_age_struct_type_list.currentText()
        self.dict_sql_settings["current_age_struct_year_current"] = \
            self.ui.comboBox_tab_age_struct_year_list.currentText()
        self.dict_sql_settings["current_age_struct_area_current"] = \
            self.ui.comboBox_tab_age_struct_area_list.currentText()

        # Enabled/Disabled interface elements set
        self.ui.pushButton_export_age_structure_calculation_to_sql.setEnabled(True)

        self.save_dict_file()
        self.age_struct_calculation()

    def age_struct_calculation(self):

        self.df_age_struct = sql_lib.get_age_struct_from_sql(
            sql_server=self.dict_sql_settings['current_sql_server'],
            bio_space=self.dict_sql_settings['current_age_struct_type_current'],
            cur_year=str(int(float(self.dict_sql_settings['current_age_struct_year_current']))),
            water_body=self.dict_sql_settings['current_age_struct_area_current'],
            sql_server_name=self.dict_sql_settings['current_sql_server_name'],
            data_base_name=self.dict_sql_settings['current_data_base_name']
        )
        self.ui.textEdit_age_structure_calculation_for_print_dataframe.setText(str(self.df_age_struct))

    def age_struct_calculation_export_to_sql(self):

        # export values from save combobox
        self.dict_sql_settings['current_age_struct_export_to_sql'] = \
            self.ui.comboBox_export_age_structure_calculation_to_sql.currentText()
        self.dict_sql_settings['current_age_struct_percent_export_to_sql'] = \
            self.ui.comboBox_export_age_structure_persent_calculation_to_sql.currentText()
        self.ui.textEdit_age_structure_calculation_for_print_dataframe.setText(
            self.ui.textEdit_age_structure_calculation_for_print_dataframe.toPlainText() + '\n' +
            sql_lib.save_age_struct_to_sql(
                sql_server=self.dict_sql_settings['current_sql_server'],
                bio_space=self.dict_sql_settings['current_age_struct_type_current'],
                cur_year=str(int(float(self.dict_sql_settings['current_age_struct_year_current']))),
                water_body=self.dict_sql_settings['current_age_struct_area_current'],
                cur_sample_size=sum(self.df_age_struct['count']),
                sql_server_name=self.dict_sql_settings['current_sql_server_name'],
                data_base_name=self.dict_sql_settings['current_data_base_name'],
                current_table=self.dict_sql_settings['current_age_struct_export_to_sql']
            ) + '\n' +
            sql_lib.save_age_percent_to_sql(
                df_age_count=self.df_age_struct,
                sql_server=self.dict_sql_settings['current_sql_server'],
                bio_space=self.dict_sql_settings['current_age_struct_type_current'],
                cur_year=str(int(float(self.dict_sql_settings['current_age_struct_year_current']))),
                water_body=self.dict_sql_settings['current_age_struct_area_current'],
                sql_server_name=self.dict_sql_settings['current_sql_server_name'],
                data_base_name=self.dict_sql_settings['current_data_base_name'],
                current_table=self.dict_sql_settings['current_age_struct_percent_export_to_sql']
            )
        )
        self.ui.textEdit_age_structure_calculation_for_print_dataframe.setText(
            self.ui.textEdit_age_structure_calculation_for_print_dataframe.toPlainText() + ' 1 ')
        self.save_dict_file()




    def push_button_catch_history_choose_table(self):
        if self.ui.checkBox_catch_history_save_choose_table.checkState():
            self.dict_sql_settings['current_catch_history_choose_table'] = \
                self.ui.comboBox_catch_history_table_choose.currentText()
            self.dict_sql_settings['current_catch_history_commercial_register_choose_table'] = \
                self.ui.comboBox_catch_history_commercial_register_choose_table.currentText()
            self.dict_sql_settings['current_catch_history_privat_register_choose_table'] = \
                self.ui.comboBox_catch_history_privat_register_choose_table.currentText()

            self.ui.tableWidget_catch_history_table_of_type_by_year.setEnabled(True)
            self.ui.comboBox_catch_history_choose_type.setEnabled(True)
            self.ui.checkBox_catch_history_choose_type.setEnabled(True)
            self.ui.comboBox_catch_history_table_choose.setEnabled(False)
            self.ui.comboBox_catch_history_commercial_register_choose_table.setEnabled(False)
            self.ui.comboBox_catch_history_privat_register_choose_table.setEnabled(False)

            self.ui.comboBox_catch_history_choose_type.clear()
            # найти откуда получать список видов
            self.ui.comboBox_catch_history_choose_type.addItems(
                sql_lib.get_list_from_sql(self.dict_sql_settings,
                                          f'SELECT DISTINCT '
                                          f'[type] '
                                          f'FROM [{self.ui.comboBox_catch_history_table_choose.currentText()}]'
                                          ))

            self.save_dict_file()

        else:
            self.ui.comboBox_catch_history_table_choose.setEnabled(True)
            self.ui.comboBox_catch_history_commercial_register_choose_table.setEnabled(True)
            self.ui.comboBox_catch_history_privat_register_choose_table.setEnabled(True)
            self.ui.comboBox_catch_history_choose_type.clear()
            self.ui.checkBox_catch_history_choose_type.setChecked(False)
            self.ui.tableWidget_catch_history_table_of_type_by_year.setEnabled(False)
            self.ui.comboBox_catch_history_choose_type.setEnabled(False)
            self.ui.checkBox_catch_history_choose_type.setEnabled(False)

    def choose_type_check_box(self):
        if self.ui.checkBox_catch_history_choose_type.checkState():
            self.dict_sql_settings['current_catch_history_choose_type']\
                = self.ui.comboBox_catch_history_choose_type.currentText()
            self.save_dict_file()

            self.ui.checkBox_catch_history_choose_year.setEnabled(True)
            self.ui.comboBox_catch_history_choose_year.setEnabled(True)
            self.ui.tableWidget_catch_history_table_of_type_of_the_year.setEnabled(True)

            type_catch_history_table = sql_lib.get_tuple_list_from_sql(self.dict_sql_settings,
                                      f"SELECT [type], [year], [fishing_stock_t], [quota_t], [cath_t]  "
                                      f"FROM {self.dict_sql_settings['current_catch_history_choose_table']} "
                                      f"WHERE [type] LIKE '{self.dict_sql_settings['current_catch_history_choose_type']}'"
                                      )

            self.ui.tableWidget_catch_history_table_of_type_by_year.setRowCount(len(type_catch_history_table))
            self.ui.tableWidget_catch_history_table_of_type_by_year.setColumnCount(5)
            self.ui.tableWidget_catch_history_table_of_type_by_year.setColumnWidth(1, 50)
            self.ui.tableWidget_catch_history_table_of_type_by_year.setColumnWidth(2, 50)
            self.ui.tableWidget_catch_history_table_of_type_by_year.setColumnWidth(3, 50)
            self.ui.tableWidget_catch_history_table_of_type_by_year.setColumnWidth(4, 50)
            column_column = 0
            for column in type_catch_history_table:
                self.ui.tableWidget_catch_history_table_of_type_by_year.setItem(column_column, 0, QTableWidgetItem(f'{column[0]}'))
                self.ui.tableWidget_catch_history_table_of_type_by_year.setItem(column_column, 1, QTableWidgetItem(f'{column[1]}'))
                self.ui.tableWidget_catch_history_table_of_type_by_year.setItem(column_column, 2, QTableWidgetItem(f'{column[2]}'))
                self.ui.tableWidget_catch_history_table_of_type_by_year.setItem(column_column, 3, QTableWidgetItem(f'{column[3]}'))
                self.ui.tableWidget_catch_history_table_of_type_by_year.setItem(column_column, 4, QTableWidgetItem(f'{column[4]}'))
                column_column += 1

            self.ui.comboBox_catch_history_choose_type.setEnabled(False)
            self.ui.tableWidget_catch_history_table_of_type_by_year.setEnabled(True)

            self.ui.comboBox_catch_history_choose_year.addItems(
                sql_lib.get_list_from_sql(self.dict_sql_settings,
                                          f'SELECT DISTINCT '
                                          f'[year] '
                                          f'FROM [{self.ui.comboBox_catch_history_table_choose.currentText()}]'
                                          f"WHERE [type] LIKE '{self.dict_sql_settings['current_catch_history_choose_type']}'"
                                          ))

        else:
            self.ui.checkBox_catch_history_choose_year.setEnabled(False)
            self.ui.comboBox_catch_history_choose_year.setEnabled(False)
            self.ui.tableWidget_catch_history_table_of_type_of_the_year.setEnabled(False)
            self.ui.tableWidget_catch_history_table_of_type_by_year.clear()
            self.ui.tableWidget_catch_history_table_of_type_by_year.setEnabled(False)
            self.ui.comboBox_catch_history_choose_type.setEnabled(True)
            self.ui.comboBox_catch_history_choose_year.clear()
            self.ui.checkBox_catch_history_choose_year.setChecked(False)

    def choose_year_check_box(self):
        if self.ui.checkBox_catch_history_choose_year.checkState():
            self.dict_sql_settings['current_catch_history_choose_year'] = \
                self.ui.comboBox_catch_history_choose_year.currentText()
            self.save_dict_file()
            self.ui.pushButton_export_catch_history_to_sql.setEnabled(True)
        else:
            self.ui.pushButton_export_catch_history_to_sql.setEnabled(False)

    # def load_settings_from_file(self):
    #     import connection_settings
    #
    #     self.dict_sql_settings["current_sql_server"] = connection_settings.current_sql_server
    #     self.dict_sql_settings["current_sql_server_name"] = connection_settings.current_sql_server_name
    #     self.dict_sql_settings["current_data_base_name"] = connection_settings.current_data_base_name
    #     self.dict_sql_settings["current_bioanalis_table"] = connection_settings.current_bioanalis_table
    #     self.dict_sql_settings["current_age_struct_type_column"] = connection_settings.current_age_struct_type_column
    #     self.dict_sql_settings["current_age_struct_year_column"] = connection_settings.current_age_struct_year_column
    #     self.dict_sql_settings["current_age_struct_area_column"] = connection_settings.current_age_struct_area_column
    #     self.dict_sql_settings["current_age_struct_type_current"] = connection_settings.current_age_struct_type_current
    #     self.dict_sql_settings["current_age_struct_year_current"] = connection_settings.current_age_struct_year_current
    #     self.dict_sql_settings["current_age_struct_area_current"] = connection_settings.current_age_struct_area_current

    dict_sql_settings = {
        'current_sql_server': "SQL Server",
        'current_sql_server_name': "DESKTOP-6RLRC5B\SQLEXPRESS",
        'current_data_base_name': "FISH_WORK",
        'current_bioanalis_table': "bioanalis$",
        'current_age_struct_type_column': "",
        'current_age_struct_year_column': "",
        'current_age_struct_area_column': "",
        'current_age_struct_type_current': "",
        'current_age_struct_year_current': "",
        'current_age_struct_area_current': "",
        'current_age_struct_export_to_sql': "",
        'current_age_struct_percent_export_to_sql': "",
        'current_catch_history_choose_table': "",
        'current_catch_history_commercial_register_choose_table': "",
        'current_catch_history_privat_register_choose_table': "",
        'current_catch_history_choose_type': "",
        'current_catch_history_choose_year': ""
    }

    def save_dict_file(self):
        file = open("connection_settings.py", "w", encoding='UTF-16')
        file.write(f'current_sql_server = "{self.dict_sql_settings["current_sql_server"]}"\n'
                   f'current_sql_server_name = "{self.dict_sql_settings["current_sql_server_name"]}"\n'
                   f'current_data_base_name = "{self.dict_sql_settings["current_data_base_name"]}"\n'
                   f'current_bioanalis_table = "{self.dict_sql_settings["current_bioanalis_table"]}"\n'
                   f'current_age_struct_type_column = "{self.dict_sql_settings["current_age_struct_type_column"]}"\n'
                   f'current_age_struct_year_column = "{self.dict_sql_settings["current_age_struct_year_column"]}"\n'
                   f'current_age_struct_area_column = "{self.dict_sql_settings["current_age_struct_area_column"]}"\n'
                   f'current_age_struct_type_current = "{self.dict_sql_settings["current_age_struct_type_current"]}"\n'
                   f'current_age_struct_year_current = "{self.dict_sql_settings["current_age_struct_year_current"]}"\n'
                   f'current_age_struct_area_current = "{self.dict_sql_settings["current_age_struct_area_current"]}"\n'
                   f'current_age_struct_export_to_sql = "{self.dict_sql_settings["current_age_struct_export_to_sql"]}"\n'
                   f'current_age_struct_percent_export_to_sql = "{self.dict_sql_settings["current_age_struct_percent_export_to_sql"]}"\n'
                   f'current_catch_history_choose_table = "{self.dict_sql_settings["current_catch_history_choose_table"]}"\n'
                   f'current_catch_history_commercial_register_choose_table = "{self.dict_sql_settings["current_catch_history_commercial_register_choose_table"]}"\n'
                   f'current_catch_history_privat_register_choose_table = "{self.dict_sql_settings["current_catch_history_privat_register_choose_table"]}"\n'
                   f'current_catch_history_choose_type = "{self.dict_sql_settings["current_catch_history_choose_type"]}"\n'
                   f'current_catch_history_choose_year = "{self.dict_sql_settings["current_catch_history_choose_year"]}"\n')
        file.close()

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
