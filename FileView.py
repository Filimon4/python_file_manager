from PySide6.QtWidgets import QWidget, QAbstractItemView, QListView, QPushButton, QSizePolicy, QSpacerItem
from PySide6.QtCore import QSize, QDir

class DiskButton(QPushButton):
    def __init__(self, disks, path):
        super().__init__()
        self.disks = disks
        self.path = path
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setMaximumHeight(25)
        self.setMaximumWidth(35)
        self.setText(self.path)
        self.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        self.disks.navigateToDisk(self.path)



class Disks:
    def __init__(self, app):
        self.app = app
        self.logicDisks = QDir.drives()
        self.driverView = self.app.ui.driverView

        for disk in self.logicDisks:
            button = DiskButton(self, disk.absolutePath())
            self.driverView.addWidget(button)
        self.driverView.addItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

    def navigateToDisk(self, path):
        self.app.rendeRoot_Signal.emit(path)


class FileView(QWidget):
    def __init__(self, app):
        super().__init__()

        self.app = app

        self.last_move = []
        self.next_move = []

        self.tree_ui = self.app.ui.treeView

        self.tree = QListView(self.tree_ui)
        self.tree.resize(QSize(self.tree_ui.width(), self.tree_ui.height()))
        self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.tree.setModel(self.app.FileS.engine)
        self.tree.setRootIndex(self.app.FileS.engine.index(self.app.currentDir))

        self.tree.doubleClicked.connect(self.treeClicked)

        self.redo_btn = self.app.ui.redo_btn
        self.undo_btn = self.app.ui.undo_btn
        self.levelUp_btn = self.app.ui.up_btn
        self.update_move_btn()

        self.redo_btn.clicked.connect(self.redo)
        self.undo_btn.clicked.connect(self.undo)
        self.levelUp_btn.clicked.connect(self.parent)

        print("rootIndex: ", self.tree.rootIndex())

    @property
    def rootIndex(self):
        return self.tree.rootIndex()

    @rootIndex.setter
    def rootIndex(self, index):
        self.tree.setRootIndex(index)

    def getSelectedFiles(self):
        files = self.tree.selectionModel().selectedIndexes()
        uniqueFiles = []
        for file in files:
            path = self.app.FileS.engine.filePath(file)
            if not path in uniqueFiles:
                uniqueFiles.append(path)
        uniqueFiles = [self.app.FileS.engine.index(x) for x in uniqueFiles]
        return uniqueFiles

    def getSingleSelectedFile(self):
        files = self.getSelectedFiles()
        if len(files) == 1:
            return files[0]
        else:
            return None

    def parent(self):
        dirs = self.app.currentDir.split('/')

        if not (QDir(self.app.currentDir).cdUp()):
            self.app.rendeRoot_Signal.emit('')
        else:
            path = '/'.join(dirs[0:len(dirs)-1])
            self.app.rendeRoot_Signal.emit(path)


    def undo (self):
        if (len(self.last_move) == 0): return
        last = self.last_move.pop(0)
        currentDir = self.app.currentDir
        if (last is currentDir):
            if (not (currentDir in self.last_move) and not(currentDir in self.next_move)):
                self.next_move.insert(0, currentDir)
            if (not (last in self.next_move)):
                self.next_move.insert(0, last)
            last = self.last_move.pop(0)
        if (not (currentDir in self.last_move) and not(currentDir in self.next_move)):
            self.next_move.insert(0, currentDir)
        if (not (last in self.next_move)):
            self.next_move.insert(0, last)
        self.app.rendeRoot_Signal.emit(last)

    def redo (self):
        if (len(self.next_move) == 0): return
        next = self.next_move.pop(0)
        currentDir = self.app.currentDir
        if (next is currentDir):
            if (not (next in self.last_move)):
                self.last_move.insert(0, next)
            next = self.next_move.pop(0)
        if (not (next in self.last_move)):
            self.last_move.insert(0, next)
        self.app.rendeRoot_Signal.emit(next)

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

        if (self.app.currentDir == ''):
            self.levelUp_btn.setEnabled(False)
        else:
            self.levelUp_btn.setEnabled(True)

    def resizeEvent(self, event):
        self.tree.resize(QSize(self.ui.treeView.width(), self.ui.treeView.height()))

    def treeClicked(self, index):
        self.app.treeClicked_Signal.emit(index)
