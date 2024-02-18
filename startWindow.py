import sys
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
    QFile
)
from PySide6.QtGui import QKeySequence, QShortcut
from ui_mainwindow import Ui_MainWindow

class FileSystem:

    def __init__(self):
        pass

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

        self.quit_action.triggered.connect(self.app.quit)
        self.about_qt_action.triggered.connect(self.app.about_qt)
        self.about_action.triggered.connect(self.app.about)
        self.newFile_action.triggered.connect(self.app.newFolder)
        self.newFolder_action.triggered.connect(self.app.newFile)
        self.delete_action.triggered.connect(self.app.delete)
        self.rename_action.triggered.connect(self.app.rename)
        self.move_action.triggered.connect(self.app.move)
        self.copy_action.triggered.connect(self.app.copy)
        self.paste_action.triggered.connect(self.app.paste)
        self.cut_action.triggered.connect(self.app.cut)

class FileExplorerApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # logic
        self.last_move = []
        self.next_move = []
        self.currentDir = ''
        self.savedFiles = []

        # ui.ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Файловый менеджер")
        self.setGeometry(100, 100, 900, 600)

        # ui elements
        self.filePath = self.ui.directory
        self.filePath.setText(f"{QDir.root().dirName()}")

        # QFileSystemModel
        self.dialog = QFileSystemModel(self)
        self.dialog.setRootPath(QDir.currentPath())

        # QTreeView
        self.tree_ui = self.ui.treeView
        self.tree = QListView(self.ui.treeView)
        self.tree.resize(QSize(self.ui.treeView.width(), self.ui.treeView.height()))
        self.tree.setModel(self.dialog)
        self.tree.doubleClicked.connect(self.treeClicked)
        self.currentDir = QDir.root().dirName()
        self.tree.setRootIndex(self.dialog.index(self.currentDir))
        self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)

        #Actions
        self.actions = ActionsApp(self)

        #Ui buttons
        self.redo_btn = self.ui.redo_btn
        self.undo_btn = self.ui.undo_btn
        self.levelUp_btn = self.ui.up_btn
        self.update_move_btn()

        # connect buttons
        self.redo_btn.clicked.connect(self.redo)
        self.undo_btn.clicked.connect(self.undo)
        self.levelUp_btn.clicked.connect(self.parent)

        # Shortcuts
        self.copy_short = QShortcut(QKeySequence("Ctrl+A"), self)
        self.copy_short.activated.connect(self.copy)
        self.copy_short = QShortcut(QKeySequence("Ctrl+S"), self)
        self.copy_short.activated.connect(self.paste)
        self.copy_short = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.copy_short.activated.connect(self.cut)
        self.copy_short = QShortcut(QKeySequence("Ctrl+D"), self)
        self.copy_short.activated.connect(self.delete)


    def newFolder(self):
        # TODO: use os.mkdir function
        folderName, ok = QInputDialog.getText(self, "Ввод", "Название папки: ", QLineEdit.Normal)
        if ok:
            QDir(self.currentDir).mkdir(f"{folderName}")
        print('new folder')
    def newFile(self):
        fileName, ok = QInputDialog.getText(self, "Ввод", "Название файла: ", QLineEdit.Normal)
        file = f"{self.currentDir}/{fileName}"
        if ok:
            with open(file, "w") as file:
                pass
        print('new file')
    def delete(self, items = []):
        indexes = self.getSelectedFiles()
        if items:
            indexes = items
        print(indexes)
        if len(indexes) > 0:
            quest = f"Удалить {len(indexes)} элементов"
            willDelete = QMessageBox.question(self, "Удаление", quest, QMessageBox.Yes|QMessageBox.No)
            if willDelete == QMessageBox.StandardButton.Yes:
                for index in indexes:
                    self.dialog.remove(index)
        print('new delete')

    def delete_cut_items(self, items = []):
        print(items)
        for index in items:
            self.dialog.remove(index)
        print('new delete')

    def getSelectedFiles(self):
        files = self.tree.selectionModel().selectedIndexes()
        uniqueFiles = []
        for file in files:
            path = self.dialog.filePath(file)
            if not path in uniqueFiles:
                uniqueFiles.append(path)
        uniqueFiles = [self.dialog.index(x) for x in uniqueFiles]
        return uniqueFiles

    def getSingleSelectedFile(self):
        files = self.getSelectedFiles()
        if len(files) == 1:
            return files[0]
        else:
            return None

    def copy(self):
        files = self.getSelectedFiles()
        self.savedFiles = files
        print('new copy')

    def cut(self):
        # get selected files
        files = self.savedFiles
        if files:
            quest = f"Вырезать {len(files)} элементов"
            willDelete = QMessageBox.question(self, "Вырезание", quest, QMessageBox.Yes|QMessageBox.No)
            if willDelete == QMessageBox.StandardButton.Yes:
                self.paste()
                self.delete_cut_items(files)
        print('new cut')

    def paste(self):
        willPaste = QMessageBox.question(self, "Вставка", "Вставить файлы в настоящую директорию", QMessageBox.Yes|QMessageBox.No)
        if not willPaste == QMessageBox.StandardButton.Yes:
            return
        for file in self.savedFiles:
            if self.dialog.fileInfo(file).isDir():
                filePath = self.dialog.filePath(file)
                fileName = self.dialog.fileName(file)


                files = os.listdir(self.currentDir)

                if os.path.isdir(filePath):
                    counter = 0
                    for f in files:
                        if f.startswith(fileName):
                            counter += 1
                            print(f, counter)
                    if counter == 0 or counter == 1:
                        shutil.copytree(filePath, f"{self.currentDir}/{fileName} - copy")
                    else:
                        shutil.copytree(filePath, f"{self.currentDir}/{fileName} - copy ({counter})")
                else:
                    shutil.copytree(filePath, f"{self.currentDir}/{fileName}")
            elif self.dialog.fileInfo(file).isFile():
                filePath = self.dialog.filePath(file)
                fileName = self.dialog.fileName(file)
                shutil.copy2(filePath, f"{self.currentDir}/{fileName}")

    def treeClicked(self, index):
        file = self.dialog.filePath(index)
        self.filePath.setText(f"{file}")
        self.last_move.insert(0, self.currentDir)
        self.render_new_root(file)

    def parent (self):
        # TODO: Can be used os.path.join
        dirs = self.currentDir.split('/')

        if (len(dirs) == 1):
            self.render_new_root('')
        else:
            path = '/'.join(dirs[0:len(dirs)-1])
            self.render_new_root(path)


    def undo (self):
        if (len(self.last_move) == 0): return
        last = self.last_move.pop(0)
        if (last is self.currentDir):
            if (not (self.currentDir in self.last_move) and not(self.currentDir in self.next_move)):
                self.next_move.insert(0, self.currentDir)
            if (not (last in self.next_move)):
                self.next_move.insert(0, last)
            last = self.last_move.pop(0)
        if (not (self.currentDir in self.last_move) and not(self.currentDir in self.next_move)):
            self.next_move.insert(0, self.currentDir)
        if (not (last in self.next_move)):
                self.next_move.insert(0, last)
        self.render_new_root(last)

    def redo (self):
        if (len(self.next_move) == 0): return
        next = self.next_move.pop(0)
        if (next is self.currentDir):
            if (not (next in self.last_move)):
                self.last_move.insert(0, next)
            next = self.next_move.pop(0)
        if (not (next in self.last_move)):
            self.last_move.insert(0, next)
        self.render_new_root(next)

    def rename (self):
        file = self.getSingleSelectedFile()
        if file:
            itemPath = self.dialog.filePath(file)
            item = QFile(itemPath)
            fileName, ok = QInputDialog.getText(self, "Ввод", "Новое имя: ", QLineEdit.Normal)
            filePath = f"{self.currentDir}/{fileName}"
            if item.rename(filePath):
                print("New file name")
            else:
                print("Cannot rename file")


    def move_file(self, fromPath, toPath):
        if fromPath and toPath:
            shutil.move(fromPath, toPath)

    def move (self):
        file = self.getSingleSelectedFile()
        if file:
            dia = FolderSelectorDialog()
            result = dia.exec_()

            if result == QDialog.Accepted:
                selected_directory = self.dialog.filePath(dia.tree_view.currentIndex())
                fileName = self.dialog.fileName(file)
                fromPath = self.dialog.filePath(file)
                toPath = f"{selected_directory}/{fileName}"
                quest = f"Переместить {fileName} из {fromPath} в {toPath}"
                willMove = QMessageBox.question(self, "Move item", quest, QMessageBox.Yes|QMessageBox.No)
                if willMove == QMessageBox.StandardButton.Yes:
                    self.move_file(fromPath, toPath)

    # render new rootindex
    def render_new_root(self, dir):
        self.filePath.setText(f"{dir}")
        self.tree.setRootIndex(self.dialog.index(dir))
        self.currentDir = dir
        self.update_move_btn()
        self.tree.clearSelection()

    def update_move_btn(self):
        len_next = len(self.next_move)
        len_last = len(self.last_move)

        if (len_next == 0):
            self.redo_btn.setEnabled(False)
        else:
            self.redo_btn.setEnabled(True)

        if (len_last == 0):
            self.undo_btn.setEnabled(False)
        else:
            self.undo_btn.setEnabled(True)

        if (self.currentDir == ''):
            self.levelUp_btn.setEnabled(False)
        else:
            self.levelUp_btn.setEnabled(True)

    def quit(self):
        QApplication.quit()

    def about_qt(self):
        QApplication.aboutQt()

    def about(self):
        dialog = QMessageBox()
        dialog.setText('''О Программе\n\nНастоящий проекта был разработан по заказу предодователей ВятГу\nПроект: Файловый Менеджер''')
        dialog.setWindowTitle("О программе")
        dialog.setIcon(QMessageBox.Icon.Information)
        dialog.exec()

    # tree view resize
    def resizeEvent(self, event):
        self.tree.resize(QSize(self.ui.treeView.width(), self.ui.treeView.height()))

    def showEvent(self, event):
        self.tree.resize(QSize(self.ui.treeView.width(), self.ui.treeView.height()))


