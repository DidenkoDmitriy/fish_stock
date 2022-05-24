import sys
import SQL_Lib as sql_lib
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_MainWindow


class MainWindow(QMainWindow):

    # Step 0. Initialization application window
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connection()

        # Connecting buttons events to function in code
        self.ui.pushButton_Connect_SQL_DB.clicked.connect(self.pushing_connecting_button)
        self.ui.btn_DisConnect_SQL_DB.clicked.connect(self.pushing_disconnecting_button)

    # Sets start sql parameters
    def connection(self):
        self.ui.lineEdit_SQL_Name.setText('SQL Server')
        self.ui.lineEdit_SQL_Server_Name.setText('DESKTOP-6RLRC5B\SQLEXPRESS')
        self.ui.lineEdit_DB_Name.setText('FISH_WORK')

    # Step 1. Function to set SQL parameters and dynamic interface working
    def pushing_connecting_button(self):
        # Set SQL parameters
        self.dict_sql_settings['current_sql_server'] = self.ui.lineEdit_SQL_Name.text()
        self.dict_sql_settings['current_sql_server_name'] = self.ui.lineEdit_SQL_Server_Name.text()
        self.dict_sql_settings['current_data_base_name'] = self.ui.lineEdit_DB_Name.text()

        # Dynamic interface

        # Enabled/Disabled elements set
        self.ui.pushButton_Connect_SQL_DB.setEnabled(False)
        self.ui.btn_DisConnect_SQL_DB.setEnabled(True)
        self.ui.lineEdit_SQL_Name.setEnabled(False)
        self.ui.lineEdit_SQL_Server_Name.setEnabled(False)
        self.ui.lineEdit_DB_Name.setEnabled(False)
        self.ui.comboBox_tab_sql_bioanalis_table_list.setEnabled(False)
        self.ui.comboBox_tab_sql_bioanalis_table_list.setEnabled(True)
        self.ui.pushButton_sql_bioanalis_choose_table.setEnabled(True)

        # Completion comboBox data from SQL
        self.ui.comboBox_tab_sql_bioanalis_table_list.clear()
        self.ui.comboBox_tab_sql_bioanalis_table_list.addItems(
            sql_lib.get_list_from_sql(self.dict_sql_settings,
                                      "SELECT [name] FROM sys.objects WHERE type in (N'U')"
                                      ))

        self.ui.pushButton_sql_bioanalis_choose_table.clicked.connect(self.push_button_age_struct_choose_table)
        self.save_dict_file()

    # Retutn to Step 0.
    def pushing_disconnecting_button(self):
        # Enabled/Disabled elements set
        self.ui.pushButton_Connect_SQL_DB.setEnabled(True)
        self.ui.btn_DisConnect_SQL_DB.setEnabled(False)
        self.ui.lineEdit_SQL_Name.setEnabled(True)
        self.ui.lineEdit_SQL_Server_Name.setEnabled(True)
        self.ui.lineEdit_DB_Name.setEnabled(True)
        self.ui.comboBox_tab_sql_bioanalis_table_list.setEnabled(False)
        self.ui.comboBox_tab_sql_bioanalis_table_list.clear()
        self.ui.pushButton_sql_bioanalis_choose_table.setEnabled(False)
        self.ui.comboBox_tab_age_struct_type_list_choose_column.setEnabled(False)
        self.ui.comboBox_tab_age_struct_year_list_choose_column.setEnabled(False)
        self.ui.comboBox_tab_age_struct_area_list_choose_column.setEnabled(False)
        self.ui.pushButton_age_struct_choose_column.setEnabled(False)

    # Step 2. SQL connected and bioanalyse Table chosen.
    def push_button_age_struct_choose_table(self):
        self.dict_sql_settings['current_bioanalis_table'] = self.ui.comboBox_tab_sql_bioanalis_table_list.currentText()
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
                                                        str(self.dict_sql_settings['current_bioanalis_table']) + str(
                                                            "'")
                                                        )

        self.ui.comboBox_tab_age_struct_type_list_choose_column.addItems(tmp_list_of_columns)
        self.ui.comboBox_tab_age_struct_year_list_choose_column.addItems(tmp_list_of_columns)
        self.ui.comboBox_tab_age_struct_area_list_choose_column.addItems(tmp_list_of_columns)

        self.ui.pushButton_age_struct_choose_column.clicked.connect(self.button_age_struct_choose_columns)

    # Step 3. Setting area, year, type
    def button_age_struct_choose_columns(self):

        # Getting data from chose-column-combobox to settings dict
        self.dict_sql_settings[
            'current_age_struct_type_column'] = self.ui.comboBox_tab_age_struct_type_list_choose_column.currentText()
        self.dict_sql_settings[
            'current_age_struct_year_column'] = self.ui.comboBox_tab_age_struct_year_list_choose_column.currentText()
        self.dict_sql_settings[
            'current_age_struct_area_column'] = self.ui.comboBox_tab_age_struct_area_list_choose_column.currentText()

        # Enabled/Disabled interface elements set
        self.ui.comboBox_tab_age_struct_type_list.setEnabled(True)
        self.ui.comboBox_tab_age_struct_year_list.setEnabled(True)
        self.ui.comboBox_tab_age_struct_area_list.setEnabled(True)
        self.ui.pushButton_age_struct_choose_values.setEnabled(True)

        self.ui.comboBox_tab_age_struct_type_list.clear()
        self.ui.comboBox_tab_age_struct_year_list.clear()
        self.ui.comboBox_tab_age_struct_area_list.clear()

        # Data from SQL to combobox
        self.ui.comboBox_tab_age_struct_type_list.addItems(
            sql_lib.get_list_from_sql(self.dict_sql_settings,
                                      f'SELECT DISTINCT '
                                      f'[{self.ui.comboBox_tab_age_struct_type_list_choose_column.currentText()}] '
                                      f'FROM [{self.ui.comboBox_tab_sql_bioanalis_table_list.currentText()}]'
                                      ))
        self.ui.comboBox_tab_age_struct_year_list.addItems(
            sql_lib.get_list_from_sql(self.dict_sql_settings,
                                      f'SELECT DISTINCT '
                                      f'[{self.ui.comboBox_tab_age_struct_year_list_choose_column.currentText()}] '
                                      f'FROM [{self.ui.comboBox_tab_sql_bioanalis_table_list.currentText()}]'
                                      ))
        self.ui.comboBox_tab_age_struct_area_list.addItems(
            sql_lib.get_list_from_sql(self.dict_sql_settings,
                                      f'SELECT DISTINCT '
                                      f'[{self.ui.comboBox_tab_age_struct_area_list_choose_column.currentText()}] '
                                      f'FROM [{self.ui.comboBox_tab_sql_bioanalis_table_list.currentText()}]'
                                      ))

        # self.combobox_age_struct_list()
        # self.save_dict_file()

    # def combobox_age_struct_list(self):

    #
    #     self.ui.comboBox_tab_age_struct_type_list_choose_column.currentText()
    #     self.ui.comboBox_tab_age_struct_year_list_choose_column.currentText()
    #     self.ui.comboBox_tab_age_struct_area_list_choose_column.currentText()
    #
    #     self.ui.pushButton_age_struct_choose_values.clicked.connect(self.button_age_struct_columns)
    #
    # def button_age_struct_columns(self):
    #     self.dict_sql_settings[
    #         'current_age_struct_type_data_list'] = self.ui.comboBox_tab_age_struct_type_list.currentText()
    #     self.dict_sql_settings[
    #         'current_age_struct_year_data_list'] = self.ui.comboBox_tab_age_struct_year_list.currentText()
    #     self.dict_sql_settings[
    #         'current_age_struct_area_data_list'] = self.ui.comboBox_tab_age_struct_area_list.currentText()
    #     self.save_dict_file()
    #

    dict_sql_settings = {
        'current_sql_server': "SQL Server",
        'current_sql_server_name': "DESKTOP-6RLRC5B\SQLEXPRESS",
        'current_data_base_name': "FISH_WORK",
        'current_bioanalis_table': "bioanalis$",
        'current_age_struct_type_column': "",
        'current_age_struct_year_column': "",
        'current_age_struct_area_column': "",
        'current_age_struct_type_data_list': "",
        'current_age_struct_year_data_list': "",
        'current_age_struct_area_data_list': ""
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
                   f'current_age_struct_type_data_list = "{self.dict_sql_settings["current_age_struct_type_data_list"]}"\n'
                   f'current_age_struct_year_data_list = "{self.dict_sql_settings["current_age_struct_year_data_list"]}"\n'
                   f'current_age_struct_area_data_list = "{self.dict_sql_settings["current_age_struct_area_data_list"]}"\n'
                   )
        file.close()


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
