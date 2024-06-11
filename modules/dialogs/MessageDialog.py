
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Qt

class MessageDialog:
    def __init__(self, app):
        self.parent = app

    def question(self, title, message):
        button = QMessageBox.question(self.parent, "Question dialog", "The longer message")

        if button == QMessageBox.StandardButton.Yes:
            print("Yes")
        else:
            print("NO")

    def info(self, title, message):
        button = QMessageBox.information(self.parent, title, message)

        if button == QMessageBox.StandardButton.Ok:
            print("Ok")
        else:
            print("No")

    def critical(self):
        button = QMessageBox.critical(
            self.parent,
            "Oh dear!",
            "Something went very wrong.",
            buttons=QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.NoToAll | QMessageBox.StandardButton.Ignore,
            defaultButton=QMessageBox.StandardButton.Discard,
        )

        if button == QMessageBox.StandardButton.Discard:
            print("Discard!")
        elif button == QMessageBox.StandardButton.NoToAll:
            print("No to all!")
        else:
            print("Ignore!")
