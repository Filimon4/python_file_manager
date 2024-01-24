from PySide6.QtWidgets import QSizePolicy, QMainWindow, QFileSystemModel, QTreeView, QWidget, QVBoxLayout, QLabel, QTreeWidget, QSplitter
from PySide6.QtCore import QDir
from PySide6.QtGui import QIcon, QHeaderView
from ui_mainwindow import Ui_MainWindow

class StartWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("File title")
        self.setGeometry(100, 100, 800, 600)

        # self.central_widget = QWidget(self)
        # self.setCentralWidget(self.central_widget)

        self.filePath = self.ui.directory
        self.filePath.setText(f"Current: {QDir.root().dirName()}")

        self.dialog = QFileSystemModel(self)
        self.dialog.setRootPath(QDir.currentPath())
        self.dialog.rootPathChanged.connect(self.pathChanged)

        self.tree = QTreeView(self.ui.treeView)
        self.tree.header().setResizeMode(QHeaderView.ResizeToContents)
        self.tree.header().setStretchLastSection(False)
        self.tree.setModel(self.dialog)
        self.tree.doubleClicked.connect(self.treeClicked)
        self.tree.setRootIndex(self.dialog.index(QDir.root().dirName()))

        # self.layout.addWidget(self.filePath)
        # self.layout.addWidget(self.tree)



    def pathChanged(self, path):
        print(path)

    def btn_clicked(self):
        print("clicked")

    def treeClicked(self, index):
        file = self.dialog.filePath(index)
        self.filePath.setText(f"Current: {file}")
        self.tree.setRootIndex(self.dialog.index(file))











