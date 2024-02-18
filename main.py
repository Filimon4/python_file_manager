from PySide6.QtWidgets import QApplication
from startWindow import FileExplorerApp

if __name__ == "__main__":
    app = QApplication([])
    window = FileExplorerApp()
    window.show()
    app.exec()


