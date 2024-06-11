import os
import sys
import codecs
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QTextEdit, QPushButton, QFileDialog, QFontDialog, QMessageBox, QProgressDialog
from PySide6.QtGui import QFont, QTextCursor, QIcon
from PySide6.QtCore import QFile, QIODevice, QTextStream, Qt
from modules.dialogs.ProgressBar import ProgressBar

class TextEditorDialog(QDialog):
    def __init__(self, filePath=None):
        super().__init__()

        self.filePath = filePath

        app_icon = QIcon('app_icon.png')
        self.setWindowIcon(app_icon)

        self.setWindowTitle("Редактор файлов")
        self.setGeometry(100, 100, 600, 400)

        self.textEdit = QTextEdit()
        self.textEdit.setFontFamily("Consolas")
        self.textEdit.setFont("Regular")
        self.saveButton = QPushButton("Сохранить")
        self.changeFontButton = QPushButton("Изменить шрифт")

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

        fileSize = os.path.getsize(self.filePath)
        print(fileSize)

        p = QProgressDialog("Чтение файла", "Закрыть", 0, fileSize, self)
        p.setWindowModality(Qt.WindowModal)
        p.setMinimumDuration(0)
        p.setValue(0)

        with open(self.filePath, "r", errors='replace') as f:
            # self.textEdit.setPlainText(f.read())
            chunk_size = 1024
            while True:
                if p.wasCanceled():
                    break
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                self.textEdit.insertPlainText(chunk)
                p.setValue(p.value() + chunk_size)
                
        p.close()

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
