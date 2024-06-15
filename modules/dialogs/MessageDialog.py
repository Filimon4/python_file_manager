from PySide6.QtWidgets import QMessageBox, QInputDialog, QDialogButtonBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

class MessageDialog:
    def __init__(self, app):
        self.parent = app

    @staticmethod
    def input(title, text, default="Новый файл.txt"):
        input = QInputDialog()
        input.setWindowIcon(QIcon("app_icon.png"))
        input.setWindowTitle(title)
        input.setLabelText(text)

        input.setCancelButtonText("Отмена")
        input.setOkButtonText("Ок")
        input.setTextValue(default)

        if input.exec_() == QInputDialog.Accepted:
            return input.textValue(), True
        else:
            return "", False

    @staticmethod
    def ask(title, text):
        ask = QMessageBox()
        ask.setIcon(QMessageBox.Question)
        ask.setWindowTitle(title)
        ask.setWindowIcon(QIcon("app_icon.png"))
        ask.setText(text)
        ask.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        buttonYes = ask.button(QMessageBox.Yes)
        buttonYes.setText('Ок')
        buttonNo = ask.button(QMessageBox.No)
        buttonNo.setText('Отмена')
        ask.exec_()

        if ask.clickedButton() == buttonYes:
            return True
        else:
            return False

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
