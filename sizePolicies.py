from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QSizePolicy


class SizePolicies(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Size Policies")

        label = QLabel("Some text: ")
        line_edit = QLineEdit()

        line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        label.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)

        button_1 = QPushButton("One")
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")

        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(label)
        h_layout_1.addWidget(line_edit)

        h_layout_2 = QHBoxLayout()
        h_layout_2.addWidget(button_1,2)
        h_layout_2.addWidget(button_2,1)
        h_layout_2.addWidget(button_3,1)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout_1)
        v_layout.addLayout(h_layout_2)

        self.setLayout(v_layout)



