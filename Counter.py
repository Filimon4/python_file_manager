from PySide6.QtWidgets import QWidget
from ui_form import Ui_Form

class Counter(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
