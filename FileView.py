from PySide6.QtWidgets import QWidget, QAbstractItemView, QListView, QPushButton, QSizePolicy, QSpacerItem
from PySide6.QtWidgets import QVBoxLayout, QLineEdit, QListWidget, QListWidgetItem, QFileDialog, QDialog
from PySide6.QtCore import QSize, QDir, Qt, QSortFilterProxyModel, QRegularExpression, Signal

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

class FileListWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.current_path = QDir.rootPath()  # Start with the root directory
        self.original_items = []

        self.search_edit = QLineEdit()
        self.list_widget = QListWidget()

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.search_edit)
        self.layout.addWidget(self.list_widget)

        self.populate_list()

        self.search_edit.textChanged.connect(self.handle_search_text_changed)

    def populate_list(self):
        self.list_widget.clear()
        self.original_items = []

        dir_model = QDir(self.current_path)

        # List files and directories
        entries = dir_model.entryList(QDir.AllEntries | QDir.NoDotAndDotDot)
        for entry in entries:
            list_item = QListWidgetItem(entry)
            self.original_items.append(list_item)
            self.list_widget.addItem(list_item)

    def handle_search_text_changed(self, text):
        if text:
            self.filter_items(text)
        else:
            self.list_widget.clear()
            self.list_widget.addItems(self.original_items)

    def filter_items(self, filter_text):
        self.list_widget.clear()
        filtered_items = []
        for item in self.original_items:
            print(item.text())
        # self.list_widget.addItems(filtered_items)

    def browse_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory", self.current_path)
        if directory:
            self.current_path = directory
            self.populate_list()

class CustomSortFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.setSourceModel(model)
        self.setFilterRegularExpression(QRegularExpression(''))
        self.regex = ''

    def setCustomFilter(self, regex):
        self.setFilterRegularExpression(regex)

    def changeSearch(self, text):
        print(text)
        self.setFilterRegularExpression(QRegularExpression(f"{text}", QRegularExpression.CaseInsensitiveOption))
        self.regex = text

    def filterAcceptsRow(self, sourceRow, sourceParent):
        sourceIndex = self.model.index(sourceRow, 0, sourceParent)
        data = self.model.data(sourceIndex)
        root_path = self.model.rootPath()
        root_path = QDir(root_path).canonicalPath()
        root_path = QDir.cleanPath(root_path)
        root_index_path = self.model.index(root_path)

        return True


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

        self.last_move = []
        self.next_move = []

        self.tree_ui = self.app.ui.treeView

        self.tree = CustomListView(self.tree_ui)
        self.tree.resize(QSize(self.tree_ui.width(), self.tree_ui.height()))
        self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.tree.enterPressed.connect(self.onEnterPressed)  # Connect the signal to a slot

        self.proxyModel = CustomSortFilterProxyModel(self.app.FileS.engine)

        self.tree.setModel(self.proxyModel)
        self.tree.setRootIndex(self.proxyModel.mapFromSource(self.app.FileS.engine.index(self.app.currentDir)))
        # self.tree.setModel(self.app.FileS.engine)
        # self.tree.setRootIndex(self.app.FileS.engine.index(self.app.currentDir))

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
        self.tree.setRootIndex(self.proxyModel.mapFromSource(index))
        # self.tree.setRootIndex(index)

    def getSelectedFiles(self):
        files = self.tree.selectionModel().selectedIndexes()
        uniqueFiles = []
        for file in files:
            path = self.app.FileS.engine.filePath(self.proxyModel.mapToSource(file))
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

    def onEnterPressed(self, event):
        enterFile = self.getSingleSelectedFile()
        if enterFile:
            enterFile = self.proxyModel.mapFromSource(enterFile)
            self.app.treeClicked_Signal.emit(enterFile)





