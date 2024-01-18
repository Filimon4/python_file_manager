# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication
from ui_mainwindow import Ui_MainWindow

class StartWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app

        self.actionQuit.triggered.connect(self.quit)
        self.actionCopy.triggered.connect(self.copy)
        self.actionCut.triggered.connect(self.cut)
        self.actionPaste.triggered.connect(self.paste)
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionAbout.triggered.connect(self.about)
        # self.actionAbout_Qt.triggered.connect(self.aboutqt)

    def quit(self):
        self.app.quit()
    def copy(self):
        self.textEdit.copy()
    def cut(self):
        self.textEdit.cut()
    def paste(self):
        self.textEdit.paste()
    def undo(self):
        self.textEdit.undo()
    def redo(self):
        self.textEdit.redo()
    def about(self):
        QMessageBox.information(self,"Going pro!","QMainWindow,Qt Designer and Resources : Going pro!")
    def aboutqt(self):
        QApplication.aboutQt()

