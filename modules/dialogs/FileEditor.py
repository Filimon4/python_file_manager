import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QTextEdit, QPushButton, QFileDialog, QFontDialog, QMessageBox
from PySide6.QtGui import QFont, QTextCursor
from PySide6.QtCore import QFile, QIODevice, QTextStream

class TextEditorDialog(QDialog):
    def __init__(self, filePath=None):
        super().__init__()

        self.filePath = filePath

        self.setWindowTitle("Text Editor")
        self.setGeometry(100, 100, 600, 400)

        self.textEdit = QTextEdit()
        self.saveButton = QPushButton("Save")
        self.changeFontButton = QPushButton("Change Font")

        self.saveButton.clicked.connect(self.save)
        self.changeFontButton.clicked.connect(self.changeFont)

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.saveButton)
        layout.addWidget(self.changeFontButton)

        self.setLayout(layout)

        if self.filePath:
            self.loadFile()

    def loadFile(self):
        with open(self.filePath, "r") as f:
            self.textEdit.setPlainText(f.read())

    def save(self):
        if not self.filePath:
            self.filePath = self.getFilePathFromDialog()
        if self.filePath:
            with open(self.filePath, 'w') as f:
                f.write(self.textEdit.toPlainText())

    def changeFont(self):
        ok, font = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)
