import sys
import socket as s
import protocol_fish_counting_SQL as fc
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connection()

    def connection(self):
        self.ui.label_SQL_Name.setText('SQL Name')
        self.ui.label_SQL_Server_Name.setText('SQL Server Name')
        self.ui.label_DB_Name.setText('DB Name')
        self.ui.lineEdit_SQL_Name.setText('SQL Server')
        self.ui.lineEdit_SQL_Server_Name.setText('DESKTOP-6RLRC5B\SQLEXPRESS')
        self.ui.lineEdit_DB_Name.setText('FISH_WORK')
        self.ui.btn_Connect_SQL_DB.clicked.connect(self.connection_line_input)

    def connection_line_input(self):

        self.dict_sql_settings['current_sql_server'] = self.ui.lineEdit_SQL_Name.text()
        self.dict_sql_settings['current_sql_server_name'] = self.ui.lineEdit_SQL_Server_Name.text()
        self.dict_sql_settings['current_data_base_name'] = self.ui.lineEdit_DB_Name.text()
        self.dict_sql_settings['current_bioanalis_table'] = self.ui.comboBox_tab_sql_bioanalis_table_list.currentText()

        self.ui.btn_Connect_SQL_DB.setEnabled(False)
        self.ui.btn_DisConnect_SQL_DB.setEnabled(True)


        self.ui.lineEdit_SQL_Name.setEnabled(False)
        self.ui.lineEdit_SQL_Server_Name.setEnabled(False)
        self.ui.lineEdit_DB_Name.setEnabled(False)
        self.ui.comboBox_tab_sql_bioanalis_table_list.setEnabled(False)

        self.ui.comboBox_tab_sql_bioanalis_table_list.setEnabled(True)

        self.set_tables()

        self.save_dict_file()


    def set_tables(self):
        fc.get_list_from_sql("SELECT [name] FROM sys.objects WHERE type in (N'U')")
        self.ui.comboBox_tab_sql_bioanalis_table_list.addItems(
            fc.get_list_from_sql("SELECT [name] FROM sys.objects WHERE type in (N'U')"))
        self.ui.pushButton_sql_bioanalis_choose_table.setEnabled(True)
        self.ui.pushButton_sql_bioanalis_choose_table.clicked.connect(self.push_button_age_struct_choose_table)



    def push_button_age_struct_choose_table(self):
        self.dict_sql_settings['current_bioanalis_table'] = self.ui.comboBox_tab_sql_bioanalis_table_list.currentText()
        self.save_dict_file()


    dict_sql_settings = {
        'current_sql_server': "SQL Server",
        'current_sql_server_name': "LAPTOP-E5Q4G2L1",
        'current_data_base_name': "FISH_WORK",
        'current_bioanalis_table': "bioanalis$"
    }

    def save_dict_file(self):
        file = open("connection_settings.py", "w")
        file.write(f'current_sql_server = "{self.dict_sql_settings["current_sql_server"]}"\n'
                   f'current_sql_server_name = "{self.dict_sql_settings["current_sql_server_name"]}"\n'
                   f'current_data_base_name = "{self.dict_sql_settings["current_data_base_name"]}"\n'
                   f'current_bioanalis_table = "{self.dict_sql_settings["current_bioanalis_table"]}"\n'
                   )
        file.close()


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())