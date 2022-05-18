import sys
import socket as s
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
        self.ui.lineEdit_SQL_Server_Name.setText(s.gethostname())
        self.ui.lineEdit_DB_Name.setText('FISH_WORK')

        self.ui.btn_Connect_SQL_DB.clicked.connect(self.connection_line_input)

    def connection_line_input(self):
        file = open("connection_settings.py", "w")
        file.write(f'current_sql_server = "{self.ui.lineEdit_SQL_Name.text()}"\n'
                   f'current_sql_server_name = "{self.ui.lineEdit_SQL_Server_Name.text()}"\n'
                   f'current_data_base_name = "{self.ui.lineEdit_DB_Name.text()}"'
                   )
        file.close()


    def age_structure_calculation(self):
        pass


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())