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


        self.ui.label_Text_SQL_Base.setText(init_var.current_data_base_name)
        self.ui.label_Text_Table_Name.setText(init_var.table_name)
        self.ui.label_Text_Space.setText(init_var.current_bio_space)
        self.ui.label_Text_Year.setText(init_var.current_cur_year)
        # current_water_places = fc.get_water_place_for_space_from_sql(
        #     sql_server=init_var.current_sql_server,
        #     bio_space=init_var.current_bio_space,
        #     cur_year=init_var.current_cur_year,
        #     sql_server_name=init_var.current_sql_server_name,
        #     data_base_name=init_var.current_data_base_name
        # )
        # self.ui.comboBox.insertItems(self,current_water_places)

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())