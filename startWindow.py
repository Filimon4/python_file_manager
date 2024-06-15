import os
import time

import rc_icons
from PySide6.QtWidgets import (
    QMainWindow,
    QMessageBox
)
from PySide6.QtCore import (
    QSize, Signal, Slot, QTimer
)
from PySide6.QtGui import QKeySequence, QShortcut, QMouseEvent, QIcon, QPixmap
from ui_mainwindow import Ui_MainWindow

# Main logic modules
from modules import FileOperations, FileSystem, FileView, Disks, FileEncrypt, FileDecrypt, ActionsApp
from modules.dialogs import TextEditorDialog, MessageDialog, ProgressBar
# -- -- -- --

class FileExplorerApp(QMainWindow, Ui_MainWindow):
    treeClicked_Signal = Signal((QMouseEvent))
    rendeRoot_Signal = Signal((str))
    setSavedFiles_Signal = Signal((list))
    setCurrentFolder_Signal = Signal((str))
    renderVirtualRoot_Signal = Signal((str))
    updateDir_Signal = Signal()
    def __init__(self):
        super().__init__()

        app_icon = QIcon(QPixmap(':/app_icon.png'))
        self.setWindowIcon(app_icon)

        self.currentDir = ""
        self.savedFiles = []

        # Signals
        self.treeClicked_Signal[QMouseEvent].connect(self.treeClicked)
        self.rendeRoot_Signal[str].connect(self.renderNewRoot)
        self.renderVirtualRoot_Signal[str].connect(self.renderVirtualRoot)
        self.setSavedFiles_Signal[list].connect(self.setSavedFiles)
        self.setCurrentFolder_Signal[str].connect(self.setCurrentFolder)
        self.updateDir_Signal.connect(self.updateDir)

        # ui.ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Файловый менеджер")
        self.setGeometry(100, 100, 900, 600)

        # ui elements
        self.filePath = self.ui.directory
        self.filePath.setText(f"{self.currentDir}")

        self.FileS = FileSystem(self)
        self.FileV = FileView(self)
        self.FileO = FileOperations(self)
        self.Encrpt = FileEncrypt.Encrypt(self)
        self.Decrpt = FileDecrypt.Decrypt(self)
        self.Disks = Disks(self)
        self.Notif = MessageDialog(self)

        self.actions = ActionsApp(self)

        self.copy_short = QShortcut(QKeySequence("Ctrl+A"), self)
        self.copy_short.activated.connect(FileOperations.copy)
        self.copy_short = QShortcut(QKeySequence("Ctrl+S"), self)
        self.copy_short.activated.connect(FileOperations.paste)
        self.copy_short = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.copy_short.activated.connect(FileOperations.cut)
        self.copy_short = QShortcut(QKeySequence("Ctrl+D"), self)
        self.copy_short.activated.connect(FileOperations.delete)

    @Slot(QMouseEvent)
    def treeClicked(self, index):
        file = self.FileS.engine.filePath(index)
        if os.path.isdir(file):
            self.filePath.setText(f"{file}")
            # self.FileV.last_move.insert(0, self.currentDir)
            self.renderNewRoot(file)
        elif os.path.isfile(file):
            window = TextEditorDialog(file)
            window.exec_()

    @Slot(str)
    def renderNewRoot(self, dir):
        self.filePath.setText(f"{dir}")
        dirIndex = self.FileS._engine.index(dir)
        
        self.FileS.engine.setRootPath(dir)
        self.FileV.rootIndex = dirIndex
        self.currentDir = dir
        
        self.FileV.tree.clearSelection()
        self.FileV.update_steps(self.currentDir)
        self.FileV.update_move_btn()

    @Slot(str)
    def renderVirtualRoot(self, dir):
        self.filePath.setText(f"{dir}")
        dirIndex = self.FileS._engine.index(dir)

        self.FileS.engine.setRootPath(dir)
        self.FileV.rootIndex = dirIndex

        self.FileV.tree.clearSelection()
        self.FileV.update_move_btn()

    @Slot(list)
    def setSavedFiles(self, files):
        self.savedFiles = files

    @Slot(str)
    def setCurrentFolder(self, dir):
        self.currentDir = dir

    @Slot()
    def updateDir(self):
        self.currentDir = self.FileS.engine.rootPath()
        self.FileS.engine.setRootPath(self.currentDir)
        self.FileV.rootIndex = self.FileS.engine.index(self.currentDir)
        self.FileV.update_steps(self.currentDir)
        self.FileV.update_move_btn()

    def resizeEvent(self, event):
        self.FileV.tree.resize(QSize(self.ui.treeView.width(), self.ui.treeView.height()))

    def showEvent(self, event):
        self.FileV.tree.resize(QSize(self.ui.treeView.width(), self.ui.treeView.height()))

    def closeEvent(self, event):
        pass

