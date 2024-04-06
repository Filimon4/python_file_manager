import os

from PySide6.QtWidgets import (
    QMainWindow,
)
from PySide6.QtCore import (
    QSize, Signal, Slot, QSettings
)
from PySide6.QtGui import QKeySequence, QShortcut, QMouseEvent, QIcon
from ui_mainwindow import Ui_MainWindow

# Maim logic modules
from FileOperations import FileOperations
from FileSystem import FileSystem
from FileView import FileView, Disks
from CipherAlgo import Encrypt, Decrypt
from FileEditor import TextEditorDialog
# -- -- -- --

class ActionsApp():

    def __init__(self, app):
        self.app = app
        self.ui = app.ui

        self.quit_action = self.ui.actionQuit

        self.about_action = self.ui.actionAbout
        self.about_qt_action = self.ui.actionAbout_Qt

        self.newFile_action = self.ui.actionMake_folder
        self.newFolder_action = self.ui.actionNew_File
        self.delete_action = self.ui.actionDelete_folder
        self.rename_action = self.ui.actionRename
        self.move_action = self.ui.actionMove
        self.copy_action = self.ui.actionCopy
        self.paste_action = self.ui.actionPaste
        self.cut_action = self.ui.actionCut

        self.quit_action.triggered.connect(self.app.FileS.quit)
        self.about_qt_action.triggered.connect(self.app.FileS.about_qt)
        self.about_action.triggered.connect(self.app.FileS.about)

        self.newFile_action.triggered.connect(self.app.FileO.newFolder)
        self.newFolder_action.triggered.connect(self.app.FileO.newFile)
        self.delete_action.triggered.connect(self.app.FileO.delete)
        self.rename_action.triggered.connect(self.app.FileO.rename)
        self.move_action.triggered.connect(self.app.FileO.move)
        self.copy_action.triggered.connect(self.app.FileO.copy)
        self.paste_action.triggered.connect(self.app.FileO.paste)
        self.cut_action.triggered.connect(self.app.FileO.cut)

class FileExplorerApp(QMainWindow, Ui_MainWindow):
    treeClicked_Signal = Signal((QMouseEvent))
    rendeRoot_Signal = Signal((str))
    setSavedFiles_Signal = Signal((list))
    setCurrentFolder_Signal = Signal((str))
    def __init__(self):
        super().__init__()

        app_icon = QIcon('app_icon.png')
        self.setWindowIcon(app_icon)

        self.currentDir = ""
        self.savedFiles = []

        # Signals
        self.treeClicked_Signal[QMouseEvent].connect(self.treeClicked)
        self.rendeRoot_Signal[str].connect(self.renderNewRoot)
        self.setSavedFiles_Signal[list].connect(self.setSavedFiles)
        self.setCurrentFolder_Signal[str].connect(self.setCurrentFolder)

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
        self.Encrpt = Encrypt(self)
        self.Decrpt = Decrypt(self)
        self.Disks = Disks(self)

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
        # file = self.FileS.engine.filePath(index)
        print(index)
        file = self.FileS.engine.filePath(self.FileV.proxyModel.mapToSource(index))
        print(file)
        if os.path.isdir(file):
            self.filePath.setText(f"{file}")
            self.FileV.last_move.insert(0, self.currentDir)
            self.renderNewRoot(file)
        elif os.path.isfile(file):
            window = TextEditorDialog(file)
            window.exec_()

    @Slot(str)
    def renderNewRoot(self, dir):
        self.filePath.setText(f"{dir}")
        dirIndex = self.FileS._engine.index(dir)
        self.FileV.rootIndex = dirIndex
        self.currentDir = dir
        self.FileV.update_move_btn()
        self.FileV.tree.clearSelection()
        ###
        self.FileS.engine.setRootPath(dir)
        # print(self.FileS.engine.rootPath())

    @Slot(list)
    def setSavedFiles(self, files):
        self.savedFiles = files

    @Slot(str)
    def setCurrentFolder(self, dir):
        self.currentDir = dir

    def resizeEvent(self, event):
        self.FileV.tree.resize(QSize(self.ui.treeView.width(), self.ui.treeView.height()))

    def showEvent(self, event):
        self.FileV.tree.resize(QSize(self.ui.treeView.width(), self.ui.treeView.height()))

    def closeEvent(self, event):
        pass

