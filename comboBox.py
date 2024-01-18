from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QComboBox, QPushButton, QVBoxLayout

class ComboBox(QWidget):
    def __init__(self):
        super().__init__()

        self.combo_box = QComboBox(self)

        self.combo_box.addItem("Earch")
        self.combo_box.addItem("Venus")
        self.combo_box.addItem("Mars")
        self.combo_box.addItem("Pluton")
        self.combo_box.addItem("Saturn")

        button_current_value = QPushButton("Current Value")
        button_current_value.clicked.connect(self.current_value)
        button_set_current = QPushButton("Set Value")
        button_set_current.clicked.connect(self.set_current)
        button_get_values = QPushButton("Get Values")
        button_get_values.clicked.connect(self.get_values)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.combo_box)
        v_layout.addWidget(button_current_value)
        v_layout.addWidget(button_set_current)
        v_layout.addWidget(button_get_values)
        v_layout.addSpacing(100)

        self.setLayout(v_layout)

    def get_values(self):
        pass

    def set_current(self):
        pass

    def current_value(self):
        pass
