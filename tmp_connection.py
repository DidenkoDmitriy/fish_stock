import sys
import initial_variables as init_var
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
        self.ui.btn_Connect_SQL_DB.clicked.connect(self.line_input)


    def line_input(self):

        self.sql_name = self.ui.lineEdit_SQL_Name.text()
        self.sql_server_name = self.ui.lineEdit_SQL_Server_Name.text()
        self.db_name = self.ui.lineEdit_DB_Name.text()
        self.ui.label_print_widjet.setText(f'{self.sql_name}\n{self.sql_server_name}\n{self.db_name}')


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())