from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton


class ImageBox(QWidget):
    def __init__(self):
        super().__init__()
        # screenshot_of_window
        self.setWindowTitle("QLabel Image Demo")

        image_label = QLabel()
        image_label.setPixmap(QPixmap("screenshot_of_window.png"))
        image_label.resize(QSize(200, 200))

        layout = QVBoxLayout()
        layout.addWidget(image_label)

        self.setLayout(layout)

