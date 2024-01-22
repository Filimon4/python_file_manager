from PySide6.QtWidgets import QMainWindow, QFileSystemModel, QTreeView, QWidget, QVBoxLayout, QLabel, QTreeWidget, QSplitter
from PySide6.QtCore import QDir
from ui_mainwindow import Ui_MainWindow

class StartWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File title")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.filePath = QLabel()
        self.filePath.setText(f"Current: {QDir.root().dirName()}")

        self.dialog = QFileSystemModel(self)
        self.dialog.setRootPath(QDir.currentPath())
        self.dialog.rootPathChanged.connect(self.pathChanged)

        self.tree = QTreeView(self.central_widget)
        self.tree.setModel(self.dialog)
        self.tree.doubleClicked.connect(self.treeClicked)
        self.tree.setRootIndex(self.dialog.index(QDir.root().dirName()))

        self.layout.addWidget(self.filePath)
        self.layout.addWidget(self.tree)



    def pathChanged(self, path):
        print(path)

    def treeClicked(self, index):
        file = self.dialog.filePath(index)
        self.filePath.setText(f"Current: {file}")
        self.tree.setRootIndex(self.dialog.index(file))











