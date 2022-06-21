from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import UiMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        # super(MainWindow, self).__init__(parent)
        super().__init__()
        self.df_age_struct = dict
        self.ui = UiMainWindow(self)
        # self.ui.setup_ui(self)


def main():
    app = QApplication()
    window = MainWindow()
    window.show()
    exit(app.exec())


if __name__ == "__main__":
    main()
