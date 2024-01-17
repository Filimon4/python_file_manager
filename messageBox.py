from PySide6 import QtCore
from PySide6.QtWidgets import QPushButton, QMessageBox, QVBoxLayout, QWidget


class MessageBox(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QMessage box")

        button_clicked_question = QPushButton("Question")
        button_clicked_question.clicked.connect(self.button_clicked_question)

        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.button_clicked_critical)

        button_about = QPushButton("About")
        button_about.clicked.connect(self.button_clicked_about)

        layout = QVBoxLayout()
        layout.addWidget(button_clicked_question)
        layout.addWidget(button_critical)
        layout.addWidget(button_about)
        self.setLayout(layout)

    def button_clicked_about(self):
        message = QMessageBox()
        message.setMinimumSize(700,200)
        message.setWindowTitle("Message title")
        message.setText("Something happened")
        message.setInformativeText("Hi, this is about message")
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("user choose ok")
        else:
            print("User chose Cancel")

    def button_clicked_critical(self):
        ret = QMessageBox.critical(self, "Message Title", "Critical message", QMessageBox.Ok | QMessageBox.Cancel)

        if ret == QMessageBox.Ok:
            print("User chose OK")
        else:
            print("User chose Critical")

    def button_clicked_question(self):
        ret = QMessageBox.question(self, "Message Title", "Asking a question?", QMessageBox.Ok | QMessageBox.Cancel)

        if ret == QMessageBox.Ok:
            print("Ok")
        else:
            print('Cancel')
