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
    QFile, Signal, Slot
)
from PySide6.QtGui import QKeySequence, QShortcut, QMouseEvent
from FolderSelectorDialog import FolderSelectorDialog
from ui_mainwindow import Ui_MainWindow

# Maim logic modules
from FileOperations import FileOperations
from FileSystem import FileSystem
from FileView import FileView
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
    rendeRoot_Signal = Signal()
    def __init__(self):
        super().__init__()
        # logic
        # self.last_move = []
        # self.next_move = []
        self.currentDir = ''
        self.savedFiles = []

        # Signals
        self.treeClicked_Signal[QMouseEvent].connect(self.treeClicked)

        # ui.ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Файловый менеджер")
        self.setGeometry(100, 100, 900, 600)

        # ui elements
        self.filePath = self.ui.directory
        self.filePath.setText(f"{QDir.root().dirName()}")

        self.FileS = FileSystem(self)
        self.FileV = FileView(self)

        # QFileSystemModel
        # self.dialog = QFileSystemModel(self)
        # self.dialog.setRootPath(QDir.currentPath())

        # QTreeView
        # self.tree_ui = self.ui.treeView
        # self.tree = QListView(self.ui.treeView)
        # self.tree.resize(QSize(self.ui.treeView.width(), self.ui.treeView.height()))
        # self.tree.setModel(self.dialog)
        # self.tree.doubleClicked.connect(self.treeClicked)
        # self.currentDir = QDir.root().dirName()
        # self.tree.setRootIndex(self.dialog.index(self.currentDir))
        # self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)

        #Actions
        self.actions = ActionsApp(self)

        #Ui buttons
        # self.redo_btn = self.ui.redo_btn
        # self.undo_btn = self.ui.undo_btn
        # self.levelUp_btn = self.ui.up_btn
        # self.update_move_btn()

        # connect buttons
        # self.redo_btn.clicked.connect(self.redo)
        # self.undo_btn.clicked.connect(self.undo)
        # self.levelUp_btn.clicked.connect(self.parent)

        # Shortcuts
        self.copy_short = QShortcut(QKeySequence("Ctrl+A"), self)
        self.copy_short.activated.connect(FileOperations.copy)
        self.copy_short = QShortcut(QKeySequence("Ctrl+S"), self)
        self.copy_short.activated.connect(FileOperations.paste)
        self.copy_short = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.copy_short.activated.connect(FileOperations.cut)
        self.copy_short = QShortcut(QKeySequence("Ctrl+D"), self)
        self.copy_short.activated.connect(FileOperations.delete)

        # self.treeClicked_Signal.connect(self.treeClicked)
        # self.rendeRoot_Signal.connect(self.render_new_root)

    def treeClicked(self, index):
        file = self.FileS.engine.filePath(index)
        self.filePath.setText(f"{file}")
        self.FileV.last_move.insert(0, self.currentDir)
        self.render_new_root(file)

    ## File Operations
    # def newFolder(self):
    #     folderName, ok = QInputDialog.getText(self, "Ввод", "Название папки: ", QLineEdit.Normal)
    #     if ok:
    #         QDir(self.currentDir).mkdir(f"{folderName}")

    # def newFile(self):
    #     fileName, ok = QInputDialog.getText(self, "Ввод", "Название файла: ", QLineEdit.Normal)
    #     file = f"{self.currentDir}/{fileName}"
    #     if ok:
    #         with open(file, "w") as file:
    #             pass

    # def delete(self, items = []):
    #     indexes = self.getSelectedFiles()
    #     if items:
    #         indexes = items
    #     print(indexes)
    #     if len(indexes) > 0:
    #         quest = f"Удалить {len(indexes)} элементов"
    #         willDelete = QMessageBox.question(self, "Удаление", quest, QMessageBox.Yes|QMessageBox.No)
    #         if willDelete == QMessageBox.StandardButton.Yes:
    #             for index in indexes:
    #                 self.dialog.remove(index)

    # def delete_cut_items(self, items = []):
    #     print(items)
    #     for index in items:
    #         self.dialog.remove(index)



    # def copy(self):
    #     files = self.getSelectedFiles()
    #     self.savedFiles = files

    # def cut(self):
    #     # get selected files
    #     files = self.savedFiles
    #     if files:
    #         quest = f"Вырезать {len(files)} элементов"
    #         willDelete = QMessageBox.question(self, "Вырезание", quest, QMessageBox.Yes|QMessageBox.No)
    #         if willDelete == QMessageBox.StandardButton.Yes:
    #             self.paste()
    #             self.delete_cut_items(files)

    # def paste(self):
    #     willPaste = QMessageBox.question(self, "Вставка", "Вставить файлы в настоящую директорию", QMessageBox.Yes|QMessageBox.No)
    #     if not willPaste == QMessageBox.StandardButton.Yes:
    #         return
    #     for file in self.savedFiles:
    #         if self.dialog.fileInfo(file).isDir():
    #             filePath = self.dialog.filePath(file)
    #             fileName = self.dialog.fileName(file)


    #             files = os.listdir(self.currentDir)

    #             if os.path.isdir(filePath):
    #                 counter = 0
    #                 for f in files:
    #                     if f.startswith(fileName):
    #                         counter += 1
    #                         print(f, counter)
    #                 if counter == 0 or counter == 1:
    #                     shutil.copytree(filePath, f"{self.currentDir}/{fileName} - copy")
    #                 else:
    #                     shutil.copytree(filePath, f"{self.currentDir}/{fileName} - copy ({counter})")
    #             else:
    #                 shutil.copytree(filePath, f"{self.currentDir}/{fileName}")
    #         elif self.dialog.fileInfo(file).isFile():
    #             filePath = self.dialog.filePath(file)
    #             fileName = self.dialog.fileName(file)
    #             shutil.copy2(filePath, f"{self.currentDir}/{fileName}")

    # def move_file(self, fromPath, toPath):
    #     if fromPath and toPath:
    #         shutil.move(fromPath, toPath)

    # def move (self):
    #     file = self.getSingleSelectedFile()
    #     if file:
    #         dia = FolderSelectorDialog()
    #         result = dia.exec_()

    #         if result == QDialog.Accepted:
    #             selected_directory = self.dialog.filePath(dia.tree_view.currentIndex())
    #             fileName = self.dialog.fileName(file)
    #             fromPath = self.dialog.filePath(file)
    #             toPath = f"{selected_directory}/{fileName}"
    #             quest = f"Переместить {fileName} из {fromPath} в {toPath}"
    #             willMove = QMessageBox.question(self, "Move item", quest, QMessageBox.Yes|QMessageBox.No)
    #             if willMove == QMessageBox.StandardButton.Yes:
    #                 self.move_file(fromPath, toPath)

    # def rename (self):
    #     file = self.getSingleSelectedFile()
    #     if file:
    #         itemPath = self.dialog.filePath(file)
    #         item = QFile(itemPath)
    #         fileName, ok = QInputDialog.getText(self, "Ввод", "Новое имя: ", QLineEdit.Normal)
    #         filePath = f"{self.currentDir}/{fileName}"
    #         if item.rename(filePath):
    #             print("New file name")
    #         else:
    #             print("Cannot rename file")

    def render_new_root(self, dir):
        self.filePath.setText(f"{dir}")
        dirIndex = self.FileS._engine.index(dir)
        self.FileV.rootIndex = dirIndex
        self.currentDir = dir
        self.FileV.update_move_btn()
        self.FileV.tree.clearSelection()


    ## Tree View Operations
    # def treeClicked(self, index):
    #     file = self.dialog.filePath(index)
    #     self.filePath.setText(f"{file}")
    #     self.last_move.insert(0, self.currentDir)
    #     self.render_new_root(file)


    # def update_move_btn(self):
    #     len_next = len(self.next_move)
    #     len_last = len(self.last_move)

    #     if (len_next == 0):
    #         self.redo_btn.setEnabled(False)
    #     else:
    #         self.redo_btn.setEnabled(True)

    #     if (len_last == 0):
    #         self.undo_btn.setEnabled(False)
    #     else:
    #         self.undo_btn.setEnabled(True)

    #     if (self.currentDir == ''):
    #         self.levelUp_btn.setEnabled(False)
    #     else:
    #         self.levelUp_btn.setEnabled(True)

    # def parent (self):
    #     dirs = self.currentDir.split('/')

    #     if (len(dirs) == 1):
    #         self.render_new_root('')
    #     else:
    #         path = '/'.join(dirs[0:len(dirs)-1])
    #         self.render_new_root(path)


    # def undo (self):
    #     if (len(self.last_move) == 0): return
    #     last = self.last_move.pop(0)
    #     if (last is self.currentDir):
    #         if (not (self.currentDir in self.last_move) and not(self.currentDir in self.next_move)):
    #             self.next_move.insert(0, self.currentDir)
    #         if (not (last in self.next_move)):
    #             self.next_move.insert(0, last)
    #         last = self.last_move.pop(0)
    #     if (not (self.currentDir in self.last_move) and not(self.currentDir in self.next_move)):
    #         self.next_move.insert(0, self.currentDir)
    #     if (not (last in self.next_move)):
    #             self.next_move.insert(0, last)
    #     self.render_new_root(last)

    # def redo (self):
    #     if (len(self.next_move) == 0): return
    #     next = self.next_move.pop(0)
    #     if (next is self.currentDir):
    #         if (not (next in self.last_move)):
    #             self.last_move.insert(0, next)
    #         next = self.next_move.pop(0)
    #     if (not (next in self.last_move)):
    #         self.last_move.insert(0, next)
    #     self.render_new_root(next)

    # def getSelectedFiles(self):
    #     files = self.tree.selectionModel().selectedIndexes()
    #     uniqueFiles = []
    #     for file in files:
    #         path = self.dialog.filePath(file)
    #         if not path in uniqueFiles:
    #             uniqueFiles.append(path)
    #     uniqueFiles = [self.dialog.index(x) for x in uniqueFiles]
    #     return uniqueFiles

    # def getSingleSelectedFile(self):
    #     files = self.getSelectedFiles()
    #     if len(files) == 1:
    #         return files[0]
    #     else:
    #         return None

    def resizeEvent(self, event):
        self.FileV.tree.resize(QSize(self.ui.treeView.width(), self.ui.treeView.height()))

    def showEvent(self, event):
        self.FileV.tree.resize(QSize(self.ui.treeView.width(), self.ui.treeView.height()))

