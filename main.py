from PySide6.QtWidgets import QApplication
from startWindow import FileExplorerApp

def main():
    app = QApplication([])
    window = FileExplorerApp()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()

