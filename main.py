import sys
from PySide6.QtWidgets import QApplication
from startWindow import StartWindow
from Counter import Counter

if __name__ == "__main__":
    app = QApplication([])
    window = StartWindow()
    window.show()
    # c = Counter()
    # c.show()
    app.exec()


