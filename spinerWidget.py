from PySide6.QtWidgets import QWidget, QPushButton
from PySide6.QtGui import QIcon
from ui_spiner import Ui_Form

class SpinerWidget(QWidget, Ui_Form):
    def __init__(self):
       super().__init__()
       self.setupUi(self)
       self.setWindowTitle("User data")
       self.spinBox.setValue(50)
       self.plusButton.clicked.connect(self.plus)
       self.minusButton.clicked.connect(self.minus)

       plus_icon = QIcon("Images\\plus.png")
       minus_icon = QIcon("Images\\minus.jpg")

       self.plusButton.setIcon(plus_icon)
       self.minusButton.setIcon(minus_icon)

    def plus(self):
        value = self.spinBox.value()
        self.spinBox.setValue(value + 1)

    def minus(self):
        value = self.spinBox.value()
        self.spinBox.setValue(value - 1)
