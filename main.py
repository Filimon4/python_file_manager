# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtCore import QSize
from rockWidget import RockWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.app = app
        self.setWindowTitle("Cusom MainWindow")

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        toolbar.addAction(quit_action)

    def quit_app(self):
        self.app.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
