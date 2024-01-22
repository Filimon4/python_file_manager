import sys
from PySide6.QtWidgets import QApplication
from startWindow import StartWindow

if __name__ == "__main__":
    app = QApplication([])
    window = StartWindow()
    window.show()
    app.exec()