class FolderSelectorDialog(QDialog):
    def __init__(self):
        super(FolderSelectorDialog, self).__init__()

        layout = QVBoxLayout()

        self.setWindowTitle("Выбор папки")

        self.folder_name_line_edit = QLineEdit()
        self.folder_name_line_edit.setReadOnly(True)
        layout.addWidget(self.folder_name_line_edit)

        self.tree_view = QTreeView()
        layout.addWidget(self.tree_view)

        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())
        self.model.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)
        self.tree_view.setModel(self.model)

        ok_button = QPushButton("Ок")
        ok_button.clicked.connect(self.accept)
        cancel_button = QPushButton("Отмена")
        cancel_button.clicked.connect(self.reject)

        layout.addWidget(ok_button)
        layout.addWidget(cancel_button)

        self.setLayout(layout)

        self.tree_view.selectionModel().selectionChanged.connect(self.handle_selection_change)

    def handle_selection_change(self, selected, deselected):
            selected_indexes = selected.indexes()
            if selected_indexes:
                current_index = selected_indexes[0]
                selected_directory = self.model.filePath(current_index)
                self.setEnabled_ok_button(QFileInfo(selected_directory).isDir())

                self.folder_name_line_edit.setText(selected_directory)
            else:
                self.setEnabled_ok_button(False)
                self.folder_name_line_edit.clear()

    def setEnabled_ok_button(self, enabled):
        ok_button = self.layout().itemAt(1).widget()
        ok_button.setEnabled(enabled)

