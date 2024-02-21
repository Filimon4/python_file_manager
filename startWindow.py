import shutil
import os

from PySide6.QtWidgets import (
    QPushButton, QAbstractItemView, QApplication,
    QMessageBox, QDialog, QLineEdit, QInputDialog, QMainWindow,
    QFileSystemModel, QListView, QTreeView,
    QVBoxLayout
)
from PySide6.QtCore import (
    QFileInfo, QDir, QSize,
    QFile, Signal, Slot, QSettings
)
from PySide6.QtGui import QKeySequence, QShortcut, QMouseEvent
from FolderSelectorDialog import FolderSelectorDialog
from ui_mainwindow import Ui_MainWindow

# Maim logic modules
from FileOperations import FileOperations
from FileSystem import FileSystem
from FileView import FileView
# -- -- -- --

SETTINGS_NAME = "FileExplorer"
PRESET_NAME = "Preset_1"

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

        self.quit_action.triggered.connect(FileSystem.quit)
        self.about_qt_action.triggered.connect(FileSystem.about_qt)
        self.about_action.triggered.connect(FileSystem.about)

        self.newFile_action.triggered.connect(FileOperations.newFolder)
        self.newFolder_action.triggered.connect(FileOperations.newFile)
        self.delete_action.triggered.connect(FileOperations.delete)
        self.rename_action.triggered.connect(FileOperations.rename)
        self.move_action.triggered.connect(FileOperations.move)
        self.copy_action.triggered.connect(FileOperations.copy)
        self.paste_action.triggered.connect(FileOperations.paste)
        self.cut_action.triggered.connect(FileOperations.cut)

class FileExplorerApp(QMainWindow, Ui_MainWindow):
    treeClicked_Signal = Signal((QMouseEvent))
    rendeRoot_Signal = Signal((str))
    def __init__(self):
        super().__init__()

        self.currentDir = ""
        self.savedFiles = []

        settings = QSettings(SETTINGS_NAME, PRESET_NAME)
        current_dir = settings.value("current_dir")
        if current_dir:
            self.currentDir = current_dir

        # Signals
        self.treeClicked_Signal[QMouseEvent].connect(self.treeClicked)
        self.rendeRoot_Signal[str].connect(self.render_new_root)

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
        self.filePath.setText(f"{file}")
        self.FileV.last_move.insert(0, self.currentDir)
        self.render_new_root(file)

    @Slot(str)
    def render_new_root(self, dir):
        self.filePath.setText(f"{dir}")
        dirIndex = self.FileS._engine.index(dir)
        self.FileV.rootIndex = dirIndex
        self.currentDir = dir
        self.FileV.update_move_btn()
        self.FileV.tree.clearSelection()

    def resizeEvent(self, event):
        self.FileV.tree.resize(QSize(self.ui.treeView.width(), self.ui.treeView.height()))

    def showEvent(self, event):
        self.FileV.tree.resize(QSize(self.ui.treeView.width(), self.ui.treeView.height()))

    def closeEvent(self, event):
        settings = QSettings(SETTINGS_NAME, PRESET_NAME)
        settings.setValue("current_dir", self.currentDir)
        print("close")

