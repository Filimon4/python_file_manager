from PySide6.QtWidgets import QApplication
from startWindow import FileExplorerApp
import pyuac

def main():
    # print(pyuac.isUserAdmin())
    # if not pyuac.isUserAdmin():
    #     pyuac.runAsAdmin(wait=False)
    #     print(pyuac.isUserAdmin())
    
    # if pyuac.isUserAdmin():
    app = QApplication([])
    window = FileExplorerApp()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()

