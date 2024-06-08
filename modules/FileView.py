from PySide6.QtWidgets import QWidget, QAbstractItemView, QListView, QPushButton, QSizePolicy, QSpacerItem
from PySide6.QtWidgets import QVBoxLayout, QLineEdit, QListWidget, QListWidgetItem, QFileDialog, QDialog
from PySide6.QtCore import QSize, QDir, Qt, QSortFilterProxyModel, QRegularExpression, Signal

class CustomListView(QListView):
    enterPressed = Signal(str)

    def __init__(self, ui):
        super().__init__(ui)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.enterPressed.emit(event)
        else:
            super().keyPressEvent(event)


class FileView(QWidget):
    def __init__(self, app):
        super().__init__()

        self.app = app
        
        self.moves = {
            "steps": [],
            "index": 0,
        }

        self.tree_ui = self.app.ui.treeView

        self.tree = CustomListView(self.tree_ui)
        self.tree.resize(QSize(self.tree_ui.width(), self.tree_ui.height()))
        self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.tree.enterPressed.connect(self.onEnterPressed)  # Connect the signal to a slot

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


    def update_steps(self, currentDir):
        self.moves["steps"] = [i for i in currentDir.split('/') if i ]
        self.moves["index"] = len(self.moves["steps"]) - 1

    def parent(self):
        dirs = self.app.currentDir.split('/')

        if not (QDir(self.app.currentDir).cdUp()):
            self.app.rendeRoot_Signal.emit('')
        else:
            path = '/'.join(dirs[0:len(dirs)-1])
            self.app.rendeRoot_Signal.emit(path)

    def undo(self):
        prevHop = self.moves["index"]-1
        if prevHop <= 0:
            prevHop = 0
        lastStep = '/'.join([i for i in self.moves['steps'][0:self.moves['index']]])
        self.moves["index"] = prevHop
        print(lastStep)

        self.app.renderVirtualRoot_Signal.emit(lastStep)

        

    def redo(self):
        nextHop = self.moves["index"]+1
        if nextHop >= len(self.moves["steps"])-1:
            nextHop = len(self.moves["steps"])-1
        self.moves["index"] = nextHop
        nextStep = '/'.join([i for i in self.moves['steps'][0:self.moves['index']+1]])
        print("NexStep: ", nextStep)

        self.app.renderVirtualRoot_Signal.emit(nextStep)


    def update_move_btn(self):
        self.levelUp_btn.setEnabled(False)
        self.undo_btn.setEnabled(False)
        self.redo_btn.setEnabled(False)

        lenSteps = len(self.moves['steps'])
        if lenSteps == 0:
            pass
        elif lenSteps == 1:
            self.undo_btn.setEnabled(True)
            self.levelUp_btn.setEnabled(True)
        elif lenSteps > 0 and self.moves['index']+1 < lenSteps:
            self.levelUp_btn.setEnabled(True)
            self.undo_btn.setEnabled(True)
            self.redo_btn.setEnabled(True)
        elif lenSteps == self.moves['index']+1:
            self.undo_btn.setEnabled(True)
            self.levelUp_btn.setEnabled(True)

    def resizeEvent(self, event):
        self.tree.resize(QSize(self.ui.treeView.width(), self.ui.treeView.height()))

    def treeClicked(self, index):
        self.app.treeClicked_Signal.emit(index)

    def onEnterPressed(self, event):
        enterFile = self.getSingleSelectedFile()
        if enterFile:
            self.app.treeClicked_Signal.emit(enterFile)
