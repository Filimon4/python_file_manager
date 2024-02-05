from PySide6.QtWidgets import QAbstractItemView, QApplication, QMessageBox, QDialog, QLineEdit, QInputDialog, QSizePolicy, QMainWindow, QFileSystemModel, QTreeView, QWidget, QVBoxLayout, QLabel, QTreeWidget, QSplitter
from PySide6.QtCore import QDir, QSize, QModelIndex, QFile, QIODevice
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
        # self.dialog.rootPathChanged.connect(self.pathChanged)

        # QTreeView
        self.tree_ui = self.ui.treeView
        self.tree = QTreeView(self.ui.treeView)
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

    def newFolder(self):
        # TODO: use os.mkdir function
        folderName, ok = QInputDialog.getText(self, "Ввод", "Folder name: ", QLineEdit.Normal)
        if ok:
            QDir(self.currentDir).mkdir(f"{folderName}")
        print('new folder')
    def newFile(self):
        fileName, ok = QInputDialog.getText(self, "Ввод", "Folder name: ", QLineEdit.Normal)
        file = f"{self.currentDir}/{fileName}"
        print(file)
        with open(file, "w") as file:
            pass
        print('new file')
    def delete(self):
        index = self.tree.currentIndex()
        if index:
            fileName = self.tree.model().data(index)
            filePath = self.dialog.fileInfo(index)
            desc = f"Do you want to delete folder: \"{fileName}\""
            if (filePath.dir().path() == self.currentDir):
                willDelete = QMessageBox.question(self, "Delete folder", desc, QMessageBox.Yes|QMessageBox.No)
                if willDelete == QMessageBox.StandardButton.Yes:
                    self.dialog.remove(index)
        print('new delete')
        # intersing code

        # if(model->fileInfo(index).isDir())
        # {
        #     // directory
        #     model->rmdir(index); (or os.rmdir)
        #     shutil.rmtree(str)
        # }
        # else
        # {
        #     // file
        #     model->remove(index);
        # }

    def getSelectedFiles(self):
        files = self.tree.selectionModel().selectedIndexes()
        uniqueFiles = []
        for file in files:
            path = self.dialog.filePath(file)
            if not path in uniqueFiles:
                uniqueFiles.append(path)
        uniqueFiles = [self.dialog.index(x) for x in uniqueFiles]
        return uniqueFiles

    def copy(self):
        files = self.getSelectedFiles()
        self.savedFiles = files
        print('new copy')
    def cut(self):
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

    def btn_clicked(self):
        print("clicked")

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

    def render_new_root(self, dir):
        self.filePath.setText(f"Current: {dir}")
        self.tree.setRootIndex(self.dialog.index(dir))
        self.currentDir = dir
        # print(f"last moves: {self.last_move}")
        # print(f"next moves: {self.next_move}")

        self.update_move_btn()

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

    # tree view events
    def resizeEvent(self, event):
        self.tree.resize(QSize(self.ui.treeView.width(), self.ui.treeView.height()))

    def showEvent(self, event):
        self.tree.resize(QSize(self.ui.treeView.width(), self.ui.treeView.height()))

