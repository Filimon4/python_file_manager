from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

class LoadUI(QWidget):
    def __init__(self):
        super().__init__()

        self.window = loader.load("form.ui", None)
        self.setWindowTitle("QUiLoader")
        self.window.pushButton.clicked.connect(self.do_something)

    def show(self):
        self.window.show()

    def do_something(self):
        print(self.window.fullNameLineEdit.text(), " is a ", self.window.OccupationLineEdit.text())
