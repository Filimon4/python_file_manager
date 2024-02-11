from PySide6.QtWidgets import QPushButton, QFileDialog, QDialog, QAbstractItemView, QApplication, QMessageBox, QDialog, QLineEdit, QInputDialog, QSizePolicy, QMainWindow, QFileSystemModel, QListView, QTreeView, QWidget, QVBoxLayout, QLabel, QTreeWidget, QSplitter
from PySide6.QtCore import QFileInfo, QDir, QSize, QModelIndex, QFile, QIODevice, Qt
from PySide6.QtGui import QKeySequence, QShortcut
from ui_mainwindow import Ui_MainWindow

import sys, shutil, os

class StartWindow(QMainWindow, Ui_MainWindow):
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
        self.setWindowTitle("File Explorer")
        self.setGeometry(100, 100, 900, 600)

        # current dir
        self.filePath = self.ui.directory
        self.filePath.setText(f"Current: {QDir.root().dirName()}")

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
        self.about_action = self.ui.actionAbout
        self.quit_action = self.ui.actionQuit
        self.about_qt_action = self.ui.actionAbout_Qt

        self.newFile_action = self.ui.actionMake_folder
        self.newFolder_action = self.ui.actionNew_File
        self.delete_action = self.ui.actionDelete_folder
        self.rename_action = self.ui.actionRename
        self.move_action = self.ui.actionMove


        #Ui buttons
        self.redo_btn = self.ui.redo_btn
        self.undo_btn = self.ui.undo_btn
        self.levelUp_btn = self.ui.up_btn
        self.update_move_btn()

        self.newFolder_btn = self.ui.newFolder_btn
        self.newFile_btn = self.ui.newFile_btn
        self.delete_btn = self.ui.delete_btn
        self.copy_btn = self.ui.copy_btn
        self.paste_btn = self.ui.paste_btn
        self.cut_btn = self.ui.cut_btn

        # connect actions
        self.quit_action.triggered.connect(self.quit)
        self.about_qt_action.triggered.connect(self.about_qt)
        self.about_action.triggered.connect(self.about)
        self.newFile_action.triggered.connect(self.newFolder)
        self.newFolder_action.triggered.connect(self.newFile)
        self.delete_action.triggered.connect(self.delete)
        self.rename_action.triggered.connect(self.rename)
        self.move_action.triggered.connect(self.move)

        # connect buttons
        self.redo_btn.clicked.connect(self.redo)
        self.undo_btn.clicked.connect(self.undo)
        self.levelUp_btn.clicked.connect(self.parent)

        self.newFolder_btn.clicked.connect(self.newFolder)
        self.newFile_btn.clicked.connect(self.newFile)
        self.copy_btn.clicked.connect(self.copy)
        self.paste_btn.clicked.connect(self.paste)
        self.cut_btn.clicked.connect(self.cut)
        self.delete_btn.clicked.connect(self.delete)

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
        folderName, ok = QInputDialog.getText(self, "Ввод", "Folder name: ", QLineEdit.Normal)
        if ok:
            QDir(self.currentDir).mkdir(f"{folderName}")
        print('new folder')
    def newFile(self):
        fileName, ok = QInputDialog.getText(self, "Ввод", "File name: ", QLineEdit.Normal)
        file = f"{self.currentDir}/{fileName}"
        print(file)
        with open(file, "w") as file:
            pass
        print('new file')
    def delete(self, items = []):
        indexes = self.getSelectedFiles()
        if items:
            indexes = items
        print(indexes)
        if len(indexes) > 0:
            quest = f"Do you want to delete {len(indexes)} items"
            willDelete = QMessageBox.question(self, "Delete items", quest, QMessageBox.Yes|QMessageBox.No)
            if willDelete == QMessageBox.StandardButton.Yes:
                for index in indexes:
                    fileName = self.tree.model().data(index)
                    filePath = self.dialog.fileInfo(index)
                    self.dialog.remove(index)
        print('new delete')

    def delete_cut_items(self, items = []):
        print(items)
        for index in items:
            fileName = self.tree.model().data(index)
            filePath = self.dialog.fileInfo(index)
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
            quest = f"Do you want to cut {len(files)} items"
            willDelete = QMessageBox.question(self, "Cut items", quest, QMessageBox.Yes|QMessageBox.No)
            if willDelete == QMessageBox.StandardButton.Yes:
                self.paste()
                self.delete_cut_items(files)
        print('new cut')

    def paste(self):
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
        self.filePath.setText(f"Current: {file}")
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
            fileName, ok = QInputDialog.getText(self, "Ввод", "New file name: ", QLineEdit.Normal)
            filePath = f"{self.currentDir}/{fileName}"
            if item.rename(filePath):
                print("New file name")
            else:
                print("Cannot rename file")

    def move (self):
        file = self.getSingleSelectedFile()
        if file:
            fileDialog = QDialog(self)
            quest = f"Do you want to move {file}"
            willDelete = QMessageBox.question(self, "Move item", quest, QMessageBox.Yes|QMessageBox.No)
            if willDelete == QMessageBox.StandardButton.Yes:
                dia = FolderSelectorDialog()
                result = dia.exec_()

                if result == QDialog.Accepted:
                    selected_directory = dia.tree_view.currentIndex().data(Qt.DisplayRole)
                    print(dia.tree_view.currentIndex().data(Qt.DisplayRole))
                    print(self.dialog.filePath(dia.tree_view.currentIndex()))

                # if folderName:
                #     quest = f"Do you want to move {file} to {folderName}"
                #     willDelete = QMessageBox.question(self, "Move item", quest, QMessageBox.Yes|QMessageBox.No)
                #     if willDelete == QMessageBox.StandardButton.Yes:
                #         print('move')

    # render new rootindex
    def render_new_root(self, dir):
        self.filePath.setText(f"Current: {dir}")
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
        dialog.setText('''About\n\nThis is my college project\nBasic file explorer''')
        dialog.setWindowTitle("About")
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

        # Set up the UI components
        self.init_ui()

    def init_ui(self):
        # Create a layout
        layout = QVBoxLayout()

        # Create a QLineEdit to display the selected folder name
        self.folder_name_line_edit = QLineEdit()
        self.folder_name_line_edit.setReadOnly(True)
        layout.addWidget(self.folder_name_line_edit)

        # Create a QTreeView
        self.tree_view = QTreeView()
        layout.addWidget(self.tree_view)

        # Create a QFileSystemModel
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())  # You can set any initial root path here
        self.model.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)  # Show only directories
        self.tree_view.setModel(self.model)

        # Set the root index of the tree view to the root path
        root_index = self.model.index(QDir.rootPath())

        # Set up the buttons
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)

        # Add buttons to the layout
        layout.addWidget(ok_button)
        layout.addWidget(cancel_button)

        # Set the layout for the dialog
        self.setLayout(layout)

        # Connect item selection signal to custom slot
        self.tree_view.selectionModel().selectionChanged.connect(self.handle_selection_change)

    def handle_selection_change(self, selected, deselected):
            # Enable OK button only if an item is selected and it is a directory
            selected_indexes = selected.indexes()
            if selected_indexes:
                current_index = selected_indexes[0]
                selected_directory = self.model.filePath(current_index)
                self.setEnabled_ok_button(QFileInfo(selected_directory).isDir())

                # Update the QLineEdit with the selected folder name
                self.folder_name_line_edit.setText(selected_directory)
            else:
                self.setEnabled_ok_button(False)
                self.folder_name_line_edit.clear()

    def setEnabled_ok_button(self, enabled):
        # Enable or disable the OK button
        ok_button = self.layout().itemAt(1).widget()  # Assumes OK button is the second item in layout
        ok_button.setEnabled(enabled)

