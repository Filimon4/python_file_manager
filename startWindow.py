from PySide6.QtWidgets import QMainWindow, QFileSystemModel, QSplitter, QTreeView, QWidget, QVBoxLayout
from PySide6.QtCore import QDir

class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File title")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.dialog = QFileSystemModel()
        self.dialog.setRootPath(QDir.currentPath())

        self.tree = QTreeView(self.central_widget)
        self.tree.setModel(self.dialog)
        self.tree.setRootIndex(self.dialog.index(QDir.rootPath()))


        self.layout.addWidget(self.tree)

        # class SimpleFileManager(QMainWindow):
        #     def __init__(self):
        #         super(SimpleFileManager, self).__init__()

        #         self.setWindowTitle("Simple File Manager")
        #         self.setGeometry(100, 100, 800, 600)

        #         self.central_widget = QWidget(self)
        #         self.setCentralWidget(self.central_widget)

        #         self.layout = QVBoxLayout(self.central_widget)

        #         # File Tree
        #         self.model = QFileSystemModel()
        #         self.model.setRootPath(QDir.rootPath())  # Display files starting from the root directory

        #         self.tree_view = QTreeView(self.central_widget)
        #         self.tree_view.setModel(self.model)
        #         self.tree_view.setRootIndex(self.model.index(QDir.rootPath()))

        #         self.layout.addWidget(self.tree_view)











