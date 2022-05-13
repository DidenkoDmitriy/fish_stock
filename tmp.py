import sys

import initial_variables as init_var
import protocol_fish_counting_SQL as fc


from PySide6.QtWidgets import QApplication, QMainWindow

from ui_form import Ui_Dialog


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        txt_SQL_base_name = init_var.current_data_base_name
        self.ui.label_Text_SQL_Base.setText(txt_SQL_base_name)

        txt_Table_name = init_var.table_name
        self.ui.label_Text_Table_Name.setText(txt_Table_name)

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())